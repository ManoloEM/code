#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:09:00 2021

@author: bini
"""
from numpy import *
from matplotlib.pyplot import *
from math import *
import scipy as sp
from scipy.interpolate import interp1d

#EJERCICIO.1

#   (a)

def fNor(x):
    return(x**6-6*x**4+12*x**2-8)

# def fNew(x):
#     return((5*x**6-14*x**4+12*x**2+8)/(6*x**5-20*x**3+24*x))
def fNew(x):
    return(x-((x**6-6*x**4+12*x**2-8)/(6*x**5-24*x**3+24*x)))

def puntofijo(f,x0,eps,nmax):
    niter = 0
    while(niter<nmax):
        if(abs(fNor(x0))<eps):
            return("Hemos llegado a una solucion con una precision de al menos"+str(eps)+", con el valor de x_"+str(niter)+" igual a"+str(x0))
        else:
            niter+=1
            x1=f(x0)
            print("Iteracion nº"+str(niter))
            print("Valor de x_"+str(niter)+" igual a "+str(x1))
            print("Valor de e_"+str(niter)+" igual a "+str(f(x1)))
            print("Valor de e_"+str(niter)+"/e_"+str(niter-1)+" igual a "+str(f(x1)/f(x0)))
            x0=x1
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))


#   (b)

#print(puntofijo(fNew,1.5,10**(-12),500))

def constC(g,p,l):
    return(abs(g(l))/factorial(p)) #Donde g es la derivada p-esima no nula en l

def d1f(x):
    return(6*x**5-24*x**3+24*x)

def d2f(x):
    return(30*x**4-72*x**2+24)

#g2l = -((2*d2f(2**(1/2))*d1f(2**(1/2))-(d1f(2**(1/2)))**2)-2*(d1f(2**(1/2)))**3*d2f(2**(1/2)))/((d1f(2**(1/2)))**3)


#   (c)

def fNew2(x):
    return(x-3*((x**6-6*x**4+12*x**2-8)/(6*x**5-24*x**3+24*x)))


print(puntofijo(fNew2,1.5,10**(-12),500))


#EJERCICIO.2


#Calcula el denominador del polinomio de interpolacion de Lagrange    
def LagrangeD(xi,i):
    acum=1
    for j in range(len(xi)):
        if(j!=i):
            acum*=(xi[i]-xi[j])
    return(acum)

#Calcula el numerador del polinomio de interpolacion de Lagrange    
def LagrangeN(xi,i,x):
    acum=1
    for j in range(len(xi)):
        if(j!=i):
            acum*=(x-xi[j])
    return(acum)
       
#Calcula el polinomio de Lagrange, tan solo hace falta darle alores de x
x1=[1,2**3,3**3,4**3,5**3]
y1=[1,2,3,4,5]            
def polinomioInter(xi,yi,x):
    acum=0
    for j in range(len(xi)):
        acum+=(yi[j]*(LagrangeN(xi,j,x)/LagrangeD(xi,j)))
    return(acum)


xdat = [0 ,0.025 ,0.05 ,0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9 ,1]
yinf = [0 ,-0.0052 ,-0.0060 ,-0.0045 ,-0.0016, 0.0010 ,0.0036 ,0.0070 ,0.0121 ,0.0170, 0.0199 ,0.0178 ,0]
ysup =[0 ,0.0250, 0.0376 ,0.0563 ,0.0812 ,0.0962 ,0.1035, 0.1033, 0.0950, 0.0802, 0.0597 ,0.0340 ,0]

"En rojo se representa los puntos y en azul las funciones"
x=linspace(0,1,5000) 
axis([0, 1, 0, 1])
plot(x,polinomioInter(xdat,yinf,x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(x,polinomioInter(xdat,ysup,x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(xdat,yinf,'bo') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(xdat,ysup,'bo') #dibujar la grafica y 'r.' es color red con el simbolo .
title('Grafica de f y puntos')
figure()


#    (b)

x = linspace(0, 1, 500)
axis([0, 1, 0, 1])
y1 = sp.interpolate.interp1d(xdat, yinf, kind="cubic")(x)
y2 = sp.interpolate.interp1d(xdat, ysup, kind="cubic")(x) #otros tipos 'linear' o 'quadratic'
plot(x,y1,'r.')
plot(x,y2,'r.')
plot(xdat,yinf,'bo') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(xdat,ysup,'go') #dibujar la grafica y 'r.' es color red con el simbolo .
title('Grafica de f y spliceCubic')
figure()
































