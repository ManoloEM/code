## 📚 Deep Learning

Notebooks developed for the Deep Learning course of the MULCIA Master's programme (University of Seville). The exercises cover CNN classification, regularization, transfer learning, and meta-learning on the CIFAR-10 and FER-2013 datasets.

[🇪🇸 Read the Spanish version](README_ES.md)

| Notebook | Description |
|---|---|
| [Clasificando CIFAR10 con redes convolucionalesV2.ipynb](./Clasificando%20CIFAR10%20con%20redes%20convolucionalesV2.ipynb) | Design and implementation of a CNN from scratch for classifying the 10 CIFAR-10 classes. Different architectures, activation functions, and training strategies are explored. |
| [Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb](./Ejercicio_CIFAR10_Sobreajuste_ManuelEncisoMartinez.ipynb) | Analysis of the overfitting phenomenon in CNNs on CIFAR-10. The impact of model capacity is studied and basic regularization techniques are applied to mitigate it. |
| [Regulizarización_avanzada_ManuelEncisoMartinez.ipynb](./Regulizarización_avanzada_ManuelEncisoMartinez.ipynb) | Exploration of advanced regularization techniques (Dropout, L1/L2, Batch Normalization, Data Augmentation) to improve the generalization of deep networks on CIFAR-10. |
| [Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb](./Reconocimiento_de_expresiones_faciales_ManuelEncisoMartinez.ipynb) | Facial expression classification (FER-2013 dataset) using CNNs and transfer learning. Models trained from scratch are compared with fine-tuned pretrained architectures. |
| [Aprendiendo_Pocos_Datos_Manuel_Enciso_Martinez.ipynb](./Aprendiendo_Pocos_Datos_Manuel_Enciso_Martinez.ipynb) | Implementation of the **Reptile** algorithm (meta-learning) for few-shot classification (N-way K-shot) on CIFAR-10. Accuracy improvements are analyzed as the number of meta-training iterations and the number of examples per class increase. |

**Stack:** `TensorFlow 2`, `Keras`, `NumPy`, `matplotlib`, `Google Colab (GPU T4)`
