## 🔧 Artificial Intelligence and Data Science

[🇪🇸 Read the Spanish version](README_ES.md)

#### 🔧 `Metodos_IA.py`

Implementation from scratch of the following algorithms and techniques:

- **Logistic Regression** with mini-batch training and learning-rate decay
- **Multiclass classification** using the One-vs-Rest (OvR) strategy
- **One-hot encoding** of categorical variables
- **Exhaustive hyperparameter search** on standard datasets: US congressional votes, cancer diagnosis, and IMDB

#### 📊 `Proyecto_Annealing.ipynb`

Complete pipeline applied to the *Steel Plates Faults* dataset (UCI):

1. **Disambiguation of compacted `NaN` values**: distinction between true missing values and *Not applicable* categories using decision trees and one-hot encoding
2. **Iterative imputation** of residual missing values with `IterativeImputer` + `BayesianRidge`
3. **Final preprocessing**: normalization with `StandardScaler` and stratified train/validation/test split
4. **Training of baseline models**: Random Forest, Logistic Regression, and Multilayer Perceptron with a weighted voting system (*soft voting*)
5. **Feature relevance** through permutation importance — the attributes `ohesurface-qualitynan` and `hardness` are the most influential
6. **Dimensionality reduction** with PCA at different explained-variance thresholds (50%–95%)
7. **Stacking and hyperparameter search** to obtain the best-performing predictive model

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
