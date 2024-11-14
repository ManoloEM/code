#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:23:15 2023

@author: bini
"""

# R E P A S A R frontera rk45 solo hace falta el de orden 4 porque el 5 es para estimar error

from pylab import *
from time import perf_counter


def fun(t,x):
    f1 = x[1]
    f2 = -(al)*x[0]-(be)*x[1]
    return(array([f1,f2]))


'EJERCICIO_1'
# datos
a = 0
b = 20
x0 = array([1,0])
N = 200

'a)'

#datos
al = 10
be = 1

def AB4s(a,b,fun, N,y0):
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
        y[:,k+1] = y[:,k]+h/24*(55*f[:,k] - 59*f[:,k-1] + 37*f[:,k-2] - 9*f[:,k-3])
        t[k+1] = t[k] + h
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t,y)


(t,x) = AB4s(a,b,fun, N,x0)

figure('Ejercicio 1, a)')
subplot(311)
title('Funcion x')
#Para obtener x tan solo hace falta despejarla de la ecuacion luego:
plot(t,(-(x[1]+be*x[0])/al))
subplot(312)
plot(t,x[0])
title('Funcion y')
subplot(313)
plot((-(x[1]+be*x[0])/al),x[0])
title('Plano de fases')





figure('Estabilidad absoluta, a)')
rho = array([1., -1., 0., 0., 0.]) # primero
sigma = array([0., 55., -59., 37., -9.])/24. # segundo
theta = arange(0, 2.*pi, 0.01)
numer = polyval(rho, exp(theta*1j)) # rho(e^{theta*i})
denom = polyval(sigma, exp(theta*1j)) # sigma(e^{theta*i})
mu = numer/denom
x = real(mu)
y = imag(mu)

plot(x, y)
grid(True)
axis('equal')

mA = array([[0,1],[-al,-be]])
print('Para la matriz:\n',mA)
(aut1,aut2)=eig(mA)[0]
print('Se tienen los autovalores',(aut1,aut2))
h = 20/N
plot(h*real(aut1),h*imag(aut1),'+')
plot(h*real(aut2),h*imag(aut2),'+')


'b)'
#datos
al = 15
be = 3


(t,x) = AB4s(a,b,fun, N,x0)

figure('Ejercicio 1, b)')
subplot(311)
title('Funcion x')
#Para obtener x tan solo hace falta despejarla de la ecuacion luego:
plot(t,(-(x[1]+be*x[0])/al))
subplot(312)
plot(t,x[0])
title('Funcion y')
subplot(313)
plot((-(x[1]+be*x[0])/al),x[0])
title('Plano de fases')



figure('Estabilidad absoluta, b)')
rho = array([1., -1., 0., 0., 0.]) # primero
sigma = array([0., 55., -59., 37., -9.])/24. # segundo
theta = arange(0, 2.*pi, 0.01)
numer = polyval(rho, exp(theta*1j)) # rho(e^{theta*i})
denom = polyval(sigma, exp(theta*1j)) # sigma(e^{theta*i})
mu = numer/denom
x = real(mu)
y = imag(mu)

plot(x, y)
grid(True)
axis('equal')

mB = array([[0,1],[-al,-be]])
print('Para la matriz:\n',mA)
(aut1,aut2)=eig(mB)[0]
print('Se tienen los autovalores',(aut1,aut2))
h = 20/N
plot(h*real(aut1),h*imag(aut1),'+')
plot(h*real(aut2),h*imag(aut2),'+')

# en el b) se observa que los puntos estan fuera para el h elegido, luego por eso el comportamiento es mucho peor

'EJERCICIO_2'

def AM4pfs(a,b,fun ,N,y0): #punto fijo
    tol = 1e-12 #tolerancia punto fijo
    lmax = 200 #maximas iteraciones
    y = zeros([len(y0),N+1])
    t = zeros(N+1)
    f = zeros([len(y0),N+1])
    t[0] = a
    h = (b-a)/float(N) 
    y[:,0] = y0
    f[:,0] = fun(a,y0)  
    l = ones(N+1)   
    for k in range(3): #Calculamos las 2 condicones inciales con RK4
        k1 = fun(t[k],y[:,k])
        k2 = fun(t[k]+h/2,y[:,k]+h/2*k1)
        k3 = fun(t[k]+h/2,y[:,k]+h/2*k2)
        k4 = fun(t[k]+h,y[:,k]+h*k3)
        y[:,k+1] = y[:,k] +h/6*(k1+2*k2+2*k3+k4)
        t[k+1] = t[k]+h
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    for k in range(3,N):
        Ck = y[:,k]+ h/720*(646*f[:,k]-264*f[:,k-1]+106*f[:,k-2]-19*f[:,k-3])
        t[k+1] = t[k] + h
        zold = y[:,k]+h/24*(55*f[:,k] - 59*f[:,k-1] + 37*f[:,k-2] - 9*f[:,k-3])
        znew = h*251/720*fun(t[k+1],zold)+Ck
        while(l[k]<200  and max(abs(znew-zold))>=tol):
            zold = znew
            znew = h*251/720*fun(t[k+1],zold)+Ck
            l[k] +=1
        if l[k]==lmax:
            print('El numero maximo de iteraciones ',lmax,' ha sido alcanzado.')
        y[:,k+1] = znew
        f[:,k+1] = fun(t[k+1], y[:,k+1])
    return (t,y,max(l))     




'a)'

#datos
al = 10
be = 1



(t,x,l) = AM4pfs(a,b,fun, N,x0)

figure('Ejercicio 2, a)')
subplot(311)
title('Funcion x')
#Para obtener x tan solo hace falta despejarla de la ecuacion luego:
plot(t,(-(x[1]+be*x[0])/al))
subplot(312)
plot(t,x[0])
title('Funcion y')
subplot(313)
plot((-(x[1]+be*x[0])/al),x[0])
title('Plano de fases 2a')





figure('Estabilidad absoluta, 2a)')
rho = array([1, -1, 0, 0, 0])
sigma = array([251, 646, -264, 106,-19])/720
theta = arange(0, 2.*pi, 0.01)
numer = polyval(rho, exp(theta*1j)) # rho(e^{theta*i})
denom = polyval(sigma, exp(theta*1j)) # sigma(e^{theta*i})
mu = numer/denom
x = real(mu)
y = imag(mu)

plot(x, y)
grid(True)
axis('equal')

mA = array([[0,1],[-al,-be]])
print('Para la matriz:\n',mA)
(aut1,aut2)=eig(mA)[0]
print('Se tienen los autovalores',(aut1,aut2))
h = 20/N
plot(h*real(aut1),h*imag(aut1),'+')
plot(h*real(aut2),h*imag(aut2),'+')


'b)'
#datos
al = 15
be = 3


(t,x,l) = AM4pfs(a,b,fun, N,x0)

figure('Ejercicio 2, b)')
subplot(311)
title('Funcion x')
#Para obtener x tan solo hace falta despejarla de la ecuacion luego:
plot(t,(-(x[1]+be*x[0])/al))
subplot(312)
plot(t,x[0])
title('Funcion y')
subplot(313)
plot((-(x[1]+be*x[0])/al),x[0])
title('Plano de fases')


rho = array([1, -1, 0, 0, 0])
sigma = array([251, 646, -264, 106,-19])/720

figure('Estabilidad absoluta, 2b)')
rho = array([1, -1, 0, 0, 0])
sigma = array([251, 646, -264, 106,-19])/720
theta = arange(0, 2.*pi, 0.01)
numer = polyval(rho, exp(theta*1j)) # rho(e^{theta*i})
denom = polyval(sigma, exp(theta*1j)) # sigma(e^{theta*i})
mu = numer/denom
x = real(mu)
y = imag(mu)

plot(x, y)
grid(True)
axis('equal')

mB = array([[0,1],[-al,-be]])
print('Para la matriz:\n',mA)
(aut1,aut2)=eig(mB)[0]
print('Se tienen los autovalores',(aut1,aut2))
h = 20/N
plot(h*real(aut1),h*imag(aut1),'+')
plot(h*real(aut2),h*imag(aut2),'+')





