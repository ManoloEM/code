# -*- coding: utf-8 -*-
"""
Spyder Editor

''''''' Metodos Analisis Numerico'''''''

This is a temporary script file.
@author: Manu/bini
"""

from pylab import *

# Nota: 
    # Anotar el input y output de cada metodo para facilitar

"-----------------------------------------------------------" 
"-------------------     Euler     -------------------------"
"-----------------------------------------------------------" 



def euler(a, b, fun, N, y0):
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros(N+1) # inicializacion del vector de resultados
    t[0] = a # nodo inicial
    y[0] = y0 # valor inicial
    # Metodo de Euler
    for k in range(N):
        y[k+1] = y[k]+h*fun(t[k], y[k])
        t[k+1] = t[k]+h
    return (t, y)



"-----------------------------------------------------------" 
"-----------------     Punto Medio     ---------------------"
"-----------------------------------------------------------" 



def puntomedio(a, b, fun, N, y0):
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros(N+1) # inicializacion del vector de resultados
    t[0] = a # nodo inicial
    y[0] = y0 # valor inicial
    # Metodo de Euler
    for k in range(N):
        y[k+1] = y[k]+h*fun(t[k]+h/2, y[k]+h/2*fun(t[k],y[k]))
        t[k+1] = t[k]+h
    return (t, y)



"------------------------------------------------------------" 
"-----------------     Runge-Kutta     ----------------------"
"------------------------------------------------------------" 



def RK4(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        k1 = fun(t[k],y[k])
        k2 = fun(t[k]+h/2,y[k]+h/2*k1)
        k3 = fun(t[k]+h/2,y[k]+h/2*k2)
        k4 = fun(t[k]+h,y[k]+h*k3)
        y[k+1] = y[k] +h/6*(k1+2*k2+2*k3+k4)
        t[k+1] = t[k]+h
    return(t,y)



"------------------------------------------------------------" 
"-------------------     Heun     ---------------------------"
"------------------------------------------------------------" 



def heun(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros(N+1)
    t[0] = a
    y[0] = y0
    for k in range(N):
        y[k+1] = y[k] +h/2*(fun(t[k],y[k])+fun(t[k]+h,y[k]+h*fun(t[k],y[k])))
        t[k+1] = t[k]+h
    return(t,y)



"-------------------------------------------------------------------" 
"-------------------     Euler Sistema     -------------------------"
"-------------------------------------------------------------------" 



def eulersistema(a, b, fun, N, y0):
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros([len(y0),N+1])
    t[0] = a 
    y[:,0] = y0  # valor inicial
    # Metodo de EulerSistema
    for k in range(N):
        y[:,k+1] = y[:,k]+h*fun(t[k], y[:,k])
        t[k+1] = t[k]+h
    return (t, y)



"--------------------------------------------------------------------" 
"-----------------     Punto Medio Sistema    -----------------------"
"--------------------------------------------------------------------" 


def puntomediosistema(a, b, fun, N, y0):
    h = (b-a)/N # paso de malla
    t = zeros(N+1) # inicializacion del vector de nodos
    y = zeros([len(y0),N+1])
    t[0] = a 
    y[:,0] = y0  # valor inicial
    # Metodo de EulerSistema
    for k in range(N):
        y[:,k+1] = y[:,k]+h*fun(t[k]+h/2, y[:,k]+h/2*fun(t[k],y[:,k]))
        t[k+1] = t[k]+h
    return (t, y)



"--------------------------------------------------------------------" 
"-----------------     Runge-Kutta Sistema    -----------------------"
"--------------------------------------------------------------------" 



def RK4sistema(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[:,0] = y0
    for k in range(N):
        k1 = fun(t[k],y[:,k])
        k2 = fun(t[k]+h/2,y[:,k]+h/2*k1)
        k3 = fun(t[k]+h/2,y[:,k]+h/2*k2)
        k4 = fun(t[k]+h,y[:,k]+h*k3)
        y[:,k+1] = y[:,k] +h/6*(k1+2*k2+2*k3+k4)
        t[k+1] = t[k]+h
    return(t,y)



"--------------------------------------------------------------------" 
"-------------------     Heun Sistema    ----------------------------"
"--------------------------------------------------------------------" 



def heunsistema(a,b,fun,N,y0):
    h = (b-a)/N
    t = zeros(N+1)
    y = zeros([len(y0),N+1])
    t[0] = a
    y[0] = y0
    for k in range(N):
        y[:,k+1] = y[:,k] +h/2*(fun(t[k],y[:,k])+fun(t[k]+h,y[:,k]+h*fun(t[k],y[:,k])))
        t[k+1] = t[k]+h
    return(t,y)
