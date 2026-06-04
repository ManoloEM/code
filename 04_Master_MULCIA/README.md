# 🎓04 - Máster Universitario Lógica, Computación e Inteligencia Artificial - Universidad de Sevilla

> Universidad de Sevilla · ETSII 

---

## Descripción general

Trabajos, prácticas y proyectos realizados durante el Máster Universitario en Lógica, Computación e Inteligencia Artificial (MULCIA) en la Universidad de Sevilla. El máster cubre áreas avanzadas de inteligencia artificial, aprendizaje automático profundo, sistemas expertos y explicabilidad de modelos.

---

## Contenido

### 📁 TFM — Robustez de métodos de explicabilidad frente a ataques adversarios

Estudio sobre la **manipulación de explicaciones XAI en redes neuronales profundas** y el análisis de la **robustez de los métodos de explicabilidad basados en el gradiente** frente a ataques adversarios. El trabajo se basa en el artículo de Pan Kessel *"Explanations can be manipulated and geometry is to blame"* (arXiv:1906.07983) y extiende sus experimentos para estudiar cómo el parámetro de suavizado β influye en la efectividad y resistencia de los ataques.

#### Objetivo

Demostrar que, manteniendo la predicción de la red neuronal, es posible alterar arbitrariamente el mapa de calor de la explicación asociada, y cuantificar en qué medida un valor de β elevado actúa como mecanismo de defensa frente a dicha manipulación.

#### Contenido de la carpeta

| Archivo / Carpeta | Descripción |
|---|---|
| `codigo/run_attack-beta.py` | Ataque adversario con β fijo sobre una imagen. Genera mapa de calor objetivo con texto superpuesto y optimiza la imagen adversaria. |
| `codigo/run_attack-multiples-betas.py` | Barrido sistemático de β: evalúa explicaciones adversaria y original para una lista de valores de β y genera una rejilla comparativa. |
| `codigo/ssim_compare.py` | Comparación cuantitativa original vs. adversaria mediante índice SSIM. Genera figura de 4 paneles con diferencia RGB y mapa SSIM por píxel. |
| `codigo/utils_modificado.py` | Utilidades adaptadas del repo original: `plot_overview`, `plot_overview_grid`, `load_image`, `get_expl_with_text`. |
| `imagenes/` | Figuras generadas en los experimentos (gradientes, barridos de β, comparaciones SSIM). |

#### Resultados preliminares

<p align="center">
  <img src="TFM/imagenes/Ataque_adversario_beta20.jpg" width="45%" alt="Ataque adversario β=20.0"/>
  &nbsp;&nbsp;
  <img src="TFM/imagenes/Ataque_adversario_beta1.jpg" width="45%" alt="Ataque adversario β=1.0"/>
</p>
<p align="center"><em>Izquierda: ataque con β = 20.0 — el texto "Universidad De Sevilla" es claramente visible en la explicación adversaria. &nbsp;|&nbsp; Derecha: ataque con β = 1.0 — el texto apenas se percibe, lo que indica mayor robustez a valores bajos de β.</em></p>

<p align="center">
  <img src="TFM/imagenes/Suavizado_explicacion_b=20.png" width="40%" alt="Barrido β, ataque b=20"/>
  &nbsp;&nbsp;
  <img src="TFM/imagenes/Suavizado_explicacion_b=1.jpg" width="40%" alt="Barrido β, ataque b=1"/>
</p>
<p align="center"><em>Barrido de β para imagen adversaria fija. Izquierda: ataque con β = 20.0. Derecha: ataque con β = 1.0. Cada fila corresponde a un valor de β evaluado; las columnas muestran imagen adversaria, explicación adversaria y explicación original.</em></p>

> [!TIP]
> Para una descripción completa de los scripts, instrucciones de instalación y reproducción de experimentos, consulta el [`README.md` de la carpeta TFM](./TFM/README.md).

#### Referencia

> Pan Kessel & Stellan Johannink. *"Explanations can be manipulated and geometry is to blame."* arXiv:1906.07983 (2019).
> Repositorio original: [github.com/pankessel/adv_explanation_ref](https://github.com/pankessel/adv_explanation_ref)

### 📁 Aprendizaje Automático

Cuestionarios y prácticas de la asignatura **Aprendizaje Automático**, desarrollados en Python con scikit-learn sobre conjuntos de datos reales.

| Archivo | Tema | Dataset | Descripción |
|---|---|---|---|
| `C2_Enciso_Martinez.ipynb` | Clustering y Árboles de Decisión | Higher Education Students Performance Evaluation (UCI) | Implementación de K-Means, clustering jerárquico y árboles de decisión. Análisis comparativo de modelos. |
| `C4_Enciso_Martinez.ipynb` | Redes Neuronales (MLP) | Thyroid Differentiated Cancer Recurrence (UCI) | Clasificación de recurrencia de cáncer de tiroides mediante perceptrones multicapa (`MLPClassifier`). Preprocesado con `OrdinalEncoder`, análisis de correlación y comparativa de configuraciones de red. |
| `C5_Enciso_Martinez.ipynb` | Aprendizaje no supervisado | - | Aplicación modelos perceptrón multicapa en aprendizaje semisupervisado o no supervisado mediante clustering |

**Stack:** Python, scikit-learn, pandas, NumPy, Matplotlib, Jupyter Notebook.

---

### 📁 Aprendizaje Profundo

Prácticas de la asignatura **Aprendizaje Profundo**, centradas en redes neuronales convolucionales, clasificación de imágenes y técnicas de regularización.

| Archivo                                                           | Tema                                             | Dataset                                    | Descripción                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clasificando CIFAR10 con redes convolucionalesV2.ipynb            | Redes Neuronales Convolucionales (CNN)           | CIFAR-10 (60.000 imágenes, 10 clases)      | Diseño y entrenamiento de una CNN desde cero para clasificación de imágenes. Se exploran distintas configuraciones de capas convolucionales, pooling y activaciones. Análisis de curvas de entrenamiento y evaluación sobre el conjunto de test.             |
| Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb          | Sobreajuste (Overfitting)                        | CIFAR-10                                   | Estudio del fenómeno de sobreajuste en redes profundas entrenadas sobre CIFAR-10. Se inducen escenarios de overfitting deliberado y se analizan métricas de train vs. validation loss para identificar el problema. Base para el notebook de regularización. |
| Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb | Clasificación multiclase — Visión por Computador | FER-2013 / Dataset de expresiones faciales | Red neuronal convolucional para el reconocimiento de expresiones faciales (alegría, tristeza, enfado, sorpresa, etc.). Incluye preprocesado de imágenes en escala de grises, data augmentation y evaluación por clase mediante matriz de confusión.          |
| Regulizarización_avanzada_ManuelEncisoMartinez.ipynb              | Regularización avanzada                          | CIFAR-10                                   | Aplicación sistemática de técnicas de regularización para combatir el sobreajuste detectado en el notebook anterior: Dropout, L1/L2 weight decay, Batch Normalization y Data Augmentation. Comparativa de resultados entre modelos con y sin regularización. |

**Stack:** Python, TensorFlow, Keras, NumPy, Matplotlib, Jupyter Notebook.

---
### 📁 TrabajoFinalSVRAI — Monte Carlo Tree Search con Incertidumbre (Python)

Implementación y comparativa de dos variantes del algoritmo **MCTS** para la asignatura **Sistemas de Razonamiento Automático e Inteligencia Artificial**. Basado en el artículo *"The Second Type of Uncertainty in Monte Carlo Tree Search"*.

| Aspecto | Detalle |
|---|---|
| **Lenguaje** | Python (Jupyter Notebook) |
| **Problema** | Toma de decisiones bajo incertidumbre en árboles asimétricos dirigidos |
| **Algoritmos** | MCTS clásico (UCB) y MCTS-T (UCB con factor de profundidad desconocida) |
| **Estructuras** | `ArbolBinario`, `ArbolNario`, `ArbolNarioHijos` |
| **Visualización** | Representación interactiva por iteración mediante slider (`ipywidgets`) |
| **Fases MCTS** | Selección, Expansión, Simulación (rollout), Retropropagación |

**Stack:** Python · NumPy · NetworkX · Matplotlib · ipywidgets.

---


### 📁 TrabajoICManuelEncisoMartinez — Puzzle Deslizante (CLIPS)

Sistema experto implementado en **CLIPS** para la asignatura **Ingeniería del Conocimiento**. Resuelve un puzzle deslizante 4×4 con piezas fijas, letras especiales (A, B) y un hueco libre.

| Aspecto | Detalle |
|---|---|
| **Lenguaje** | CLIPS (sistema de producción basado en reglas) |
| **Problema** | Puzzle deslizante 4×4 — ordenar piezas numéricas (1–11) en espiral exterior respetando casillas fijas (X) y buffers de letras (A, B) |
| **Modos** | Manual (input de usuario) y Automático (resolución guiada por reglas) |
| **Módulos** | `MAIN`, `DIBUJAR`, `VALIDACION`, `JUEGO` |
| **Estrategia automática** | Rotación del anillo exterior, uso de buffers (2,3)/(3,2) para letras, secuencia especial para piezas 10 y 11 |

**Stack:** CLIPS 6.x.


## Stack tecnológico

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat&logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![CLIPS](https://img.shields.io/badge/CLIPS-Sistemas%20Expertos-darkgreen?style=flat)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white)

---

## Notas

- El TFM está se encuentra en proceso. Tratando sobre la robustez de técnicas de explicabilidad ante diversos ataques adversarios, manteniendo la clasificación de redes neuronales (artículo de referencia:	arXiv:1906.07983).

