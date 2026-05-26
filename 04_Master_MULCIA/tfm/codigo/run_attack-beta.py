# Copyright 2019
# Original code from Pan Kessel, "Explanations can be manipulated and geometry is to blame"
# Repository: https://github.com/pankessel/adv_explanation_ref
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------
# Modificaciones para el Trabajo Fin de Máster de Manuel Enciso Martínez:
#   - Uso de una única imagen como entrada; el mapa de calor objetivo
#     se genera superponiendo texto sobre la misma imagen mediante
#     get_expl_with_text, en lugar de usar una segunda imagen de destino.
#   - Inclusión de un parámetro --beta_value y lógica beta_growth para
#     fijar un valor concreto de β en las activaciones softplus de la red.
#   - Registro detallado por iteración de las pérdidas de explicación
#     (loss_expl) y de clasificación (loss_output).
#   - Generación de una figura de resumen (plot_overview) con imagen
#     original, mapa original y mapa adversario.
#   - Guardado de la imagen adversaria desnormalizada como JPEG, junto
#     con un fichero de texto con predicciones y métricas (MSE, MAE).
# ----------------------------------------------------------------------

"""
Script para ejecutar el ataque adversario sobre el mapa de explicaciones
usando una única imagen como base.

A partir de una imagen se genera:
  1) El mapa de calor original (org_expl) y un mapa objetivo alterado con
     texto superpuesto (target_expl), usando get_expl_with_text.
  2) Una imagen adversaria x_adv optimizando la diferencia entre el mapa
     original y el mapa objetivo, manteniendo la predicción de clase.

Permite fijar un valor concreto de β para las activaciones softplus de la
red (mediante --beta_growth y --beta_value).
"""

import argparse
from datetime import datetime

import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import torchvision.transforms as T

from nn.enums import ExplainingMethod
from nn.networks import ExplainableNet
from nn.utils import (
    get_expl,
    get_expl_with_text,
    plot_overview,
    clamp,
    load_image,
    make_dir,
)


def get_beta(i: int, num_iter: int) -> float:
    """
    Función auxiliar para crecimiento progresivo de β (no utilizada en la
    configuración actual, pero mantenida para compatibilidad).

    Realiza un crecimiento exponencial de β entre start_beta y end_beta a
    lo largo de num_iter iteraciones.
    """
    start_beta, end_beta = 10.0, 100.0
    return start_beta * (end_beta / start_beta) ** (i / num_iter)


def parse_args() -> argparse.Namespace:
    """Parsea y devuelve los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description=(
            "Ataque adversario sobre explicaciones con un único mapa objetivo "
            "generado a partir de texto superpuesto."
        )
    )

    parser.add_argument(
        "--num_iter",
        type=int,
        default=1500,
        help="Número de iteraciones del optimizador",
    )
    parser.add_argument(
        "--img",
        type=str,
        default="../data/collie4.jpeg",
        help="Ruta a la imagen (ImageNet) sobre la que se ejecuta el ataque",
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=2e-4,
        help="Tasa de aprendizaje (learning rate) del optimizador Adam",
    )
    parser.add_argument(
        "--cuda",
        action="store_true",
        help="Si se indica, ejecuta el experimento en GPU",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="../output/",
        help="Directorio donde se guardarán las figuras de salida",
    )
    parser.add_argument(
        "--beta_growth",
        action="store_true",
        help=(
            "Si se indica, se empleará activación softplus con el valor de β "
            "proporcionado en --beta_value (o crecimiento, si se adapta get_beta)."
        ),
    )
    parser.add_argument(
        "--beta_value",
        type=float,
        help=(
            "Valor de β a usar en las activaciones softplus "
            "cuando se activa --beta_growth"
        ),
    )
    parser.add_argument(
        "--prefactors",
        nargs=2,
        type=float,
        default=[1e11, 1e6],
        metavar=("LAMBDA_EXPL", "LAMBDA_CLASS"),
        help=(
            "Prefactores de las pérdidas (λ_expl, λ_class). "
            "Escalan respectivamente la pérdida sobre el mapa de calor y "
            "la pérdida sobre la salida del modelo."
        ),
    )
    parser.add_argument(
        "--method",
        choices=[
            "lrp",
            "guided_backprop",
            "gradient",
            "integrated_grad",
            "pattern_attribution",
            "grad_times_input",
        ],
        default="lrp",
        help="Método de explicabilidad a emplear para generar los mapas de calor",
    )
    parser.add_argument(
        "--no_guardar",
        action="store_true",
        help="Si se indica, no se guardan ni la imagen adversaria ni el fichero de resultados",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Selección de dispositivo y método de explicabilidad
    device = torch.device("cuda" if args.cuda and torch.cuda.is_available() else "cpu")
    method = getattr(ExplainingMethod, args.method)

    # Valor de β a utilizar cuando se activa beta_growth
    if args.beta_growth:
        if args.beta_value is None:
            raise ValueError(
                "Debe proporcionar --beta_value cuando use la opción --beta_growth."
            )
        beta_value = float(args.beta_value)
    else:
        beta_value = None  # indicará uso de ReLU (sin softplus)

    # Modelo base (VGG16) y red explicable
    data_mean = np.array([0.485, 0.456, 0.406])
    data_std = np.array([0.229, 0.224, 0.225])

    vgg_model = torchvision.models.vgg16(pretrained=True)
    model = ExplainableNet(
        vgg_model,
        data_mean=data_mean,
        data_std=data_std,
        beta=beta_value if args.beta_growth else None,
    )

    if method == ExplainingMethod.pattern_attribution:
        state = torch.load("../models/model_vgg16_pattern_small.pth", map_location=device)
        model.load_state_dict(state, strict=False)

    model = model.eval().to(device)

    # Cargar imagen original y clonar para construir la imagen adversaria
    x = load_image(data_mean, data_std, device, args.img)
    x_adv = x.clone().detach().requires_grad_()

    # Mapas de calor original y objetivo (texto sobre la misma imagen)
    org_expl, org_acc, org_idx = get_expl(model, x, method)
    org_expl = org_expl.detach().cpu()

    # El mapa objetivo se obtiene aplicando get_expl_with_text sobre la misma imagen
    target_expl, _, _ = get_expl_with_text(model, x, method, intensity=0.4)
    target_expl = target_expl.detach()

    # Optimizador sobre la imagen adversaria
    optimizer = torch.optim.Adam([x_adv], lr=args.lr)

    # Bucle principal de optimización del ataque
    for i in range(args.num_iter):
        if args.beta_growth:
            # Si se quisiera crecimiento de β, se podría usar get_beta(i, args.num_iter)
            # model.change_beta(get_beta(i, args.num_iter))
            model.change_beta(beta_value)

        optimizer.zero_grad()

        # Explicación y salida de la red para la imagen adversaria
        adv_expl, adv_acc, class_idx = get_expl(
            model, x_adv, method, desired_index=org_idx
        )

        # Pérdida de explicabilidad: queremos que el mapa adversario se parezca al objetivo
        loss_expl = F.mse_loss(adv_expl, target_expl)

        # Pérdida de clasificación: queremos mantener la salida original
        loss_output = F.mse_loss(adv_acc, org_acc.detach())

        # Combinación ponderada de ambas pérdidas
        total_loss = args.prefactors[0] * loss_expl + args.prefactors[1] * loss_output

        # Paso de optimización
        total_loss.backward()
        optimizer.step()

        # Proyección al espacio de imágenes válidas (clamp con media y desviación)
        x_adv.data = clamp(x_adv.data, data_mean, data_std)

        print(
            f"Iter {i:4d} | "
            f"Total: {total_loss.item():.4e} | "
            f"Expl: {loss_expl.item():.4e} | "
            f"Output: {loss_output.item():.4e}"
        )

    # Preparar guardado de resultados
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = make_dir(args.output_dir)

    # Pasar todo a CPU para visualización y guardado
    target_expl = target_expl.cpu()
    org_expl = org_expl.cpu()
    adv_expl = adv_expl.cpu()
    x = x.cpu()
    x_adv = x_adv.cpu()

    # Figura resumen: imagen original, mapa objetivo y mapa adversario
    overview_name = (
        f"{output_dir}overview_{args.method}_{args.img.replace('/', '_')}"
        f"_beta={beta_value}_{fecha}.png"
    )
    plot_overview(
        [x, x, x_adv],
        [target_expl, org_expl, adv_expl],
        data_mean,
        data_std,
        filename=overview_name,
    )
    print(f"Figura de overview guardada en: {overview_name}")

    if not args.no_guardar:
        # Desnormalizar imagen adversaria y guardarla como JPEG
        img = x_adv.squeeze(0).detach()
        img = img * torch.tensor(data_std)[:, None, None] + torch.tensor(
            data_mean
        )[:, None, None]
        img = torch.clamp(img, 0.0, 1.0)

        img_np = img.permute(1, 2, 0).numpy()
        img_np = np.clip(img_np, 0.0, 1.0)

        to_pil = T.ToPILImage()
        pil_img = to_pil(torch.from_numpy(img_np.transpose(2, 0, 1)))

        img_name = (
            f"x_{args.method}_{args.num_iter}_beta={beta_value}_{fecha}.jpg"
        )
        pil_img.save(img_name, format="JPEG")
        print(f"Imagen adversaria guardada en: {img_name}")

        # Guardar fichero de texto con predicciones y métricas
        results_name = f"resultados_{fecha}.txt"

        with open(results_name, "w", encoding="utf-8") as f_log:
            # Etiquetas de ImageNet
            with open("imagenet_classes.txt", encoding="utf-8") as f:
                imagenet_labels = [line.strip() for line in f]

            f_log.write("=== PREDICCIONES ===\n")
            f_log.write(
                f"Predicción original: {org_idx} -> {imagenet_labels[org_idx]}\n"
            )
            f_log.write(
                f"Predicción adversaria: {class_idx} -> {imagenet_labels[class_idx]}\n\n"
            )

            print(
                "Predicción original:",
                org_idx,
                "->",
                imagenet_labels[org_idx],
            )
            print(
                "Predicción adversaria:",
                class_idx,
                "->",
                imagenet_labels[class_idx],
            )

            mse = torch.mean((x_adv - x) ** 2)
            mae = torch.mean(torch.abs(x_adv - x))

            f_log.write("=== MÉTRICAS ===\n")
            f_log.write(f"MSE: {mse.item():.6f}\n")
            f_log.write(f"MAE: {mae.item():.6f}\n")

            print("MSE:", mse.item(), "MAE:", mae.item())
            print(f"Resultados guardados en: {results_name}")


if __name__ == "__main__":
    main()