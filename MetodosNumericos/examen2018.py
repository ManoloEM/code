#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:47:51 2021

@author: bini
"""
from numpy import *
from matplotlib.pyplot import *

#EJERCICIO.1

def f(x):
    return(x+(x-1)*e**x)

#  (a)
x=linspace(0,1,200) #eje x en [0,1] con 200 pts
y=linspace(-1,1,200) #eje y en [-1,1] con 200 pts
plot(x,f(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(x,0*x,'k-') #eje x color negro
plot(0*x,y,'k-') #eje y color negro
#  (b)
def df(x):
    return(1+e**x+(x-1)*e**x)

def MNewton(g,derg,c):
    while((abs(g(c)))>(10**(-8))):
        if((c<0 or c>1) or derg(c)==0):
            return("Se ha detenido el algoritmo, debido a que no se puede seguir aplicando")
        else:
            c=c-((g(c))/(derg(c)))
    return("Tu valor es",c)    
#  (c)
eps = 10**(-8)

def bisec2(f,a,b):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    N = int((log(b-a)-log(eps))/log(2))+1
    for i in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn)
        if fcn==0:
            return ("Tu valor es",cn) 
        elif (fan*fcn)<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    return ("Tu valor es",cn)   

"El metodo mas lento es de bisec2, ya que se necesita hacer muchas iteraciones para llegar a un solucion con mucha precision"

#EJERCICIO.2

#   (a)
    
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
    
"Para calcular el valor del polinomio de f^-1, es suficiente con tomar"
xi=[1.533,0.576,-0.554,-1.11,-2.1]
yi=[0,0.5,1,1.5,2]
"Y evaluar el polinomio en los valores de x deseados"

#   (b)

figure()
x=linspace(-2.1,1.533,200) #eje x  con 200 pts
y=linspace(0,2,200) #eje y en [-1,1] con 200 pts
plot(x,polinomioInter(xi,yi,x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(x,0*x,'k-') #eje x color negro
plot(0*x,y,'k-') #eje y color negro

#   (c)

fdcero = polinomioInter(xi,yi,0)
















































