#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:55:57 2021

@author: bini
"""

from numpy import *
from matplotlib.pyplot import *
from math import *
import scipy as sp  #Polinomios interpolacion
from scipy.interpolate import interp1d #Polinomios interpolacion
from scipy.integrate import quad #Integrales interpolacion

def f(x):
    return(x)

"----------------"
"---RELACION-1---"
"----------------"

" COMANDO PLOT"
ejex=linspace(0,1,200) #eje x en [0,1] con 200 pts'
ejey=linspace(-1,1,200) #eje y en [-1,1] con 200 pts
plot(ejex,f(ejex),'r.') #dibujar la grafica y 'r.' es color red con el simbolo .
plot(ejex,ejex,'b.') #dibujar la grafica y 'r.' es color red con el simbolo .
axis([0, 1, -1, 1]) #Amplia SIN DIBUJAR el eje x,y a [0,1] y [-1,1] respectivamente
plot(ejex,0*ejex,'k-') #eje x color negro
plot(0*ejex,ejey,'k-') #eje y color negro
title('Funcion Polinomio de interpolacion') #Poner titulo
figure() #Cerrar pagina del plot (para seguir dibujando en otra)




"POLINOMIO INTERPOLACION"
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

conLineal = sp.interpolate.interp1d(xdat, ydat, kind="linear")(x) #donde x es una lista de volaores a interpolar

conCubic = sp.interpolate.interp1d(xdat, yinf, kind="cubic")(x) #donde x es una lista de volaores a interpolar

"----------------"
"---RELACION-2---"
"----------------"

def bisec(f,a,b,N):  #Metodo de dicotomia
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    for i in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn)
        if fcn==0:
            return cn
        elif (fan*fcn)<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    return cn

#Te calcula nº de pasos a realizar segun el valor de e de error que queramos
def bisec2(f,a,b,eps): #Metodo de dicotomia
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

#regula_fasi con parada segun epsilon o nmax de iteraciones
def regulafasi(f,a,b,eps,nmax): #Metodo regulafasi
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    cn1=bn-((bn-an)/(fbn-fan))*fbn
    print("El valor de c_"+str(0)+" es "+str(cn1))
    fcn1=f(cn1)
    print("El valor de f(c_"+str(0)+") es "+str(fcn1))
    if fcn1==0:
        return("Valor con maxima precision posible se ha llegado, siendo este"+str(cn1))
    elif (fan*fcn1)<0:
        bn=cn1
        fbn=fcn1
    else:
        an=cn1
        fan=fcn1
    for i in range(nmax):
        cn2 = cn1
        cn1=bn-((bn-an)/(fbn-fan))*fbn
        print("El valor de c_"+str(i+1)+" es "+str(cn1))
        fcn1=f(cn1)
        print("El valor de f(c_"+str(i+1)+") es "+str(fcn1))
        if fcn1==0:
            return("Valor con maxima precision posible se ha llegado, siendo este"+str(cn1))
        elif (abs(cn2-cn1)<=eps):
            return("aproximacion alcanzada, el resutaldo es "+str(cn1))
        elif (fan*fcn1)<0:
            bn=cn1
            fbn=fcn1 
        else:
            an=cn1
            fan=fcn1
    return ("Se ha llegado al numero maximo, el resultado es "+str(cn1))

#secante con parada segun epsilon o nmax de iteraciones
def secante(f,x0,x1,eps,nmax): #Metodo secante
    a = x0
    b = x1
    if (f(x0)==f(x1)):
        return("Hemos llegado a una parada forzada, los valores de f(xn) coincide con f(xn-1)")
    else:
        for i in range(nmax):
            print("Paso numero "+str(i))
            ayuda = x1
            x1 = x1 - ((x1-x0)/(f(x1)-f(x0)))*f(x1)
            if (x1 < a or x1 > b )or(f(x0)==f(x1)):
                return("Hemos llegado a una parada forzada, los valores de f(xn) coincide con f(xn-1)")
            else:
                x0 = ayuda
                if (abs(x1-x0)<=eps):
                    return("Hemos llegado a un resultado lo suficientemente pequeño "+str(x1))
        return("Hemos llegado al nmax de iteraciones "+str(x1))

#El metodo de Newton o tangente es parecido que (Metodo ptf), pero con cn+1 = cn-(fcn)/(f'cn)
def newton(g,x0,eps,nmax): #Metodo Newton (Importante dar la f(x) como funcion base)
    x1=g(x0)
    niter = 0
    while(niter<nmax):
        niter+=1
        if(abs(f(x1))<eps): #donde f es la funcion de original
            return("Hemos llegado a un valor |g(x_n)|<eps, y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:  #recomendable dar la f'(x) y comprobar si se anula (si se puede llegar a anular en el int).
            x0=x1
            x1=g(x0)
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))


"----------------"
"---RELACION-3---"
"----------------"

#Para comprobar si un metodo converge, dibujar grafica y ver su penditente, respecto de x=y, en abs < 1.
#Para comprobar si converge,tambien podemos usar la deriva de g(x) (f(x)=x-g(x)=0)
#El orden del meto es p <=> la derivada p-esima de g es no nula. C = |gp(l)|/p!
#Puntofijo con parada segun epsilon o nmax de iteraciones
def puntofijo(g,x0,eps,nmax): #Metodo punto fijo
    x1=g(x0)
    niter = 0
    while(niter<nmax):
        niter+=1
        if(abs(x1-x0)<eps):
            return("Hemos llegado a un valor |x_n-x_(n-1)|<eps, y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:
            x0=x1
            x1=g(x0)
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))

#El metodo de Newton o tangente es parecido que (Metodo ptf), pero con cn+1 = cn-(fcn)/(f'cn)
def newton(g,x0,eps,nmax): #Metodo Newton (Importante dar la f(x) como funcion base)
    x1=g(x0)
    niter = 0
    while(niter<nmax):
        niter+=1
        if(abs(f(x1))<eps): #donde f es la funcion de original
            return("Hemos llegado a un valor |g(x_n)|<eps, y el último termino de la sucesion es "+str(x1)+", con un total de iteraciones igual a "+str(niter))
        else:  #recomendable dar la f'(x) y comprobar si se anula (si se puede llegar a anular en el int).
            x0=x1
            x1=g(x0)
    return("No hemos podido llegar a la solucion con este numero de iteraciones "+str(nmax))

"----------------"
"---RELACION-5---"
"----------------"



















