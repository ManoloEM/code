[🇪🇸 Read the Spanish version](README_ES.md)

# 🌍 02 — Erasmus · University of Coimbra (2023–2024)

Repository of projects and practices developed during the Erasmus+ mobility period
at the **Faculty of Sciences and Technology of the University of Coimbra**.
The work was carried out in Portuguese or English, sometimes in collaboration with colleagues.

---

## 📁 Content

### `As-proyecto.Rmd`
**Course:** Sampling and Surveying
**Language:** R
**Collaboration:** Sara Aguado

Statistical analysis project that compares two domain estimators on a real dataset of student academic performance (Kaggle). The mean estimator in a subdomain (women) is studied under two scenarios: with and without knowledge of the population size of the domain N₀.

The work includes:
- Calculation of the true value of the target parameter
- Extraction of a simple random sample without replacement (SSR)
- Point and variance estimation for both estimators
- Construction of 95% confidence intervals
- Simulation of 100 repetitions to calculate coverage probabilities
- Graphical comparison of estimators and their variances using boxplots

**Main conclusion:** Both estimators converge in bias, but differ in variance.
The estimator with known N₀ presents a higher estimated variance, a result that is analyzed
in detail in the attached PDF document.

---

### `ProyectoONMatLab.m`
**Course:** Numerical Optimization
**Language:** MATLAB

Function approximation project using single-hidden-layer neural networks,
modeled as linear combinations of ReLU activation functions (φ(x) = max(x, 0)).
Given a set of observations O and a validation set T, the quadratic error between the target function f and the approximation g is minimized.

The work covers the following experiments:

| Exercise | Description |
|-----------|-------------|
| Ex. 2–3   | Approximation of f(x)=(x−1)² with m=2 and m=10 neurons; quasi-Newton method (`fminunc`) |
| Ex. 4.A   | Comparison with the Nelder-Mead method (`fminsearch`) for m=2 |
| Ex. 4.B   | Increase in observation data (n=20) and neurons (m=7); improvement analysis |
| Ex. 4.C   | Data with random perturbation (uniform noise); model robustness |
| Ex. 4.D   | Generalization to different functions: x³, x(x−1)(x−2), ((x−1)²−1)², eˣ, sin(x) |

Each experiment records the optimal parameters (a, b), the value of the objective function,
the number of iterations and evaluations, and generates superimposed visualizations of f(x) and g(x).

---

### 📂 `modelizacion/`
Folder corresponding to the **Mathematical Modeling** course.
Contains practical and applied mathematical model construction and analysis projects.

---

### 📂 `BaseDeDatos/`
**Course:** Databases
**Language:** SQL
**Collaboration:** Juan Rodriguez

Project to create a website linked to a database for collecting movie reviews.

---

## Technological stack

![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=sqlite&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-e16737?style=flat&logo=mathworks&logoColor=white)

---

## 🏫 Institution

**University of Coimbra** — Faculty of Sciences and Technology
**Erasmus+** Program · Academic year 2023–2024
