#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:12:11 2023

@author: Manuel Enciso Martinez
"""

from pylab import *
from time import perf_counter




"""
-----------
EJERCICIO 1
-----------
"""



# DATOS

g = 9.81
M = 12. #masa
alpha = 0.02
# mfuel0 = 7.5 NO NECESITAMOS MASA DEL COHETE

a=0. #tiempo inicial
h0 = 0.1 #paso incial 

Z0 = 1000 #altura incial
v0 = -25 #signo debido a que cae
tol = 1.e-4


T0 = 119 #FUERZA motor
C = 0.01 #ROZAMIENTO

z0=array([Z0,v0])
    
#NO SE GASTA COMBUSTIBLE, MFUEL CTE
    
def fun(t,z):
    #z[0]:= x; z[1]:=y; z[2]:=velocidad, z[3]:=angulo, z[4]:=masa de combustible 

    m = M #maso constante
    T = T0 #fuerza constante del motor
    
    f0 = z[1]
    f1 = -g + T/m - C/m*z[1]*abs(z[1])

    
    return array([f0,f1])



def rk4_sis_rocket(a, z0, h0, fun): # SOLO USANDO METODO RK4
    """ Cohete paso constante y masa constante """

    # Inicializacion de variables
    t = array ([a]) # nodos
    z = zeros([len(z0),1])
#    z = z0.reshape(len(z0), 1) # alterativa para poner el vector de c.i.como columna
    z[:,0] = z0
    h = h0 # pasos de malla

    k = 0 # contador de iteraciones
    nonstop = True
    while (nonstop and t[k] < 1000): #
        #Aplicamos metodo RK4
        k1 = fun(t[k],z[:,k])
        k2 = fun(t[k]+h/2,z[:,k]+h/2*k1)
        k3 = fun(t[k]+h/2,z[:,k]+h/2*k2)
        k4 = fun(t[k]+h,z[:,k]+h*k3)
        z = column_stack((z, z[:,k] +h/6*(k1+2*k2+2*k3+k4)))
        t = append(t, (t[k]+h))
        k += 1
        if z[0,k] < 0: #altura del cohete
            nonstop = False
    if (t[k] >= 1000): #tiempo transcurrido mayor a 1000s
        print('Tiempo maximo alcanzado') #tiempo maximo alcanzado
    return (t, z)










print('-----')

tini = perf_counter()
(t1,z1)= rk4_sis_rocket(a, z0, h0, fun)
tfin = perf_counter()

print('Tiempo programa CPU',tfin-tini)

print('Tiempo que tarda el cohete en llegar a la tierra',t1[len(t1)-1])

print('Tiempo que tarda el cohete en llegar a la tierra',z1[1,len(t1)-1])
print('Observamos que el tiempo es negativo porque cae el cohete.')

"grafica"

figure('Gracficas ejer1')
subplot(211) # para dibujar en una misma ventana grafica una fila y dos columnas (dos graficas)
plot(t1, z1[0,:]) # dibuja grafica altura y tiempo
xlabel('t')
ylabel('y')
legend(['Altura respecto al tiempo'])
subplot(212)
plot(t1, z1[1,:]) # dibuja grafica velocidad y tiempo
xlabel('t')
ylabel('v')
legend(['Velocidad respecto al tiempo'])






























"""
-----------
EJERCICIO 2
-----------
"""

#DATOS
tol2 = 1.e-8
h02 = 0.01

def rk45_sis_rocket(a, z0, h0, tol): # SOLO USANDO METODO RK45
    """ Implementacion del metodo encajado RK2(3)
    en el intervalo [a, b] con condicion inicial y0 """
    

    

    hmin = 1.e-5 # paso de malla minimo
    hmax = .05 # paso de malla maximo
    
    
    # Coeficientes RK4(5)

    q = 6 # numero de etapas
    p = 4 # orden del método menos preciso
    A = zeros([q, q])
    A[1, 0] = 1./4.
    A[2, 0] = 3/32.
    A[2, 1] = 9/32.
    A[3,0] =1932/2197.
    A[3,1] = -7200/2197.
    A[3,2] = 7296/ 2197.
    A[4,0] = 439/216.
    A[4,1] = -8.
    A[4,2] = 3680/513.
    A[4,3] = -845/4104.
    A[5,0] = -8/27.
    A[5,1] = 2
    A[5,2] = -3544/2565.
    A[5,3] = 1859/4104.
    A[5,4] = -11/40.
    
    B = zeros(q)
    B[0] = 25/216.
    B[2] = 1408/2565. 
    B[3] = 2197/4104.
    B[4] = -1/5.
    
    BB = zeros(q)
    BB[0] = 16./135.
    BB[2] = 6656./12825.
    BB[3] = 28561./56430.
    BB[4] = -9/50.
    BB[5] = 2/55.
    
    C = zeros(q)
    for i in range(q):
        C[i] = sum(A[i,:])
    
    # Inicializacion de variables
    t = array ([a]) # nodos
    z = zeros([len(z0),1])
#    z = z0.reshape(len(z0), 1) # alterativa para poner el vector de c.i.como columna
    z[:,0] = z0
    h = array ([h0]) # pasos de malla
    K = zeros ([len(z0), q])
    k = 0 # contador de iteraciones
    nonstop = True
    
    while (nonstop and t[k] < 1000):
        for i in range(q):
            K[:,i] = fun(t[k]+C[i]*h[k], z[:,k]+h[k]*dot(A[i,:], transpose(K)))
        incrlow = dot(B, transpose(K))
        incrhigh = dot(BB, transpose(K))
        error = h[k]*(incrhigh-incrlow) # estimacion del error
        z = column_stack((z, z[:,k]+h[k]*incrlow))
        t = append(t, t[k]+h[k])
        hnew = 0.9*h[k]*abs(tol/norm(error, inf))**(1./(p+1))
        hnew = min(max(hnew, hmin), hmax)
        h = append(h, hnew)
        k += 1
        if z[0,k] < 0:
            nonstop = False
    if (t[k] >= 1000): #tiempo transcurrido mayor a 1000s
        print('Tiempo maximo alcanzado') #tiempo maximo alcanzado
    return (t, z, h)




print('-----')

tini2 = perf_counter()
(t2,z2,h2)= rk45_sis_rocket(a, z0, h02, tol2)
tfin2 = perf_counter()

print('Tiempo programa CPU',tfin2-tini2)

print('Tiempo que tarda el cohete en llegar a la tierra',t2[len(t2)-1])

print('Tiempo que tarda el cohete en llegar a la tierra',z2[1,len(t2)-1])
print('Observamos que el tiempo es negativo porque cae el cohete.')

"grafica"

figure('Gracficas ejer2')
subplot(311) # para dibujar en una misma ventana grafica una fila y dos columnas (dos graficas)
plot(t2, z2[0,:]) # dibuja grafica altura y tiempo
xlabel('t')
ylabel('y')
legend(['Altura respecto al tiempo'])
subplot(312)
plot(t2, z2[1,:]) # dibuja grafica velocidad y tiempo
xlabel('t')
ylabel('v')
legend(['Velocidad respecto al tiempo'])
subplot(313)
plot(t2, h2) # dibuja grafica velocidad y tiempo
xlabel('t')
ylabel('pasos')
legend(['Pasos respecto al tiempo'])

"""
COMENTARIO:
    .)El ejercicio 1 realiza el proceso en menos tiempo de CPU aunque luego tanto la velocidad de llegada
    como el tiempo transcurrido en el aire coinciden (como podria ser de esperar).
    Podemos pensar que una de las razones puede ser el paso de malla, ya que en el ejercicio 1 es el doble
    que en el ejercicio 2, y esto se ve reflejado a que se hacen el doble de iteraciones en un respecto 
    al otro.
    .)Se observa como el paso incial es mas pequeño de lo necesario y enseguida llega al paso maximo, 
    ademas por el tipo funcion el programa siempre selecciona el paso mas grande que le hemos
    proporcionado para avanzar
"""




























































