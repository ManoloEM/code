#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:55:41 2023

@author: Manuel Enciso Martínez
"""


from pylab import *
from time import perf_counter


'EJERCICIO_1'

# def fun(t,y): #y = (no contagiado, contagiados)
#     f1 = -y[1]
#     f2 = k*y[0]*y[1]
#     return(array([f1,f2]))

def fun(t,y): #y = (no contagiado, contagiados)
    return(k*(m-y)*y)

'a)'

#datos
m = 100000
#x+y =m entonces podemos expresar x en terminos de y cmo: x=m-y 
y0 = 1000
k = 2e-6
a = 0
b = 60
N =150

def AB3(a,b,fun, N,y0): # adams-bashforht 3 pasos
    y = zeros(N+1)
    t = zeros(N+1)
    f = zeros(N+1)
    t[0] = a
    h = (b-a)/float(N) 
    y[0] = y0
    f[0] = fun(a,y[0])    
    for k in range(2): #Calculamos condicones inciales necesarias con RK4
        k1 = fun(t[k],y[k])
        k2 = fun(t[k]+h/2,y[k]+h/2*k1)
        k3 = fun(t[k]+h/2,y[k]+h/2*k2)
        k4 = fun(t[k]+h,y[k]+h*k3)
        y[k+1] = y[k] +h/6*(k1+2*k2+2*k3+k4)
        t[k+1] = t[k]+h
        f[k+1] = fun(t[k+1], y[k+1])
    for k in range(2,N):
        y[k+1] = y[k]+h/12.0*(23.0*f[k] - 16*f[k-1] + 5*f[k-2])
        t[k+1] = t[k] + h
        f[k+1] = fun(t[k+1], y[k+1])
    return (t,y)


(t,y) = AB3(a,b,fun, N,y0)
figure('Eje.1.a)')
subplot(211)
plot(t,y)
title('Contagiados')
subplot(212)
plot(t,m-y)
title('No contagiados')


'b)'

def fun(t,x): #x = (x,y,z)
    f1 = -k1*x[0]*x[1]-k3*x[0]
    f2 = k1*x[0]*x[1]-k2*x[1]
    f3 = k3*x[0]+k2*x[1]
    return(array([f1,f2,f3]))


k1=2e-6
k2=5e-3
k3=1e-5
y0 =array([m-1000,1000,0])


def AB3s(a,b,fun, N,y0):
    y = zeros([len(y0),N+1])
    t = zeros(N+1)
    f = zeros([len(y0),N+1])
    t[0] = a
    h = (b-a)/float(N) 
    y[:,0] = y0
    f[:,0] = fun(a,y0)    
    for k in range(2): #Calculamos condicones inciales necesarias con RK4
        k1 = fun(t[k],y[:,k])
        k2 = fun(t[k]+0.5*h, y[:,k]+0.5*h*k1)
        k3 = fun(t[k]+0.5*h, y[:,k]+0.5*h*k2)
        k4 = fun(t[k]+h, y[:,k]+h*k3)
        y[:,k+1] = y[:,k] + h*(k1+2*k2+2*k3+k4)/6
        t[k+1] = t[k]+h
        f[:,k+1] = fun(t[k+1],y[:,k+1])
    for k in range(2,N):
        y[:,k+1] = y[:,k]+h/12*(23*f[:,k] - 16*f[:,k-1] + 5*f[:,k-2])
        t[k+1] = t[k] + h
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t,y)


figure('Eje.1.b)')
(t,y) = AB3s(a,b,fun, N,y0)
subplot(311)
plot(t,y[0])
title('No contagiados')
subplot(312)
plot(t,y[1])
title('Contagiados')
subplot(313)
plot(t,y[1])
title('Eliminados')


print('Observamos como una vez llegados al numero maximo de contagiados, tambien se obtiene el numero maximo de personas eliminadas de ser susceptibles a ser contagiadas, ya que el numero de no contagiados esta en minimos')
print('Ademas observamos como el numero maximo de contagiados no llega a los 10000 como en el ejercicio anterior, ya que hay parte de la poblacion que se ha muerto/vuelto inmune y no puede llegar a pertenecer al grupo de contagiados (como si pasaba en el apartado a)')









