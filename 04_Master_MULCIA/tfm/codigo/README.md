## 💻 TFM — Código

Scripts desarrollados para el Trabajo Fin de Máster *"Robustez de métodos de explicabilidad frente a ataques adversarios"*, basados y adaptados del repositorio original [adv_explanation_ref](https://github.com/pankessel/adv_explanation_ref) (Pan Kessel).

| Archivo | Descripción |
|---|---|
| [`run_attack-beta.py`](./run_attack-beta.py) | Genera un ataque adversario sobre el mapa de explicación de una imagen con un **valor fijo de β**. Optimiza una imagen adversaria cuya explicación replica un mapa objetivo (texto "Universidad De Sevilla") sin alterar la predicción de la red. Guarda la imagen adversaria, la figura de overview y un fichero de métricas (MSE, MAE). |
| [`run_attack-multiples-betas.py`](./run_attack-multiples-betas.py) | Extiende el ataque anterior para estudiar la **robustez variando β sistemáticamente**. Tras generar la imagen adversaria con un β inicial, evalúa las explicaciones adversaria y original para una lista de valores de β y genera una figura en rejilla (fila por valor de β). |
| [`ssim_compare.py`](./ssim_compare.py) | Calcula y visualiza el **índice SSIM** entre la imagen original y la adversaria. Genera una figura de 4 paneles: imagen original, imagen adversaria, diferencia RGB amplificada y mapa SSIM por píxel, con el valor global en el título. |
| [`utils-modificado.py`](./utils-modificado.py) | Módulo de utilidades adaptado del repositorio original. Incluye funciones de visualización (`plot_overview`, `plot_overview_grid`), carga de imágenes con preprocesado ImageNet (`load_image`) y generación de explicaciones con texto superpuesto (`get_expl_with_text`). |

**Stack:** `PyTorch`, `torchvision`, `pytorch-msssim`, `scikit-image`, `NumPy`, `matplotlib`, `Pillow`
