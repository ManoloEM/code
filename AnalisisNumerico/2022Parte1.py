#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:28:19 2023

@author: bini
"""

from pylab import *
from time import perf_counter

"""


(E) y' = -9y

tablero butcher

1/3 / 1/3 0
2/3 / 1/3 1/3
///////////////
///// 1/2 1/2

1)y^1k = yk +h/3f/tk,yk)
2)y^2k = yk + ....
yk+1 = yk + h/2[f(t^1k,y^2k)+f(t^2k,y^2k)]



para(E) queda tal que:
    
1) y^1k= yk -h3y^1k
    despejamos cuanto es y^1k y queda tal que y^1k = yk/(1+3h)
2) 'sustituir igual'
yk+1 queda en terminos ya expresados anteriormente




"""


# EJERCICIO 1
 # APARTADO A)

print("[]   EJERCICIO 1   []\n")

def f1a(y): #no hace falta pasar el parametro t ya que es autonoma
    return(-9*y)

def RK(h,y): # no hace falta pasar el parametro t ya que f1a es autonoma, luego no calculamos t^i (ahorrar calculos)
    y1 = y/(1+3*h)
    y2 = (y-(3*h*y)/(1+3*h))/(1+3*h)
    return(y+1/2*h*(f1a(y1)+f1a(y2)))

 # APARTADO B)

#datos
a1 = 0
b1 = 2
y01 = 1 
listN = [10,20,40,80,160]


def exacta1(t):
    return(exp(-9*t))

def ejer1b():
    errores = zeros(5) #vamos a guardar los errores para estimar orden
    print('Calculamos los errores cometidos:')
    for i in listN:
        h = (b1 - a1) / i
        t = zeros(i+1)
        y = zeros(i+1)
        t[0] = a1
        y[0] = y01
        for k in range(i):
            y[k+1] = RK(h,y[k])
            t[k+1] = t[k]+h
        ye = exacta1(t)
        error = max(abs(y-ye))
        print('Error con particion ',i,' es de', error)
        errores[listN.index(i)] = error
    print('Aumentando por 2 las particiones, el error se divide en:\nCaso 10/20     ',errores[0]/errores[1],' \nCaso 20/40     ',errores[1]/errores[2],'\nCaso 40/80     ',errores[2]/errores[3],'\nCaso 80/160     ',errores[3]/errores[4])
    print('Luego el orden estimado es de 2, ya que al aumentar el intervalo por 2 se divide en 2^2 que es 4')
    return()
            
ejer1b()            


def dibuja1(): #Dibuja el metodo met con partinciones ListaN y exacta
    # Dibujamos las soluciones de cada paso de malla
    for i in listN:
        h = (b1 - a1) / i
        t = zeros(i+1)
        y = zeros(i+1)
        t[0] = a1
        y[0] = y01
        figure('Gracficas ejer1')
        for k in range(i):
            y[k+1] = RK(h,y[k])
            t[k+1] = t[k]+h
        plot(t,y, '-*') # dibuja la solucion aproximada ('-' es unir los puntos '*')
    t = linspace(a1,b1,max(listN))
    ye = exacta1(t)
    plot(t,ye,'k')
    grid(True) #, 20, 40, 80, 160
    legend(['PasoMalla 10','PasoMalla 20','PasoMalla 40','PasoMalla 80','PasoMalla 160', 'Exacta'])

    # Calculo del error cometido
    show() # muestra la grafica
    return()
    

dibuja1()


# EJERCICIO 2
 # APARTADO A)

print("[]   EJERCICIO 2   []\n")


def f2(t,y):
    fu1 = y[1]
    fu2 = 2*(y[0]-t)*(y[1]-1)
    return(array([fu1,fu2]))

def exacta2(t):
    return(tan(t)+t)

# datos iniciales
tol2 = 10**(-5)
h02 = 2 * 10**(-4)
y02 = array([0,2])
a2 = 0
b2 = 1.3

def rk45sis(a, b, fun, y0, h0, tol):
    """Implementacion del metodo encajado RK4(5)
    en el intervalo [a, b] con condicion inicial y0,
    paso inicial h0 y tolerancia tol"""
    

    hmin = 1.e-5 # paso de malla minimo
    hmax = 0.1 # paso de malla maximo

    
    # coeficientes RK
    q = 6 # orden del metodo mas uno
    A = zeros([q, q])
    A[1, 0] = 1./4.
    A[2, 0] = 3/32.
    A[2, 1] = 9/32.
    A[3,0] =1932/2197.
    A[3,1] = -7200/2197.
    A[3,2] = 7296/ 2197.
    A[4,0] = 439/216.
    A[4,1] = -8.
    A[4,2] = 3680/513.
    A[4,3] = -845/4104.
    A[5,0] = -8/27.
    A[5,1] = 2
    A[5,2] = -3544/2565.
    A[5,3] = 1859/4104.
    A[5,4] = -11/40.
    
    B = zeros(q)
    B[0] = 25/216.
    B[2] = 1408/2565. 
    B[3] = 2197/4104.
    B[4] = -1/5.
    
    BB = zeros(q)
    BB[0] = 16./135.
    BB[2] = 6656./12825.
    BB[3] = 28561./56430.
    BB[4] = -9/50.
    BB[5] = 2/55.
    
    C = zeros(q)
    for i in range(q):
        C[i] = sum(A[i,:])
    
    # inicializacion de variables
    t = array([a]) # nodos
    y = zeros([len(y0),1]) # cada nueva aproximacion sera una columna que añadamos
    y[:,0] = y0 # soluciones
#   tambien se podria y = y0.reshape(len(y0),1)
    h = array([h0]) # pasos de malla
    K = zeros([len(y0),q])
    k = 0 # contador de iteraciones
    
    while (t[k] < b):
        h[k] = min(h[k], b-t[k]) # ajuste del ultimo paso de malla
        for i in range(q):
            K[:,i] = fun(t[k]+C[i]*h[k], y[:,k]+h[k]*dot(A[i,:],transpose(K)))
        incrlow = dot(B, transpose(K)) # metodo de orden 2
        incrhigh = dot(BB, transpose(K)) # metodo de orden 3 
#       incrhigh/incrlow son vectores
        error = max(abs(h[k]*(incrhigh-incrlow))) # estimacion del error
#       para sistemas, el estimador del error se toma con norma infinito
        y = column_stack((y, y[:,k] + h[k]*incrlow))
        t = append(t, t[k]+h[k]); # t_(k+1)
        hnew = 0.9*h[k]*abs(tol/error)**(1./5) # h_(k+1)
        hnew = min(max(hnew,hmin),hmax) # hmin <= h_(k+1) <= hmax
        h = append(h, hnew)
        k += 1
    

    return (t, y, h)



tini = perf_counter()
(t,y,h) = rk45sis(a2, b2, f2, y02, h02, tol2)
tfin = perf_counter()

error = max(abs(y[0,:]-exacta2(t)))
print('·) Error cometido ', error)
print('·) Tiempo de procesamineto', tfin-tini)
print('·) Paso maximo',max(h[:-2]),' y paso minimo',min(h[:-2])) #quitamos los dos ultimos
print('·) Numero total de pasos', len(h))
figure('Gracficas ejer2')
subplot(211) # para dibujar en una misma ventana grafica una fila y dos columnas (dos graficas)
plot(t, y[0,:]) # dibuja la solucion aproximada
plot(t, exacta2(t)) # dibuja la solucion 
xlabel('t')
ylabel('y')
legend(['Aproximacion', 'Exacta'])
subplot(212)
plot(t,h)
xlabel('t')
ylabel('h')
legend(['Pasos'])

show()



