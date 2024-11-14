#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 17:03:52 2021

@author: bini
"""

#from gekko import GEKKO
from scipy.interpolate import interp1d
from numpy import *
from matplotlib.pyplot import *
import scipy as sp

#EJERCICIO.1


#    (a)

def fun(x):
    return(log(x)-1/x)

x=linspace(1,3,200) #eje x en [0,1] con 200 pts
y=linspace(fun(1),fun(3),200) #eje y en [-1,1] con 200 pts
plot(x,fun(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(x,0*x,'k-') #eje x color negro
plot(0*x+1,y,'k-') #eje y color negro
title('Grafica de f')
figure()
"Seobserva que un intervalo valido es [1.5,2.5]"


#    (b)

def puntofijo(g,x0,nmax):
    niter = 0
    while(niter<nmax):
        niter+=1
        x1=g(x0)
        if(abs(fun(x1))<10**(-10)):
            return("Hemos llegado a un valor |f(x_n)|<10^-10, y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:
            x0=x1
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))

def m1(x):
    return(e**(1/x))

def m2(x):
    return(1/(log(x)))

def m3(x):
    return((x**2*(1-log(x))+2*x)/(x+1))

#print('Con el metodo1 obtenemos ', puntofijo(m1,2,500))
#print('Con el metodo2 obtenemos ', puntofijo(m2,2,500))
#print('Con el metodo3 obtenemos ', puntofijo(m3,2,500))


#    (c)

"El metodo m1 y m2 son los unicos convergentes, el mas rapido es m3, ya que le lleva menos iteraciones conseguir el resutlado con la precision deseada"

# x=linspace(1.5,2.5,200) #eje x en [0,1] con 200 pts
# y=linspace(m1(1.5),0,200) #eje y en [-1,1] con 200 pts
# plot(x,m1(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
# plot(x,0*x,'k-') #eje x color negro
# plot(0*x+1.5,y,'k-') #eje y color negro
# title('Grafica de m1')

# figure()

# x=linspace(1.5,2.5,200) #eje x en [0,1] con 200 pts
# y=linspace(m3(1.5),0,200) #eje y en [-1,1] con 200 pts
# plot(x,m3(x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
# plot(x,0*x,'k-') #eje x color negro
# plot(0*x+1.5,y,'k-') #eje y color negro
# title('Grafica de m3')

"Se observa, que el m3 tiene derivada proxima a 0 en el intervalo. Resulta mejor"



#EJERCICIO.2

#  (a)

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




#   (b)
"En rojo se representa el Polinomio y en azul la funcion"
x=linspace(1,5**3,400) #eje x en [0,1] con 200 pts
y=linspace(1,5,400) #eje y en [-1,1] con 200 pts
plot(x,polinomioInter(x1,y1,x),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(x,x**(1/3),'b.') #dibujar la grafica y 'r.' es color red con el simbolo .
title('Grafica de f y polinomioInter')
figure()

#   (c)

raiz10 = polinomioInter(x1,y1,10)
raiz100 = polinomioInter(x1,y1,100)

compaRaiz10 = abs(raiz10-10**(1/3))
compaRaiz100 = abs(raiz10-100**(1/3))


#   (d)

#from gekko import GEKKO

# (a)  #Splice cubic
x = linspace(1, 5**3, 400)
y = sp.interpolate.interp1d(x1, y1, kind="cubic")(x)
plot(x,y,'r.')
plot(x,x**(1/3),'b.')
title('Grafica de f y spliceCubic')
figure()

# (b)

raiz10S = sp.interpolate.interp1d(x1, y1, kind="cubic")(10)
raiz100S = sp.interpolate.interp1d(x1, y1, kind="cubic")(100)

compaRaiz10S = abs(raiz10S-10**(1/3))
compaRaiz100S = abs(raiz100S-100**(1/3))

























