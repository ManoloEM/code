#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:31:22 2021

@author: bini
"""

from numpy import *
from matplotlib.pyplot import *
from math import *
import scipy as sp
from scipy.interpolate import interp1d





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


x1 = [0,0.5,1,1.5,2]
y1 = [1.533,0.576,-0.554,-1.11,-2.1]





print('\n EJERCICIO 1\n')

def funpol(x):
    return(polinomioInter(x1,y1,x))



print('\n EJERCICIO 2\n')

ptsx = linspace(0,2,200)
plot(ptsx,funpol(ptsx),'r-')
plot(ptsx,0*ptsx,'k-')
plot(0*ptsx,linspace(-2,1.5,200),'k-')
title('Funcion Polinomio de interpolacion')




print('\n EJERCICIO 3\n')


def ejercicio22(h,a,b):
    x0=a
    x1=b
    while((abs(h(x1)))>(10**(-5))):
        print(x1)
        if((x1<=0) or (h(x1)==h(x0))):
            return("Hemos llegado a un callejon sin salida")
        else:
            acum= x1
            x1=x1-((x1-x0)/(h(x1)-h(x0)))*h(x1)
            x0=acum
    return("Tu valor es", x1)        



print(ejercicio22(funpol,0.5,1))


ejercicio22(sp.interpolate.interp1d(x1, y1, kind="cubic"),0.5,1)









