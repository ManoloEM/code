# -*- coding: utf-8 -*-

from numpy import *
from numpy.linalg import *
from numpy import abs, sum, max, min

# Tipos de variables.
i = 4
r1 = 5.
r2 = 6e0
c = 4+3j
print("Entero: ", i, " de tipo ", type(i))
print("Real: ", float(i), " de tipo ", type(float(i)))
print("Real: ", r1, " de tipo ", type(r1))
print("Real: ", r2, " de tipo ", type(r2))
print("Complejo: ", complex(i), " de tipo ", type(complex(i)))
print("Complejo: ", complex(r1), " de tipo ", type(complex(r1)))
print("Complejo: ", complex(r2), " de tipo ", type(complex(r2)))
print("Complejo: ", c, " de tipo ", type(c))

# Funciones de variable compleja.
# z = complex(input("Introduce un número complejo (no nulo): "))
z = 4+3j
x = real(z)
y = imag(z)
modulo = abs(z)
argumento = angle(z)
conjugado = conj(z)
print("\n El número complejo ", z, " tiene parte real ", x,
      ", parte imaginaria ", y, ", módulo ", modulo, ", argumento ",
      argumento, " radianes, su conjugado es ", conjugado, ", su opuesto es ",
      -z, " y su inverso es ", z**(-1), ".")
print("\n Su exponencial vale ", exp(z), ".")

# Construcción de matrices.
A = array([[1, -2, 3], [-4, 5, -6]])
x = array([7., -8, 9])
X = array([[7., -8, 9]])
Y = array([[1j], [-2]])

print("\n Impresión de las matrices.")
print("A = ", A, "\nx = ", x)
print("X = ", X, "\nY = ", Y)

print("\n Tipo de las matrices.")
print("type(A) = ", type(A), "\ntype(x) = ", type(x))
print("type(X) = ", type(X), "\ntype(Y) = ", type(Y))

print("\n Número de dimensiones de las matrices.")
print("ndim(A) = ", ndim(A), "\nndim(x) = ", ndim(x))
print("ndim(X) = ", ndim(X), "\nndim(Y) = ", ndim(Y))
print(A.ndim, x.ndim, X.ndim, Y.ndim)

print("\n Tamaño de las matrices.")
print("shape(A) = ", shape(A), "\nshape(x) = ", shape(x))
print("shape(X) = ", shape(X), "\nshape(Y) = ", shape(Y))
print(A.shape, x.shape, X.shape, Y.shape)

print("\n Número de elementos de las matrices.")
print("size(A) = ", size(A), "\nsize(x) = ", size(x))
print("size(X) = ", size(X), "\nsize(Y) = ", size(Y))
print(A.size, x.size, X.size, Y.size)

# Tipo de los elementos de las matrices.
print("\n Tipo de los elementos de las matrices.")
print("A.dtype = ", A.dtype, "\nx.dtype = ", x.dtype)
print("X.dtype = ", X.dtype, "\nY.dtype = ", Y.dtype)

print("\n Matriz de tipo predefinido.")
B = array([[1, 2], [3, 4]], dtype=float)
print("B = ", B, "\nB.dtype = ", B.dtype)

# Matrices especiales.
print("\n Matrices especiales.")
print("\n Matriz de 0's.")
C = zeros((3, 2))
print("C = ", C, "\nC.dtype = ", C.dtype)
print("\n Matriz de 1's.")
D = ones((2, 3))
print("D = ", D, "\nD.dtype = ", D.dtype)
print("\n Matriz aleatoria.")
E = random.rand(3, 2)
print("E = ", E, "\nE.dtype = ", E.dtype)
print("\n Matriz de diagonal principal de 1's.")
F = eye(2, 3)
print("F = ", F, "\nF.dtype = ", F.dtype)
print("\n Matriz de k-diagonal principal de 1's.")
G = eye(3, k=1)
print("G = ", G, "\nG.dtype = ", G.dtype)

print("\n Matriz creada por interpolación.")
H = reshape(arange(0, 12, 1), (3, 4))
print("H = ", H, "\nH.dtype = ", H.dtype)
print("\n Matriz creada por interpolación.")
K = reshape(linspace(0, 11, 12), (4, 3))
print("K = ", K, "\nK.dtype = ", K.dtype)

# Acceso a los elementos de las matrices.
print("\n Acceso a los elementos de las matrices.")
print("A[0, 0] = ", A[0, 0])
print("x[1] = ", x[1])
print("X[0, 1] = ", X[0, 1])
print("Y[1, 0] = ", Y[1, 0])
print("A[1, :] = ", A[1, :])
print("A[1:, :] = ", A[1:, :])
print("A[:, 1] = ", A[:, 1])
print("A[:, 1:2] = ", A[:, 1:2])
print("A[:1, 1:] = ", A[:1, 1:])
print("A[:, ::2] = ", A[:, ::2])

# Transposición y conjugación.
print("\n Transposición y conjugación.")
print("Transpuesta-vector: transpose(x) = ", transpose(x))
print("Transpuesta: transpose(A) = ", transpose(A))
print("Conjugada: conjugate(transpose(X)) = ", conjugate(transpose(X)))
print("Conjugada: conjugate(transpose(Y)) = ", conjugate(transpose(Y)))

# Operaciones elementales.
print("\n Operaciones elementales.")
print("Suma: A+D = ", A+D)
print("Suma constante: 3+A = ", 3+A)
print("Suma vector: x+A = ", x+A)
print("Suma matriz fila: X+A = ", X+A)
print("Suma matriz columna: Y+A = ", Y+A)
print("Producto-elemento: A*D = ", A*D)
print("Producto escalares: 3*A = ", 3*A)
print("Producto vector: x*A = ", x*A)
print("Producto matriz fila: X*A = ", X*A)
print("Producto matriz columna: Y*A = ", Y*A)
print("Producto: A@H = ", A@H)
print("Potencia-elemento: A**3 = ", A**3)
print("Potencia: matrix_power(B, 2) = ", matrix_power(B, 2))

# Matrices triangulares.
print("\n Matrices triangulares:")
print("tril(A) = ", tril(A))
print("tril(A, 1) = ", tril(A, 1))
print("tril(A, -1) = ", tril(A, -1))
print("triu(A) = ", triu(A))
print("triu(A, 1) = ", triu(A, 1))
print("triu(A, -1) = ", triu(A, -1))
print("tril(x) = ", tril(x))
print("triu(x) = ", triu(x))

# Funciones usuales.
print("\n Funciones usuales.")
print("abs(A) = ", abs(A))
print("abs(Y) = ", abs(Y))
print("sum(A) = ", sum(A))
print("sum(A, axis=0) = ", sum(A, axis=0))
print("sum(A, axis=1) = ", sum(A, axis=1))
print("max(A) = ", max(A))
print("max(A, axis=0) = ", max(A, axis=0))
print("max(A, axis=1) = ", max(A, axis=1))
print("min(A) = ", min(A))
print("min(A, axis=0) = ", min(A, axis=0))
print("min(A, axis=1) = ", min(A, axis=1))
print("diagflat(x) = ", diagflat(x))
print("diagflat(Y, k=1) = ", diagflat(Y, k=1))
print("diagflat(A, k=-1) = ", diagflat(A, k=-1))
print("diag(A) = ", diag(A))
print("diag(A, k=1) = ", diag(A, k=1))
print("diag(Y) = ", diag(Y))
print("diag(x) = ", diag(x))
print("vstack([A, D]) = ", vstack([A, D]))
print("hstack([A, B]) = ", hstack([A, B]))
