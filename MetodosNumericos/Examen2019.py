#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:54:14 2021

@author: bini
"""

from numpy import *
from matplotlib.pyplot import *

#EJERCICIO.1

#  (a)



def programa(g,x0,nmax):
    niter = 0
    while(niter<=nmax):
        x1 = g(x0)
        print('Valor de x_'+str(niter)+' es '+str(g(x1)))
        niter+=1
        x0=x1
    return("El ultimo teermino del programa es "+str(x1))

#  (b)

def fun1(x):
    return(-e**x)

def fun2(x):
    return(log(-x))

def fun3(x):
    return(((x-1)*e**x)/(1+e**x))
"Converge y es el menos rapido"
def met1(x0,nmax):
    return(programa(fun1,x0,nmax))
"No converge"
def met2(x0,nmax):
    return(programa(fun2,x0,nmax))
"Converge y es el mas rapido"
def met3(x0,nmax):
    return(programa(fun3,x0,nmax))

#  (c)


#GRAFICA FUN1

x=linspace(-1,0,200) #eje x en [-1,0] con 200 pts
plot(x,fun1(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
axis([-1, 0, -1, 0])
plot(x,x,'b.') #dibujar la grafica y 'r.' es color red con el simbolo .
title('FUNCION 1º')
"La pendiente explica el porqué de que sea menos eficiente que la del metodo 3, pero sigue siendo lo suficientemente pequeña para que el metodo converja"
figure()


#GRAFICA FUN2

plot(x,fun2(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
axis([-1, 0, -1, 0])
plot(x,x,'b.') #dibujar la grafica y 'r.' es color red con el simbolo .
title('FUNCION 2º')
"La pendiente es demasido como para que el metodo converja"
figure()


#GRAFICA FUN3

plot(x,fun3(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
axis([-1, 0, -1, 0])
plot(x,x,'b.') #dibujar la grafica y 'r.' es color red con el simbolo .
title('FUNCION 3º')
"Es casi una linea horizontal, asi que la funcion aplicando el meto de punto fijo se aproxima mucho a su valor en x=-0.5 en pocas iteraciones"
figure()


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
def polinomioInter(xi,yi,x):
    acum=0
    for j in range(len(xi)):
        acum+=(yi[j]*(LagrangeN(xi,j,x)/LagrangeD(xi,j)))
    return(acum)

x=[1.047,1.134,1.221,1.308,1.396]
y=[0.86592661,0.90611159,0.93944253,0.96566732,0.98476198]
"Vamos a ordenar los puntos de x de menor a mayor, segun la distancia que esten de 1.2"
"Lo hemos calculado por abs(a-1.2)-abs(b-1.2)>0 entonces b está mas cerca que a, o al contrario"
xo=[1.221,1.134,1.308,1.047,1.396] # estan a la misma distancia 1.047 y 1.396
yo=[0.93944253,0.90611159,0.96566732,0.86592661,0.98476198]
def aproxsen(n):
    xi=xo[0:(n+1)]
    return(polinomioInter(xi,yo,1.2))    

#    (b)
def errorcom():
    for i in range(4):
        print('El polinomio de grado '+str(i+1)+' tiene un error cometido de '+str(abs(sin(1.2)-aproxsen(i+1))))
    return("Esos son los errores que se cometen, se observa que el grado mejora la exactitud")    

      
#    (c)

def aproxsenGrafica(n,x):
    xi=xo[0:(n+1)]
    print(xi)
    return(polinomioInter(xi,yo,x))  

xeje=linspace(1,1.4,200) #eje x en [0,1] con 200 pts
plot(xeje,aproxsenGrafica(4,xeje),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(xo,yo,'k*')
plot(1.2,sin(1.2),'bo')
title("Funcion seno")



















