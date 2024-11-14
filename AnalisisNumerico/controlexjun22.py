#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:14:06 2023

@author: bini
"""

from pylab import *
from time import perf_counter


'EJERCICIO_3'

def fun(t,y):
    f1 = y[1]
    f2 = -4*y[1]-29*y[0]
    return(array([f1,f2]))
    
def exacta(t):
    return(exp(-2*t)*cos(5*t))

#datos
y0= array([1,-2]) #(y,y')
a =0
b = 5
N = 200


def ABM2s(a,b,fun ,N,y0): 
    tol = 1e-12
    lmax = 200
    itermax = 0
    y = zeros([len(y0),N+1])
    t = zeros(N+1)
    f = zeros([len(y0),N+1])
    t[0] = a
    h = (b-a)/float(N) 
    y[:,0] = y0
    f[:,0] = fun(a,y0)    
    for k in range(1): #Calculamos las 1 condicones incial con HEUN
        y[:,k+1] = y[:,k] +h/2*(fun(t[k],y[:,k])+fun(t[k]+h,y[:,k]+h*fun(t[k],y[:,k])))
        t[k+1] = t[k]+h
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    for k in range(1,N):
        t[k+1] = t[k] + h
        yold = y[:,k]
        ynew = 4/3*y[:,k]-1/3*y[:,k-1]+2/3*h*f[:,k]
        fkacum = fun(t[k+1],yold)
        l = 1
        while(l<lmax  and max(abs(ynew-yold))>=tol):
            yold = ynew
            ynew = 4/3*y[:,k]-1/3*y[:,k-1]+2/3*h*f[:,k]
            l +=1
        if l==lmax:
            print('El numero maximo de iteraciones ',lmax,' ha sido alcanzado.')
        y[:,k+1] = ynew
        f[:,k+1] = fun(t[k+1], y[:,k+1])
        itermax = max(l,itermax)
    return (t,y,itermax) 


tini = perf_counter()
(t,y,itermax)  = ABM2s(a,b,fun ,N,y0)
tfin = perf_counter()

ye = exacta(t)
error = max(abs(ye-y[0]))
print('·)El error cometido es de:', error)
print('·)Tiempo de CPU de calculo:',tfin-tini)
print('·)Numero maximo de iteraciones:',itermax)

figure('Eje.3.')
subplot(211)
plot(t,y[0])
title('Estimacion')
subplot(212)
plot(t,ye)
title('Exacta')




'EJERCICIO_4'


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


def dRK(z):
    return(9/(3-z)**2)

figure('Region RK')
locfronRK(dRK, 2)






