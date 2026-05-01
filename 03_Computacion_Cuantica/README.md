# ⚛️  03 — Computación Cuántica · DIPLOMA DE EXTENSIÓN UNIVERSITARIA Quant·UMA

> Trabajo teórico y práctico sobre computación cuántica: circuitos, algoritmos y simulación con frameworks en Python.

---

## Descripción general

Esta carpeta documenta el trabajo desarrollado durante el periodo de especialización en Computación Cuántica. El contenido abarca los fundamentos matemáticos de la mecánica cuántica aplicados a la computación, el diseño y simulación de circuitos cuánticos, y el estudio de los algoritmos cuánticos más relevantes.

Las simulaciones se ejecutan sobre hardware clásico o cuántico mediante APIs de IBM o DWave.

---

## Contenido

### 📄 CodigoResolvermd-knap
Resolución del problema de la mochila (0/1 Knapsack) mediante optimización cuántica. El problema se formula como QUBO (Quadratic Unconstrained Binary Optimization) y se exploran soluciones mediante técnicas variacionales sobre el simulador cuántico de Qiskit.

### 📄 Entanglement Swapping
Implementación del protocolo de entanglement swapping entre tres agentes: Alice, Bob y Charlie. Se construyen dos pares de Bell (Alice–Bob y Bob–Charlie) y se realiza una medición de Bell en los qubits de Bob para transferir el entrelazamiento al par Alice–Charlie sin interacción directa. Incluye verificación mediante AerSimulator y análisis de resultados por canal clásico.

### 📄 Quantum Error Correction
Estudio e implementación de códigos de corrección de errores cuánticos. Se aplica el código de repetición de 3 qubits para detectar y corregir errores de tipo bit-flip, con análisis del comportamiento bajo canales de ruido y modelos de decoherencia usando Qiskit Aer.

### 📄 Quantum Teleportation
Implementación del protocolo de teleportación cuántica: transmisión del estado desconocido de un qubit de Alice a Bob utilizando un par EPR compartido y dos bits de canal clásico. Se verifica la fidelidad del estado recibido mediante simulación con AerSimulator.

### 📄 QuantumEntanglement
Construcción y simulación del estado de Bell mediante puertas Hadamard y CNOT sobre dos qubits. Incluye medición de ambos registros y visualización del histograma de resultados con AerSimulator.

---

## Stack tecnológico

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=flat&logo=qiskit&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=flat)



## Notas

- Cada notebook es autocontenido e incluye celdas de markdown explicativas.
- Se incluyen derivaciones matemáticas cuando resultan relevantes.

