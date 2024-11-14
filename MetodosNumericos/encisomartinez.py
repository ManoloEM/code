#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:33:43 2021

@author: Manuel Enciso Martinez
"""

from numpy import *
from matplotlib.pyplot import *
import scipy as sp  #Polinomios interpolacion
from scipy.interpolate import interp1d #Polinomios interpolacion
from scipy.integrate import quad #Integrales interpolacion


#EJERCICIO.1.
print('\n EJERCICIO 1 \n')

def sumamedia(ar):
    suma = sum(ar)
    media = sum(ar)/len(ar)
    return('El valor de la suma es '+str(suma)+' y la media aritmetica '+str(media))

conjx = [-1, -2, 0 , 3 , 2, 1]

print('El ejercicio 1 da como resultado:',sumamedia(conjx))

#EJERCICIO.2.
print('\n EJERCICIO 2 \n')

def dicotomia(f,a,b,eps): 
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    N = int((log(b-a)-log(eps))/log(2))+1
    for i in range(N):
        cn=(an+bn)/2.0
        print("El valor de c_"+str(i)+" es "+str(cn))
        fcn=f(cn)
        print("El valor de f(c_"+str(i)+") es "+str(fcn))
        if fcn==0:
            return cn
        elif (fan*fcn)<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    return cn

def fun(x):
    return(sin(x))

ldicotomia = dicotomia(fun,2,4,10**(-8))

print('En el ejercicio 2 la constante que se aproxima al valor obtenido es pi')

#EJERCICIO.3.
print('\n EJERCICIO 3 \n')


def metodonewton(f,df,x0,eps,nmax): 
    niter = 0
    x1 = x0 - f(x0)/df(x0)
    while(niter<nmax):
        if(abs(abs(x1)-abs(x0))<eps): #donde f es la funcion de original
            return("Hemos llegado a un valor |x_"+str(niter)+"-x_"+str(niter-1)+"|<"+str(eps)+", y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:  #recomendable dar la f'(x) y comprobar si se anula (si se puede llegar a anular en el int).
            print('Iteracion'+str(niter)+', valor de x_'+str(niter)+' es igual a '+str(x0))
            niter+=1
            x0= x1
            x1= x0 - f(x0)/df(x0)
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))


def fun3(x):
    return(cos(x/2))

def dfun3(x):
    return(-1/2*sin(x/2))

print('El ejercicio 3 da como resultado:',metodonewton(fun3,dfun3,2.5,10**(-12),100))


#EJERCICIO.4.
print('\n EJERCICIO 4 \n')


xdat = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
ydat = [ -0.0385, -0.0588, -0.1000, -0.2000, -0.5000, -1.0000, -0.5000, -0.2000, -0.1000, -0.0588, -0.0385]

#Calcula el denominador del polinomio de interpolacion de Lagrange    
def LagrangeD(conx,i): 
    list1 = linspace(conx[i],conx[i],len(conx[0:i]))
    list2 = linspace(conx[i],conx[i],len(conx[i+1:len(conx)]))
    return(prod(list1-conx[0:i])*prod(list2-conx[i+1:len(conx)]))

#Calcula el numerador del polinomio de interpolacion de Lagrange    
def LagrangeN(conx,i,x):
    acum=1
    for j in range(len(conx)):
        if(j!=i):
            acum*=(x-conx[j])
    return(acum)
       
#Calcula el polinomio de Lagrange, tan solo hace falta darle alores de x            
def polinomioInter(conx,cony,x):
    acum=0
    for j in range(len(conx)):
        acum+=(cony[j]*(LagrangeN(conx,j,x)/LagrangeD(conx,j)))
    return(acum)
 

def PolinomioInterpolacion(x):
    return(polinomioInter(xdat,ydat,x))


ejex=linspace(-1,1,1000) #eje x en [-1,1] con 1000 pts'
plot(ejex,PolinomioInterpolacion(ejex),'r|') #dibujar la grafica y 'r.' es color red con el simbolo |
conLineal = sp.interpolate.interp1d(xdat, ydat, kind="linear")(ejex) #donde x es una lista de volaores a interpolar y kind = lineal es el tipo
plot(ejex,conLineal,'k*') #dibujar la grafica y 'k.' es color negro con el simbolo *
plot(xdat,ydat,'bo') #representar los puntos xdat ydat
title('Grafica de las dos funciones de interpolacion') #Poner titulo
figure() #Cerrar pagina del plot (para seguir dibujando en otra)

print("Sabien que solo deberia tener un minimo local, podemos asegurar que en este caso Interpolacion Lineal representa mejor a la funcion f (debido a que la funcion del polinomio ,representado en rojo, tiene dos minimos) ")



#EJERCICIO.5.
print('\n EJERCICIO 5 \n')


def trapeciocomp(valx,valy):
    lng = len(valx)
    itrapecioc = (valx[lng-1]-valx[0])/(2*(lng-1))*((valy[0]+valy[lng-1])+2*sum(valy[1:(lng-1)]))
    return(itrapecioc)


print('Aplicando trapeciocomp al conjunto del ejercicio 4 nos queda como resultado',trapeciocomp(xdat,ydat),'que corresponde a la integral de la grafica lineal anterior.')



































