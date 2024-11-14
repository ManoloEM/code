#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:32:05 2023

@author: bini
"""

from pylab import *
from time import perf_counter

'Ejercicio_2'

#datos
mu = 2
y0 = array([2,0])
a = 0
b = 20

def fun(t,y):
    f1 = y[1]
    f2 = -mu*(y[0]**2-1)*y[1]-y[0]
    return(array([f1,f2]))


def AM1pfs(a,b,fun ,N,y0): #punto fijo
    tol = 1e-12 #tolerancia punto fijo
    lmax = 500 #maximas iteraciones
    y = zeros([len(y0),N+1])
    t = zeros(N+1)
    f = zeros([len(y0),N+1])
    t[0] = a
    h = (b-a)/float(N) 
    y[:,0] = y0
    f[:,0] = fun(a,y0)  
    l = ones(N+1)   
    for k in range(0,N):
        Ck = y[:,k]+ h/2*(f[:,k]) #aquello que NO depende de y[k+1] en f[k+1]
        t[k+1] = t[k] + h
        zold = y[:,k]+h*f[:,k]
        znew = h/2*fun(t[k+1],zold)+Ck
        while(l[k]<lmax  and max(abs(znew-zold))>=tol):
            zold = znew
            znew = h/2*fun(t[k+1],zold)+Ck
            l[k] +=1
        if l[k]==lmax:
            print('El numero maximo de iteraciones ',lmax,' ha sido alcanzado.')
        y[:,k+1] = znew
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t,y,max(l))   

#Si queremos tomar h = 0.1, basta con tomar N = b-a/h
h = 0.1
N = int((b-a)/h)
tini = perf_counter()
(t,y,l) = AM1pfs(a,b,fun ,N,y0)
tfin = perf_counter()
print('Tiempo de cpu:', tfin-tini)
print('Numero maximo de iteraciones:', l)
figure('Ejercicio2')
subplot(211)
plot(t,y[0])
title('Grafica x')
subplot(212)
plot(y[0],y[1])
title('Trayectoria')



'Ejercicio_4'


def fun(t,y):
    f1 = y[1]
    f2 = -6*y[1]-y[0]-2
    return(array([f1,f2]))

A = array([[0,1],[-1,-6]])
B = array([[0],[-2]])

(aut1,aut2) = eig(A)[0]

def locfronRK(dR, N):
# Localizacion de la frontera de un metodo RK
#  Devidada de la funcion R
    Npoints = 5000
    T = 2*N*pi
    h = 2*N*pi/Npoints
    z = zeros(Npoints +1 , dtype = complex)
    z[0] = 0.
    t = 0
    for k in range(len(z)-1):
        z[k+1] = z[k]+ h*1j*exp(1j*t)/dR(z[k])
        t = t + h
    x = real(z)
    y = imag(z)
    plot(x,y)
    grid(True)
    axis('equal')

figure('Region RK4')
def dRK4exp(z):
    return 1. + z + z**2/2 + z**3/6
locfronRK(dRK4exp, 4.)

plot(real(aut1),imag(aut1),'+') #representamos el autovalor 1 por +
plot(real(aut2),imag(aut2),'*') #representamos el autovalor 2 por *

# el que da mayor problemas es el aut2: queremos que h*aut2 > -2,7 => h < 2,7/aut2 (aproximadamente es 0.465)

hcrit = 0.465
plot(real(aut2)*hcrit,0,'x')
print('Como el h critico es '+str(hcrit)+' y por tanto todo h que sea menor tambien servira para la estabilidad del metodo')

ep = 0.1
a = 0
b = 20
y0 = array([ep,0])



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


#h por los valores de A caen fuera
h = 0.55
N = int((b-a)/h)
(t1,y1) = RK4sistema(a,b,fun,N,y0)
#h por los valores de A caen en la frontera dentro
h = 0.468
N = int((b-a)/h)+1
(t2,y2) = RK4sistema(a,b,fun,N,y0)
#h por los valores de A caen dentro de la region
h = 0.4
N = int((b-a)/h)
(t3,y3) = RK4sistema(a,b,fun,N,y0)

figure('Graficas Ue')
plot(t1,y1[0])
plot(t2,y2[0])
plot(t3,y3[0])
legend(('Mala','Critica','Buena'))











