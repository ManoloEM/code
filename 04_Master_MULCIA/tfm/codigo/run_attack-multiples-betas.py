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
#   - Uso de una única imagen como base y generación del mapa de calor
#     objetivo mediante una versión alterada con texto (get_expl_with_text),
#     en lugar de usar una segunda imagen de destino.
#   - Criterio de parada anticipada del ataque adversario en función de
#     la pérdida de explicabilidad (loss_dif) y del número máximo de
#     iteraciones (num_iter_max).
#   - Estudio sistemático de la robustez de las explicaciones frente a
#     distintos valores de β (lista rango_beta) sobre la misma imagen
#     original y adversaria.
#   - Generación de salidas adicionales: figura comparativa de mapas de
#     calor para varios β, guardado de la imagen adversaria desnormalizada
#     y registro en fichero de texto con predicciones y métricas (MSE, MAE).
# ----------------------------------------------------------------------

"""
Script para generar un ejemplo adversario que manipula el mapa de calor
de una imagen manteniendo la clase predicha, y para analizar la robustez
de las explicaciones frente a distintos valores del parámetro de
suavizado β en la red.

Basado en el script original run_attack.py del repositorio
https://github.com/pankessel/adv_explanation_ref
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
    plot_overview_grid,
    clamp,
    load_image,
    make_dir,
)


def parse_args() -> argparse.Namespace:
    """Parsea los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description=(
            "Genera un ejemplo adversario que altera el mapa de calor de una "
            "imagen y evalúa la robustez de las explicaciones para distintos β."
        )
    )

    parser.add_argument(
        "--num_iter_max",
        type=int,
        default=1500,
        help="Número máximo de iteraciones de optimización del ataque",
    )
    parser.add_argument(
        "--loss_dif",
        type=float,
        default=70.0,
        help="Umbral de pérdida sobre el mapa de calor (MSE) para detener el ataque",
    )
    parser.add_argument(
        "--img",
        type=str,
        default="../data/collie4.jpeg",
        help="Ruta a la imagen de entrada sobre la que se ejecuta el ataque",
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=2e-4,
        help="Tasa de aprendizaje del optimizador Adam",
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
        "--beta_value_range",
        type=float,
        nargs=2,
        metavar=("BETA_MIN", "BETA_MAX"),
        help=(
            "Rango [mínimo, máximo] de β para el análisis de robustez. "
            "Si no se especifica, se usa el conjunto por defecto [20, 10, 5, 1, 0.9, 0.8]."
        ),
    )
    parser.add_argument(
        "--split_step",
        type=int,
        default=2,
        help=(
            "Número de valores intermedios de β a muestrear entre BETA_MIN y BETA_MAX "
            "cuando se usa --beta_value_range."
        ),
    )
    parser.add_argument(
        "--prefactors",
        nargs=2,
        type=float,
        default=[1e11, 1e6],
        metavar=("LAMBDA_EXPL", "LAMBDA_CLASS"),
        help=(
            "Prefactores de las pérdidas: (λ_expl, λ_class). "
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
        help="Si se indica, no se guarda la imagen adversaria ni el fichero de resultados",
    )

    return parser.parse_args()


def build_beta_range(args: argparse.Namespace) -> np.ndarray:
    """
    Construye el rango de valores de β a considerar en el análisis de robustez.

    Si el usuario proporciona --beta_value_range y --split_step, se genera una
    rejilla uniforme entre ambos extremos. En caso contrario, se usa un
    conjunto fijo de valores representativos.
    """
    if args.beta_value_range is not None:
        beta_min, beta_max = args.beta_value_range
        if args.split_step <= 1:
            return np.array([beta_min, beta_max], dtype=float)
        return np.linspace(beta_min, beta_max, args.split_step, dtype=float)

    # Conjunto por defecto usado en los experimentos del TFM
    return np.array([20.0, 10.0, 5.0, 1.0, 0.9, 0.8], dtype=float)


def main() -> None:
    args = parse_args()

    # Dispositivo y método de explicabilidad
    device = torch.device("cuda" if args.cuda and torch.cuda.is_available() else "cpu")
    method = getattr(ExplainingMethod, args.method)

    # Rango de valores de β y valor inicial para el ataque
    beta_range = build_beta_range(args)
    beta_attack = float(beta_range[0])
    print(f"Usando β inicial para el ataque: {beta_attack}")

    # Modelo base (VGG16) y red explicable con activaciones softplus(β)
    data_mean = np.array([0.485, 0.456, 0.406])
    data_std = np.array([0.229, 0.224, 0.225])

    vgg_model = torchvision.models.vgg16(pretrained=True)
    model = ExplainableNet(
        vgg_model,
        data_mean=data_mean,
        data_std=data_std,
        beta=beta_attack,
    )

    if method == ExplainingMethod.pattern_attribution:
        state = torch.load("../models/model_vgg16_pattern_small.pth", map_location=device)
        model.load_state_dict(state, strict=False)

    model = model.eval().to(device)

    # Cargar imagen original y clonar para construir la imagen adversaria
    x = load_image(data_mean, data_std, device, args.img)
    x_adv = x.clone().detach().requires_grad_()

    # Mapa de calor original y mapa objetivo (alterado con texto)
    org_expl, org_acc, org_idx = get_expl(model, x, method)
    org_expl = org_expl.detach().cpu()

    # get_expl_with_text genera un mapa de calor objetivo manipulando la misma imagen
    target_expl, _, _ = get_expl_with_text(model, x, method, intensity=0.8)
    target_expl = target_expl.detach()

    # Optimizador sobre la imagen adversaria
    optimizer = torch.optim.Adam([x_adv], lr=args.lr)

    # Bucle de optimización con parada anticipada
    current_expl_loss = float("inf")
    num_iter = 0

    while current_expl_loss > args.loss_dif and num_iter < args.num_iter_max:
        num_iter += 1
        optimizer.zero_grad()

        # Explicación adversaria y salida de la red para la imagen perturbada
        adv_expl, adv_acc, class_idx = get_expl(
            model, x_adv, method, desired_index=org_idx
        )

        # Pérdida sobre el mapa de calor (queremos que se parezca al objetivo)
        loss_expl = F.mse_loss(adv_expl, target_expl)

        # Pérdida sobre la salida (queremos mantener la clasificación original)
        loss_output = F.mse_loss(adv_acc, org_acc.detach())

        # Combinación ponderada de ambas pérdidas
        total_loss = args.prefactors[0] * loss_expl + args.prefactors[1] * loss_output

        current_expl_loss = loss_expl.item()

        # Paso de optimización
        total_loss.backward()
        optimizer.step()

        # Proyectar la imagen adversaria al espacio de imágenes válidas
        x_adv.data = clamp(x_adv.data, data_mean, data_std)

        if num_iter % 10 == 0 or num_iter == 1:
            print(
                f"[Iter {num_iter:4d}] "
                f"Total: {total_loss.item():.4e} | "
                f"Expl: {loss_expl.item():.4e} | "
                f"Output: {loss_output.item():.4e}"
            )

    # Análisis de robustez: evaluar explicaciones para distintos β
    adv_expl_list = []
    org_expl_list = []

    for beta in beta_range:
        model.change_beta(float(beta))
        adv_expl_beta, _, _ = get_expl(model, x_adv, method)
        org_expl_beta, _, _ = get_expl(model, x, method)
        adv_expl_list.append(adv_expl_beta)
        org_expl_list.append(org_expl_beta)

    # Directorio de salida y marca temporal
    output_dir = make_dir(args.output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Asegurarse de que todo está en CPU para el guardado/visualización
    target_expl = target_expl.cpu()
    org_expl = org_expl.cpu()
    x = x.cpu()
    x_adv = x_adv.cpu()

    # Figura comparativa de mapas de calor para todos los β del rango
    plot_filename = (
        f"{output_dir}"
        f"overview_Beta_proof_{args.method}_"
        f"{args.img.replace('/', '_')}_"
        f"beta={beta_range[0]}_{beta_range[-1]}_{timestamp}.png"
    )
    plot_overview_grid(
        [x_adv for _ in range(len(beta_range))],
        adv_expl_list,
        org_expl_list,
        data_mean,
        data_std,
        beta_range,
        filename=plot_filename,
    )
    print(f"Figura de comparación de mapas de calor guardada en: {plot_filename}")

    if not args.no_guardar:
        # Guardar imagen adversaria desnormalizada como PNG
        to_pil = T.ToPILImage()

        img = x_adv.squeeze(0).detach().cpu()
        img = img * torch.tensor(data_std)[:, None, None] + torch.tensor(
            data_mean
        )[:, None, None]
        img = torch.clamp(img, 0.0, 1.0)

        adv_img_name = (
            f"x_adv_{args.method}_{args.num_iter_max}_"
            f"beta={beta_attack}_{timestamp}.png"
        )

        pil_img = to_pil(img)
        pil_img.save(adv_img_name, format="PNG")
        print(f"Imagen adversaria guardada en: {adv_img_name}")

        # Guardar fichero de texto con predicciones y métricas
        results_name = f"resultados_beta={beta_attack}_{timestamp}.txt"

        with open(results_name, "w", encoding="utf-8") as f_log:
            # Leer etiquetas de ImageNet
            with open("imagenet_classes.txt", encoding="utf-8") as f_classes:
                imagenet_labels = [line.strip() for line in f_classes]

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
            f_log.write(f"Beta ataque: {beta_attack:.6f}\n")
            f_log.write(f"Iteraciones: {num_iter}\n")
            f_log.write(
                f"Pérdida de explicabilidad final (MSE): {current_expl_loss:.11f}\n"
            )

        print("MSE:", mse.item(), "MAE:", mae.item())
        print(f"Resultados guardados en: {results_name}")


if __name__ == "__main__":
    main()