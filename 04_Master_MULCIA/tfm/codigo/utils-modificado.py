# Fragmentos de utils.py modificados para el TFM
#
# Basado en el archivo utils.py del repositorio:
#   https://github.com/pankessel/adv_explanation_ref
# de Pan Kessel, "Explanations can be manipulated and geometry is to blame",
# distribuido bajo licencia Apache 2.0.
#
# Modificaciones realizadas por Manuel Enciso Martínez (2026)
# para el Trabajo Fin de Máster (Universidad de Sevilla):
#   - Nuevas funciones de visualización:
#       * plot_overview2: figura extendida para comparar explicaciones y mostrar
#         diferencias |x_adv - x| y |h_adv - h^t|, con métricas SSIM y MSE.
#       * plot_overview_grid: figura en forma de rejilla para estudiar la influencia
#         de distintos valores de β sobre imágenes adversarias y mapas de calor.
#   - Ampliación de load_image para tratar correctamente imágenes PNG (conversión a RGB).
#   - Nuevas variantes de generación de mapas de explicabilidad con texto superpuesto:
#       * get_expl_with_text: añade el texto "Universidad De Sevilla" sobre el
#         mapa de calor original.


import os
import math
import numpy as np
import torch
import torch.nn.functional as F
import torchvision
from PIL import Image, ImageDraw, ImageFont

from pytorch_msssim import ssim

from .enums import ExplainingMethod

import matplotlib as mpl

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using non-interactive Agg backend")
    mpl.use("Agg")
import matplotlib.pyplot as plt


# ============================================================
# 1. Visualizaciones específicas para el TFM
# ============================================================


def plot_overview(
    images,
    heatmaps,
    mean,
    std,
    captions=(
        "Target Image",
        "Original Image",
        "Manipulated Image",
        "Target Explanation",
        "Original Explanation",
        "Manipulated Explanation",
    ),
    filename="overview.png",
    images_per_row=3,
):
    """
    Versión extendida de plot_overview que, además de mostrar imágenes
    y mapas de calor, calcula métricas entre:

      - x y x_adv (MSE de imagen)
      - h_0 y h_adv (MSE de mapa de calor)

    y pasa dichas métricas a la función plot_grid para mostrarlas en los títulos.
    """
    # Convertir tensores a imágenes numpy
    plots = [torch_to_image(img, mean, std) for img in images] + [
        heatmap_to_image(heatmap) for heatmap in heatmaps
    ]

    img_cmap = "jet"
    heatmap_cmap = "jet" if len(plots[-1].shape) == 3 else "coolwarm"
    cmaps = [img_cmap] * len(images) + [heatmap_cmap] * len(heatmaps)

    # Métricas en espacio tensorial original
    x_adv_x = F.mse_loss(images[1], images[2])        # MSE(x, x_adv)
    hx_adv_hx = F.mse_loss(heatmaps[1], heatmaps[2])  # MSE(h_0, h_adv)

    metricas = [x_adv_x, hx_adv_hx]

    plot_grid(
        plots,
        metricas,
        captions,
        cmap=cmaps,
        filename=filename,
        images_per_row=images_per_row,
    )



def plot_overview_grid(
    x_adv_list,
    adv_expl_list,
    org_expl_list,
    mean,
    std,
    rango_beta,
    valor_beta,
    filename="overview_beta.png",
):
    """
    Visualización usada en el análisis del β‑suavizado.

    Dibuja una figura con N filas y 3 columnas (N = len(rango_beta)):

      - Col 1: imagen adversaria x_adv (para un β fijo valor_beta)
      - Col 2: explicación adversaria h_adv para cada β de rango_beta
      - Col 3: explicación original h_0 para cada β de rango_beta
    """
    plots = []
    titles = []
    cmaps = []

    for i, beta in enumerate(rango_beta):
        # Columna 1: imagen adversaria (misma para todas las filas)
        img_adv = torch_to_image(x_adv_list[i], mean, std)
        plots.append(img_adv)
        titles.append(f"Imagen adversaria b={valor_beta}")
        cmaps.append("jet")

        # Columna 2: explicación adversaria
        hm_adv = heatmap_to_image(adv_expl_list[i])
        plots.append(hm_adv)
        titles.append(f"Explicacion Adversaria b={beta:.3f}")
        cmaps.append("coolwarm")

        # Columna 3: explicación original
        hm_org = heatmap_to_image(org_expl_list[i])
        plots.append(hm_org)
        titles.append(f"Explicacion Original b={beta:.3f}")
        cmaps.append("coolwarm")

    plot_grid(
        plots,
        metricas=None,   # aquí no mostramos métricas, solo títulos
        titles=titles,
        images_per_row=3,
        cmap=cmaps,
        filename=filename,
    )


# ============================================================
# 2. Carga de imagen (extensión PNG/JPG)
# ============================================================

def load_image(data_mean, data_std, device, image_name):
    """
    Carga una imagen en un tensor torch (1, C, H, W) con el preprocesado
    habitual de ImageNet (resize 256, center crop 224, normalización).

    Extensión respecto a la versión original:
      - Si la imagen es PNG, se fuerza la conversión a RGB para garantizar
        3 canales, evitando problemas con PNG en escala de grises o con alfa.
    """
    im = Image.open(image_name)
    if image_name.lower().endswith(".png"):
        im = im.convert("RGB")  # PNG → fuerza RGB (3 canales)

    x = torchvision.transforms.Normalize(mean=data_mean, std=data_std)(
        torchvision.transforms.ToTensor()(
            torchvision.transforms.CenterCrop(224)(
                torchvision.transforms.Resize(256)(im)
            )
        )
    )
    x = x.unsqueeze(0).to(device)
    return x


# ============================================================
# 3. Mapas de explicabilidad con texto superpuesto
# ============================================================

def get_expl_with_text(
    model,
    x,
    method,
    desired_index=None,
    intensity=0.8,
):
    """
    Variante de get_expl que añade el texto "Universidad De Sevilla" al mapa
    de calor ANTES del colapso de canales.

    - Se obtiene el heatmap bruto h(x) (vía gradiente o analyze).
    - Si el método lo requiere, se aplica grad*input.
    - Se construye una máscara binaria con el texto en una imagen 128x128,
      se reescala a (H, W) y se expande a los canales de h(x).
    - Se suma mask_txt * max_val a h(x), donde max_val es 0.8 * max(|h(x) * x|).
    - Finalmente se colapsan canales y se normaliza por la suma.
    """
    x.requires_grad = True
    acc, class_idx = model.classify(x)
    if desired_index is None:
        desired_index = class_idx

    # Heatmap bruto
    if method == ExplainingMethod.integrated_grad:
        num_summands = 30
        prefactors = x.new_tensor(
            [k / num_summands for k in range(1, num_summands + 1)]
        )
        parallel_model = torch.nn.DataParallel(model)
        y = parallel_model(prefactors.view(num_summands, 1, 1, 1) * x)

        y = torch.nn.functional.softmax(y, 1)[:, int(desired_index)]
        y = (1.0 / num_summands) * torch.sum(y / prefactors, dim=0)
        heatmap = torch.autograd.grad(y, x, create_graph=True)[0]
    else:
        heatmap = model.analyze(method=method, R=None, index=desired_index)

    # grad*input si aplica
    if method in (ExplainingMethod.grad_times_input, ExplainingMethod.integrated_grad):
        heatmap = heatmap * x

    with torch.no_grad():
        max_val = (heatmap * x).abs().max() * intensity
        _, _, H, W = x.shape

        base_H, base_W = 128, 128
        img_txt = Image.new("L", (base_W, base_H), 0)
        draw = ImageDraw.Draw(img_txt)

        # Intento de cargar fuente en distintos sistemas
        try:
            font = ImageFont.truetype("arialbd.ttf", size=22)
            print("Fuente cargada: Windows Arial Bold")
        except OSError as e1:
            print("No se pudo cargar Arial Bold:", e1)
            try:
                font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size=20
                )
                print("Fuente cargada: Linux DejaVuSerif-Bold")
            except OSError as e2:
                print("No se pudo cargar DejaVuSerif-Bold:", e2)
                font = ImageFont.load_default()
                print("Fuente cargada: DEFAULT de Pillow")

        # Texto en tres líneas: "Universidad", "De", "Sevilla"
        text_top = "Universidad"
        left, top, right, bottom = draw.textbbox((0, 0), text_top, font=font)
        w_top, h_top = right - left, bottom - top
        x_top = (base_W - w_top) // 2
        y_top = int(base_H * 0.10)
        draw.text((x_top, y_top), text_top, fill=255, font=font)

        text_mid = "De"
        left, top, right, bottom = draw.textbbox((0, 0), text_mid, font=font)
        w_mid, h_mid = right - left, bottom - top
        x_mid = (base_W - w_mid) // 2
        y_mid = int(base_H * 0.40)
        draw.text((x_mid, y_mid), text_mid, fill=255, font=font)

        text_bot = "Sevilla"
        left, top, right, bottom = draw.textbbox((0, 0), text_bot, font=font)
        w_bot, h_bot = right - left, bottom - top
        x_bot = (base_W - w_bot) // 2
        y_bot = int(base_H * 0.70)
        draw.text((x_bot, y_bot), text_bot, fill=255, font=font)

        mask_txt = torch.from_numpy(np.array(img_txt, dtype=np.float32))
        mask_txt = mask_txt.unsqueeze(0).unsqueeze(0) / 255.0
        mask_txt = F.interpolate(
            mask_txt, size=(H, W), mode="bilinear", align_corners=False
        )
        mask_txt = mask_txt.to(x.device)
        mask_txt = mask_txt.expand_as(heatmap)

        # Superposición del texto
        heatmap = heatmap + mask_txt * max_val

    # Colapso de canales y normalización por suma
    heatmap = torch.sum(torch.abs(heatmap), dim=1)      # [1,H,W]
    normalized_heatmap = heatmap / torch.sum(heatmap)   # suma = 1

    return normalized_heatmap, acc, class_idx
