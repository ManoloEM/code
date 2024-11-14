# -*- coding: utf-8 -*-

from numpy import *
from numpy.linalg import *
from numpy import abs, sum, max, min
from algoritmos import *

# Ejercicio 1.
print("\n Ejercicio 1.")
A = 2*eye(20)-eye(20, k=1)-eye(20, k=-1)
print("A = ", A)

# Ejercicio 2.
print("\n Ejercicio 2.")
A = array([[1, 2], [3, 4]])
print("A = ", A)
B = vstack([hstack([A, 2*A]), hstack([3*A, 4*A])])
print("[[A,2A],[3A,4A]] = ", B)
C = vstack([hstack([A, eye(2), zeros((2, 2))]),
            hstack([eye(2), A, eye(2)]), hstack([zeros((2, 2)), eye(2), A])])
print("[[A,I,0],[I,A,I],[0,I,A]] = ", C)

# Ejercicio 3.
print("\n Ejercicio 3.")
A = reshape(arange(0, 100, 1), (10, 10))
print("A = ", A)
print("Permutación de las filas 3 y 6:")
A[[2, 5], :] = A[[5, 2], :]
print("A = ", A)
print("Permutación de las columnas 3 y 6:")
A[:, [2, 5]] = A[:, [5, 2]]
print("A = ", A)

# Ejercicio 4.
print("\n Ejercicio 4.")
A = reshape(arange(0, 100, 1), (10, 10))
print("A = ", A)
for k in range(10):
    print("Submatriz principal de orden: ", k+1)
    print(A[:k+1, :k+1])

# Ejercicio 5.
print("\n Ejercicio 5.")
A = reshape(arange(0, 100, 1), (10, 10))
print("A = ", A)
print("Eliminación de la fila 3.")
B = delete(A, 2, axis=0)
print(B)
print("Eliminación de la columna 5.")
C = delete(B, 4, axis=1)
print(C)

# Ejercicio 6.
print("\n Ejercicio 6.")
A = array([[1+1j, -2+2j, 3-3j], [4+4j, -5+5j, 6-6j]])
print("A = ", A)
print("Matriz conjugada.")
print("conjugada(A) = ", conjugada(A))

# Ejercicio 7.
print("\n Ejercicio 7.")
A = array([[1+1j, -2+2j, 3-3j], [4+4j, -5+5j, 6-6j]])
print("A = ", A)
print("Traza.")
print("traza(A) = ", traza(A))

# Ejercicio 8.
print("\n Ejercicio 8.")
x = array([7, -8, 9])
X = array([[7., -8., 9e0]])
Y = array([[7j], [-8j], [9j]])
print("Normas vectoriales.")
print("x = ", x, "\nX = ", X, "\nY = ", Y)
print("Norma inf (propio): ", norma_vec(x, inf), norma_vec(X, inf),
      norma_vec(Y, inf))
print("Norma inf (Python): ", norm(x, inf))
print("Norma 1 (propio): ", norma_vec(x, 1), norma_vec(X, 1), norma_vec(Y, 1))
print("Norma 1 (Python): ", norm(x, 1))
print("Norma 2 (propio): ", norma_vec(x, 2), norma_vec(X, 2), norma_vec(Y, 2))
print("Norma 2 (Python): ", norm(x, 2))
print("Norma 10 (propio): ", norma_vec(x, 10), norma_vec(X, 10),
      norma_vec(Y, 10))
print("Norma 10 (Python): ", norm(x, 10))
print("Norma 95/7 (propio): ", norma_vec(x, 95/7), norma_vec(X, 95/7),
      norma_vec(Y, 95/7))
print("Norma 95/7 (Python): ", norm(x, 95/7))
print("Norma 128.4 (propio): ", norma_vec(x, 128.4), norma_vec(X, 128.4),
      norma_vec(Y, 128.4))
print("Norma 128.4 (Python): ", norm(x, 128.4))
print("Norma -3 (propio): ", norma_vec(x, -3), norma_vec(X, -3),
      norma_vec(Y, -3))
print("Norma -3 (Python): ", norm(x, -3))

# Ejercicio 9.
print("\n Ejercicio 9.")
print("Convergencia de las normas vectoriales.")
X = array([[1], [2], [3]])
conv_norma_vec(X)
X = array([[1e10], [2e10], [3e10]])
conv_norma_vec(X)
X = array([[1e-10], [2e-10], [3e-10]])
conv_norma_vec(X)
X = array([[1e100], [2e100], [3e100]])
conv_norma_vec(X)
X = array([[1e-100], [2e-100], [3e-100]])
conv_norma_vec(X)
X = array([[0], [0], [0]])
conv_norma_vec(X)
