#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:00:55 2023

@author: bini
"""

from pylab import *
from time import perf_counter


'EJERCICIO_1'


def fun(t,y): # y = (x,c)
    f1 = -(y[0]**3-a*y[0]+y[1])/e
    f2 = y[0]
    return(array([f1,f2]))

#dato
y0 = array([1.7,0.3])
a = 3 #cte de la fun
a1 = 0 #tiempo incial
b1= 30

'a)'
#datos
e=1
N = 150

def RK4sistema(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[:,0] = y0
    for k in range(N):
        k1 = fun(t[k],y[:,k])
        k2 = fun(t[k]+h/2,y[:,k]+h/2*k1)
        k3 = fun(t[k]+h/2,y[:,k]+h/2*k2)
        k4 = fun(t[k]+h,y[:,k]+h*k3)
        y[:,k+1] = y[:,k] +h/6*(k1+2*k2+2*k3+k4)
        t[k+1] = t[k]+h
    return(t,y)

(t,y) = RK4sistema(a1,b1,fun,N,y0)

figure('Eje.1.a)')
subplot(311)
plot(t,y[0])
title('Grafica x')
subplot(312)
plot(t,y[1])
title('Grafica c')
subplot(313)
plot(y[0],y[1])
title('Plano fases')
print('1.a)\n')
print('--------')
print('Para x, el tiempo de periodo de oscilación es aproximadamente de 7t')
print('Para c, el tiempo de periodo de oscilación es aproximadamente de 9t')
print('--------')

'b)'
e = 0.4 
N = 150

(t,y) = RK4sistema(a1,b1,fun,N,y0)

figure('Eje.1.b) para N=150')
subplot(311)
plot(t,y[0])
title('Grafica x')
subplot(312)
plot(t,y[1])
title('Grafica c')
subplot(313)
plot(y[0],y[1])
title('Plano fases')
print('1.b)\n')
print('--------')
print('Para x, el tiempo de periodo de oscilación es aproximadamente de 12t')
print('Para c, el tiempo de periodo de oscilación es aproximadamente de 12t')
print('La grafica no se parece a la del a) y un motivo claro puede ser debido a que el N elegido no es suficiente para la nueva constante e')
print('--------')

e = 0.4 
N = 300

(t,y) = RK4sistema(a1,b1,fun,N,y0)

figure('Eje.1.b) para N=300')
subplot(311)
plot(t,y[0])
title('Grafica x')
subplot(312)
plot(t,y[1])
title('Grafica c')
subplot(313)
plot(y[0],y[1])
title('Plano fases')
print('--------')
print('Para x, el tiempo de periodo de oscilación es aproximadamente de 5t')
print('Para c, el tiempo de periodo de oscilación es aproximadamente de 7t')
print('El latido el corazon sigue una grafica similar que el del a) pero a un ritmo de oscilacion mas rapido')
print('--------')







'EJERCICIO_2'



def fun(t,y):
    return((1-mu*sin(t)*y)*y)

#datos
y0 = 3

'a)'

a2 =0
b2 = 2
N = 20


def euler(a, b, fun, N, y0):
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros(N+1) # inicializacion del vector de resultados
    t[0] = a # nodo inicial
    y[0] = y0 # valor inicial
    # Metodo de Euler
    for k in range(N):
        y[k+1] = y[k]+h*fun(t[k], y[k])
        t[k+1] = t[k]+h
    return (t, y)

figure('Euler.a)')
for j in [1,10,50]:
    mu = j
    (t,y) = euler(a2, b2, fun, N, y0)
    plot(t,y)
    
axis([0,2,-20,20])
legend(('µ = 1','µ = 10','µ = 50'))
print('2.a)\n')
print('--------')
print('Para µ = 1 y µ = 10 el N elegido parece ser suficiente para la converegencia del metodo Euler. En cambio para µ = 50 el N es insuficiente y rapidamente se observe como la grafica diverge')
print('--------')



'b)'


def RK(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        k1 = fun(t[k],y[k]+h*(1/2*k1-1/2*k2))
        k2 = fun(t[k]+h,y[k]+h*(1/2*k1-1/2*k2))
        y[k+1] = y[k] +h*(k1/2+k2/2)
        t[k+1] = t[k]+h
    return(t,y)

















