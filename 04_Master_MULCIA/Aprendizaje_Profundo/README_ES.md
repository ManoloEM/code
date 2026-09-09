## 📚 Aprendizaje Profundo

Notebooks desarrollados durante la asignatura de Aprendizaje Profundo del Máster MULCIA (Universidad de Sevilla). Los ejercicios cubren clasificación con CNNs, regularización, transfer learning y meta-aprendizaje sobre los conjuntos de datos CIFAR-10 y FER-2013.

| Notebook | Descripción |
|---|---|
| [Clasificando CIFAR10 con redes convolucionalesV2.ipynb](./Clasificando%20CIFAR10%20con%20redes%20convolucionalesV2.ipynb) | Diseño e implementación de una CNN desde cero para clasificación de las 10 clases de CIFAR-10. Se exploran distintas arquitecturas, funciones de activación y estrategias de entrenamiento. |
| [Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb](./Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb) | Análisis del fenómeno de sobreajuste (*overfitting*) en CNNs sobre CIFAR-10. Se estudia el impacto de la capacidad del modelo y se aplican técnicas básicas de regularización para mitigarlo. |
| [Regulizarización_avanzada_ManuelEncisoMartinez.ipynb](./Regulizarización_avanzada_ManuelEncisoMartinez.ipynb) | Exploración de técnicas avanzadas de regularización (Dropout, L1/L2, Batch Normalization, Data Augmentation) para mejorar la generalización de redes profundas sobre CIFAR-10. |
| [Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb](./Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb) | Clasificación de expresiones faciales (dataset FER-2013) mediante CNNs y transfer learning. Se comparan modelos entrenados desde cero con arquitecturas preentrenadas fine-tuneadas. |
| [Aprendiendo_Pocos_Datos_Manuel_Enciso_Martinez.ipynb](./Aprendiendo_Pocos_Datos_Manuel_Enciso_Martinez.ipynb) | Implementación del algoritmo **Reptile** (meta-aprendizaje) para clasificación *few-shot* (N-way K-shot) sobre CIFAR-10. Se analiza la mejora de precisión al escalar el número de iteraciones de meta-entrenamiento y el número de ejemplos por clase. |

**Stack:** `TensorFlow 2`, `Keras`, `NumPy`, `matplotlib`, `Google Colab (GPU T4)`
