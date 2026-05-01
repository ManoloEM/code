# 🌍 02 — Erasmus · Universidade de Coimbra (2023–2024)

Repositorio de proyectos y prácticas desarrollados durante el periodo de movilidad Erasmus+
en la **Facultade de Ciências e Tecnologia da Universidade de Coimbra**.
Los trabajos se realizaron en portugués o ingles, en ocasiones en colaboración con compañeros.

---

## 📁 Contenido

### `As-proyecto.Rmd`
**Asignatura:** Amostragem e Sondagem (Muestreo y Sondeo)
**Lenguaje:** R 
**Colaboración:** Sara Aguado

Proyecto de análisis estadístico que compara dos estimadores de dominio sobre un conjunto de
datos real de rendimiento académico de estudiantes (Kaggle). Se estudia el estimador de la
media en un subdominio (mujeres) bajo dos escenarios: con y sin conocimiento del tamaño
poblacional del dominio N₀.

El trabajo incluye:
- Cálculo del valor real del parámetro objetivo
- Extracción de una muestra aleatoria simple sin reemplazamiento (SSR)
- Estimación puntual y de varianza para ambos estimadores
- Construcción de intervalos de confianza al 95%
- Simulación de 100 repeticiones para calcular probabilidades de cobertura
- Comparación gráfica de estimadores y sus varianzas mediante boxplots

**Conclusión principal:** Ambos estimadores convergen en sesgo, pero difieren en varianza.
El estimador con N₀ conocido presenta mayor varianza estimada, resultado que se analiza
en detalle en el documento PDF adjunto.

---

### `ProyectoONMatLab.m`
**Asignatura:** Otimização Numérica (Optimización Numérica)
**Lenguaje:** MATLAB

Proyecto de aproximación de funciones mediante redes neuronales de una capa oculta,
modeladas como combinaciones lineales de funciones de activación ReLU (φ(x) = max(x, 0)).
Dado un conjunto de observaciones O y un conjunto de validación T, se minimiza el error
cuadrático entre la función objetivo f y la aproximación g.

El trabajo cubre los siguientes experimentos:

| Ejercicio | Descripción |
|-----------|-------------|
| Ej. 2–3   | Aproximación de f(x)=(x−1)² con m=2 y m=10 neuronas; método quasi-Newton (`fminunc`) |
| Ej. 4.A   | Comparación con el método Nelder-Mead (`fminsearch`) para m=2 |
| Ej. 4.B   | Aumento de datos de observación (n=20) y neuronas (m=7); análisis de mejora |
| Ej. 4.C   | Datos con perturbación aleatoria (ruido uniforme); robustez del modelo |
| Ej. 4.D   | Generalización a distintas funciones: x³, x(x−1)(x−2), ((x−1)²−1)², eˣ, sin(x) |

Cada experimento registra los parámetros óptimos (a, b), el valor de la función objetivo,
el número de iteraciones y evaluaciones, y genera visualizaciones superpuestas de f(x) y g(x).

---

### 📂 `modelizacion/`
Carpeta correspondiente a la asignatura de **Modelización Matemática**.
Contiene prácticas y proyectos de construcción y análisis de modelos matemáticos aplicados.

---

### 📂 `BaseDeDatos/`
**Asignatura:** Base de Datos
**Lenguaje:** SQL
**Colaboración:** Juan Rodriguez

Proyecto de realizar una pagina web enlazada con una base de datos para la recolección de reseñas de cine.

---

## Stack tecnológico

![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=sqlite&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-e16737?style=flat&logo=mathworks&logoColor=white)

---

## 🏫 Institución

**Universidade de Coimbra** — Facultade de Ciências e Tecnologia
Programa **Erasmus+** · Curso académico 2023–2024
