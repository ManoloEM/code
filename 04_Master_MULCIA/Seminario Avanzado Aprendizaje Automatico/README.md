## 🧠 Seminario Avanzado de Aprendizaje Automático

Notebooks desarrollados en el Seminario Avanzado de Aprendizaje Automático del Máster MULCIA (curso 2025–2026). Los trabajos abordan las arquitecturas Transformer, modelos de lenguaje preentrenados y técnicas de explicabilidad avanzada (XAI).

| Notebook | Tema | Descripción |
|---|---|---|
| [Modelo_Transformer.ipynb](./Modelo_Transformer.ipynb) | **Implementación de Transformer** | Construcción de un Transformer causal como capa personalizada de Keras para **generación de texto** en castellano. Se entrena sobre dos corpus: letras de rap (Kaggle) y recetas de cocina (HuggingFace), implementando capas de embedding de token y posición desde cero. |
| [Modelo_BERT.ipynb](./Modelo_BERT.ipynb) | **Clasificador con BERT** | Fine-tuning de un modelo **BERT preentrenado** para una tarea de clasificación de texto. El entregable documenta todo el proceso: búsqueda de datos, adaptación del modelo, entrenamiento, evaluación y reflexión sobre las dificultades encontradas. |
| [Tecnicas_Explicabilidad.ipynb](./Tecnicas_Explicabilidad.ipynb) | **Técnicas XAI avanzadas** | Estudio y aplicación de métodos de explicabilidad sobre redes neuronales. Incluye **Guided Integrated Gradients** (camino adaptativo frente al IG clásico) y otras técnicas de atribución basadas en gradientes, con ejemplos visuales sobre imágenes. |

**Stack:** `TensorFlow`, `Keras`, `HuggingFace Transformers`, `NumPy`, `matplotlib`, `Google Colab`
