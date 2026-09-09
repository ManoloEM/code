#### 🔧 Metodos_IA.py

Implementación desde cero de los siguientes algoritmos y técnicas:

- **Regresión Logística** con mini-batch y decaimiento de tasa de aprendizaje
- **Clasificación multiclase** mediante estrategia One-vs-Rest (OvR)
- **Codificación one-hot** de variables categóricas
- **Búsqueda exhaustiva de hiperparámetros** sobre datasets estándar: votos de
  congresistas (US), diagnóstico de cáncer e IMDB

#### 📊 Proyecto_Annealing.ipynb

Pipeline completo aplicado al conjunto *Steel Plates Faults* (UCI):

1. **Desambiguación de valores compactados en `NaN`**: distinción entre verdaderos
   ausentes y categorías *No aplicable* mediante árboles de decisión y codificación one-hot
2. **Imputación iterativa** de nulos residuales con `IterativeImputer` + `BayesianRidge`
3. **Preprocesado final**: normalización con `StandardScaler` y partición estratificada
   en entrenamiento, validación y test
4. **Entrenamiento de modelos base**: Random Forest, Regresión Logística y Perceptrón
   Multicapa con sistema de votación ponderada (*soft voting*)
5. **Relevancia de atributos** mediante importancia por permutación — los atributos
   `ohesurface-qualitynan` y `hardness` resultan los más influyentes
6. **Reducción de dimensionalidad** con PCA a distintos umbrales de varianza explicada
   (50 %–95 %)
7. **Stacking y búsqueda de hiperparámetros** para obtener el modelo predictivo de
   mayor rendimiento


![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
