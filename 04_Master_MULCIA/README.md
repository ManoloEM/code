# 🎓04 - Master's Degree in Logic, Computation and Artificial Intelligence - University of Seville

> University of Seville · ETSII

---

## Overview

Work, practical assignments, and projects completed during the Master's Degree in Logic, Computation and Artificial Intelligence (MULCIA) at the University of Seville. The programme covers advanced areas of artificial intelligence, deep machine learning, expert systems, and model explainability.

[🇪🇸 Read the Spanish version](README_ES.md)

---

## Contents

### 📁 Master's Thesis — Robustness of Explanation Methods Against Adversarial Attacks

A study on the **manipulation of XAI explanations in deep neural networks** and the analysis of the **robustness of gradient-based explanation methods** against adversarial attacks. This work is based on Pan Kessel's article *"Explanations can be manipulated and geometry is to blame"* (arXiv:1906.07983) and extends its experiments to study how the smoothing parameter β affects the effectiveness and resistance of the attacks.

#### Objective

To show that, while keeping the neural network prediction unchanged, it is possible to arbitrarily alter the heatmap of the associated explanation, and to quantify to what extent a high β value acts as a defense mechanism against such manipulation.

#### Folder contents

| File / Folder | Description |
|---|---|
| `codigo/run_attack-beta.py` | Adversarial attack with fixed β on a single image. Generates the target heatmap with overlaid text and optimizes the adversarial image. |
| `codigo/run_attack-multiples-betas.py` | Systematic β sweep: evaluates adversarial and original explanations for a list of β values and generates a comparative grid. |
| `codigo/ssim_compare.py` | Quantitative original vs. adversarial comparison using the SSIM index. Generates a 4-panel figure with RGB difference and pixel-wise SSIM map. |
| `codigo/utils_modificado.py` | Utilities adapted from the original repo: `plot_overview`, `plot_overview_grid`, `load_image`, `get_expl_with_text`. |
| `imagenes/` | Figures generated in the experiments (gradients, β sweeps, SSIM comparisons). |

#### Results

<p align="center">
  <img src="tfm/imagenes/Ataque_adversario_beta20.jpg" width="45%" alt="Adversarial attack β=20.0"/>
  &nbsp;&nbsp;
  <img src="tfm/imagenes/Ataque_adversario_beta1.jpg" width="45%" alt="Adversarial attack β=1.0"/>
</p>
<p align="center"><em>Left: attack on the smoothed network with β = 20.0 using a text mask reading "Universidad De Sevilla". &nbsp;|&nbsp; Right: attack on the smoothed network with β = 1.0 using a text mask reading "Universidad De Sevilla".</em></p>

<p align="center">
  <img src="tfm/imagenes/ssim_comparison_b=20.png" width="45%" alt="Adversarial attack analysis β=20.0"/>
  &nbsp;&nbsp;
  <img src="tfm/imagenes/ssim_comparison_b=1.png" width="45%" alt="Adversarial attack analysis β=1.0"/>
</p>
<p align="center"><em>Left: attack on the smoothed network with β = 20, reduced perturbation magnitude. &nbsp;|&nbsp; Right: attack on the smoothed network with β = 1.0, larger perturbation magnitude but still imperceptible (SSIM > 95%).</em></p>

<p align="center">
  <img src="tfm/imagenes/Suavizado_explicacion_b=20.png" width="40%" alt="β sweep, attack b=20"/>
  &nbsp;&nbsp;
  <img src="tfm/imagenes/Suavizado_explicacion_b=1.jpg" width="40%" alt="β sweep, attack b=1"/>
</p>
<p align="center"><em>β sweep for a fixed adversarial image. Left: attack with β = 20.0. Right: attack with β = 1.0. Each row corresponds to a β value evaluated for the explanation; the columns show the adversarial image, adversarial explanation, and original explanation.</em></p>

> [!TIP]
> For a complete description of the scripts, installation instructions, and reproduction of experiments, see the [`README.md` in the TFM folder](./tfm/README.md).

#### Reference

> Pan Kessel & Stellan Johannink. *"Explanations can be manipulated and geometry is to blame."* arXiv:1906.07983 (2019).
> Original repository: [github.com/pankessel/adv_explanation_ref](https://github.com/pankessel/adv_explanation_ref)

### 📁 Machine Learning

Course exercises and practical assignments for **Machine Learning**, developed in Python with scikit-learn on real datasets.

| File | Topic | Dataset | Description |
|---|---|---|---|
| `C2_Enciso_Martinez.ipynb` | Clustering and Decision Trees | Higher Education Students Performance Evaluation (UCI) | Implementation of K-Means, hierarchical clustering, and decision trees. Comparative model analysis. |
| `C4_Enciso_Martinez.ipynb` | Neural Networks (MLP) | Thyroid Differentiated Cancer Recurrence (UCI) | Classification of thyroid cancer recurrence using multilayer perceptrons (`MLPClassifier`). Preprocessing with `OrdinalEncoder`, correlation analysis, and comparison of network configurations. |
| `C5_Enciso_Martinez.ipynb` | Unsupervised Learning | - | Application of multilayer perceptron models in semi-supervised or unsupervised learning through clustering. |

**Stack:** Python, scikit-learn, pandas, NumPy, Matplotlib, Jupyter Notebook.

---

### 📁 Deep Learning

Practical assignments for **Deep Learning**, focused on convolutional neural networks, image classification, and regularization techniques.

| File | Topic | Dataset | Description |
| ----------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clasificando CIFAR10 con redes convolucionalesV2.ipynb | Convolutional Neural Networks (CNN) | CIFAR-10 (60,000 images, 10 classes) | Design and training of a CNN from scratch for image classification. Different configurations of convolution, pooling, and activation layers are explored. Training curves and test-set evaluation are analyzed. |
| Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb | Overfitting | CIFAR-10 | Study of overfitting in deep networks trained on CIFAR-10. Deliberate overfitting scenarios are induced and train vs. validation loss metrics are analyzed to identify the issue. Basis for the regularization notebook. |
| Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb | Multiclass Classification — Computer Vision | FER-2013 / Facial Expressions Dataset | Convolutional neural network for facial expression recognition (happiness, sadness, anger, surprise, etc.). Includes grayscale image preprocessing, data augmentation, and per-class evaluation using a confusion matrix. |
| Regulizarización_avanzada_ManuelEncisoMartinez.ipynb | Advanced Regularization | CIFAR-10 | Systematic application of regularization techniques to combat the overfitting detected in the previous notebook: Dropout, L1/L2 weight decay, Batch Normalization, and Data Augmentation. Comparison of results between models with and without regularization. |

**Stack:** Python, TensorFlow, Keras, NumPy, Matplotlib, Jupyter Notebook.

---

### 📁 Advanced Seminar in Machine Learning

Assignments for the **Advanced Seminar in Machine Learning**, organized into three independent projects covering explainability, text generation with Transformer models, and classification with BERT.

| Assignment | Topic | Description |
|---|---|---|
| **Assignment 1** — Explainability | Reproduction of XAI techniques | Study and reproduction of explanation methods presented in reference papers. Practical implementation of techniques such as Guided Integrated Gradients, ShapleyCAM, and AdvXAI on trained models, analyzing prediction interpretation and comparing the behavior of each method. |
| **Assignment 2** — Text generation | Transformer model fine-tuning | Training a Transformer model for automatic text generation in two domains: **rap songs** and **cooking recipes**. The model learns the stylistic and structural patterns of each domain from specific datasets, generating text that is coherent and thematically appropriate. |
| **Assignment 3** — Review classification | BERT fine-tuning | Fine-tuning a pre-trained **BERT** model for Amazon review classification on a **1 to 5 star** scale. The task is approached as a multiclass classification problem, including dataset preprocessing, tokenization with the BERT vocabulary, and model evaluation using classification metrics and confusion probabilities. |

**Stack:** Python, PyTorch, Hugging Face Transformers, datasets, scikit-learn, Jupyter Notebook.

---
### 📁 Artificial Intelligence and Data Science

The course *Artificial Intelligence and Data Science* covers the full machine-learning workflow, from data exploration and preprocessing to training and optimizing predictive models. The folder contains two complementary projects.

| File | Description |
|---|---|
| `Metodos_IA.py` | Ground-up implementation of classical machine-learning algorithms |
| `Proyecto_Annealing.ipynb` | Complete preprocessing and modeling pipeline on the *Steel Plates Faults* dataset |

**Stack:** Python, Jupyter, Scikit-Learn, Pandas

---
### 📁 TrabajoFinalSVRAI — Monte Carlo Tree Search with Uncertainty (Python)

Implementation and comparison of two variants of the **MCTS** algorithm for the course **Automatic Reasoning Systems and Artificial Intelligence**. Based on the article *"The Second Type of Uncertainty in Monte Carlo Tree Search"*.

| Aspect | Detail |
|---|---|
| **Language** | Python (Jupyter Notebook) |
| **Problem** | Decision-making under uncertainty in directed asymmetric trees |
| **Algorithms** | Classic MCTS (UCB) and MCTS-T (UCB with unknown depth factor) |
| **Structures** | `ArbolBinario`, `ArbolNario`, `ArbolNarioHijos` |
| **Visualization** | Interactive iteration-by-iteration representation via slider (`ipywidgets`) |
| **MCTS Phases** | Selection, Expansion, Simulation (rollout), Backpropagation |

**Stack:** Python · NumPy · NetworkX · Matplotlib · ipywidgets.

---

### 📁 TrabajoICManuelEncisoMartinez — Sliding Puzzle (CLIPS)

Expert system implemented in **CLIPS** for the course **Knowledge Engineering**. It solves a 4×4 sliding puzzle with fixed pieces, special letters (A, B), and one empty slot.

| Aspect | Detail |
|---|---|
| **Language** | CLIPS (rule-based production system) |
| **Problem** | 4×4 sliding puzzle — arrange numeric pieces (1–11) in the outer spiral while respecting fixed cells (X) and letter buffers (A, B) |
| **Modes** | Manual (user input) and Automatic (rule-guided resolution) |
| **Modules** | `MAIN`, `DIBUJAR`, `VALIDACION`, `JUEGO` |
| **Automatic strategy** | Outer ring rotation, buffer usage (2,3)/(3,2) for letters, special sequence for pieces 10 and 11 |

**Stack:** CLIPS 6.x.

---

## Technology stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat&logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![CLIPS](https://img.shields.io/badge/CLIPS-Sistemas%20Expertos-darkgreen?style=flat)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white)

---
