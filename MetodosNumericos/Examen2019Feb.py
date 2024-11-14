#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:01:01 2021

@author: bini
"""

from numpy import *
from matplotlib.pyplot import *
from math import *
import scipy as sp
from scipy.interpolate import interp1d



#Calcula el denominador del polinomio de interpolacion de Lagrange ¡SIN BUCLE! 
def LagrangeD2(xi,i):
    list1 = linspace(xi[i],xi[i],len(xi[0:i]))
    list2 = linspace(xi[i],xi[i],len(xi[i+1:len(xi)]))
    return(prod(list1-xi[0:i])*prod(list2-xi[i+1:len(xi)]))



#Calcula el numerador del polinomio de interpolacion de Lagrange   ¡SIN BUCLE! 
def LagrangeN2(xi,i,x):
    list1 = linspace(x,x,len(xi[0:i]))
    list2 = linspace(x,x,len(xi[i+1:len(xi)]))
    return(prod(list1-xi[0:i])*prod(list2-xi[i+1:len(xi)]))

def polinomioInter2(xi,yi,x):
    acum=0
    for j in range(len(xi)):
         acum+=(yi[j]*(LagrangeN2(xi,j,x)/LagrangeD2(xi,j)))
    return(acum)


#EJERCICIO.1


def fun(x):
    return(e**(2*x)+3*x+2)

#    (a)

x=linspace(-1,0,200) 
plot(x,x*0,'k-')
plot(x,fun(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
title('Grafica de f')
figure()


#     (b)  METODO NEWTON

def puntofijo(g,x0,eps,nmax):
    x1=g(x0)
    niter = 0
    while(niter<nmax):
        niter+=1
        if(abs(x1-x0)<eps):
            return("Hemos llegado a un valor |x_n-x_(n-1)|<"+str(eps)+", y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:
            x0=x1
            x1=g(x0)
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))

def d1fun(x):
    return(2*e**(2*x)+3)

def newton(x):
    return(x-(fun(x)/(d1fun(x))))
#print("En el intervalo [-1,0] utilizando el metodo de Newton, obtenemos que: "+puntofijo(newton,-0.5,10**(-12),200))


#     (C)  METODO HALEY

def d2fun(x):
    return(4*e**(2*x))

def haley(x):
    return(x-(2*fun(x)*d1fun(x))/(2*d1fun(x)**2-fun(x)*d2fun(x)))
print("En el intervalo [-1,0] utilizando el metodo de Newton, obtenemos que: "+puntofijo(haley,-0.5,10**(-12),200))




#EJERCICIO.2

xdat = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1981, 1991]
ydat = [529.575, 562.525, 609.613, 688.193, 756.083, 781.690, 853.579, 1025.609, 1160.843]

#    (a)

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
def polinomioInter(xi,yi,x):
    acum=0
    for j in range(len(xi)):
        acum+=(yi[j]*(LagrangeN(xi,j,x)/LagrangeD(xi,j)))
    return(acum)

#    (b)

def interpolaLineal(x):
    return(sp.interpolate.interp1d(xdat, ydat, kind="linear")(x))


#    (c)


x = linspace(1910, 1991, 500)
plot(x,polinomioInter2(xdat,ydat,x),'r.')
title('Grafica de polinomio')
figure()

x = linspace(1910, 1991, 500)
plot(x,interpolaLineal(x),'r.')
title('Grafica de interpolacion lineal')
figure()







