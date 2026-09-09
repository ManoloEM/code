## 🧠 Advanced Seminar in Machine Learning

Notebooks developed for the Advanced Seminar in Machine Learning of the MULCIA Master's programme (2025–2026 academic year). The assignments cover Transformer architectures, pretrained language models, and advanced explainability techniques (XAI).

[🇪🇸 Read the Spanish version](README_ES.md)

| Notebook | Topic | Description |
|---|---|---|
| [Modelo_Transformer.ipynb](./Modelo_Transformer.ipynb) | **Transformer implementation** | Construction of a causal Transformer as a custom Keras layer for **text generation** in Spanish. It is trained on two corpora: rap lyrics (Kaggle) and cooking recipes (HuggingFace), implementing token and positional embedding layers from scratch. |
| [Modelo_BERT.ipynb](./Modelo_BERT.ipynb) | **BERT classifier** | Fine-tuning of a **pretrained BERT** model for a text classification task. The deliverable documents the full process: data collection, model adaptation, training, evaluation, and reflection on the difficulties encountered. |
| [Tecnicas_Explicabilidad.ipynb](./Tecnicas_Explicabilidad.ipynb) | **Advanced XAI techniques** | Study and application of explanation methods for neural networks. Includes **Guided Integrated Gradients** (an adaptive path compared to classic IG) and other gradient-based attribution techniques, with visual examples on images. |

**Stack:** `TensorFlow`, `Keras`, `HuggingFace Transformers`, `NumPy`, `matplotlib`, `Google Colab`
