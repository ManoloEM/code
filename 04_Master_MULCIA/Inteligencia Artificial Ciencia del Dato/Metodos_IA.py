# Inteligencia Artificial para la Ciencia de los Datos
# Implementación de clasificadores 
# Dpto. de C. de la Computación e I.A. (Univ. de Sevilla)
# ===================================================================


# --------------------------------------------------------------------------
# Autor(a) del trabajo:
#
# APELLIDOS: Enciso Martínez
# NOMBRE: Manuel
#
# Segundo componente (si se trata de un grupo):
#
# APELLIDOS:
# NOMBRE:
# ----------------------------------------------------------------------------


# *****************************************************************************
# HONESTIDAD ACADÉMICA: PLAGIO O CÓDIGO GENERADO AUTOMÁTICAMENTE.
# Un trabajo práctico es un examen, por lo que debe realizarse de manera 
# individual o con la pareja del grupo. 
# La discusión y el intercambio de información de carácter general con los 
# compañeros se permite, pero NO AL NIVEL DE CÓDIGO. 

# El objetivo principal del entregable es trabajar de manera práctica 
# los conceptos aprendidos en clase, para alcanzar una mayor comprensión 
# de los mismos a través de la implementación que se pide.  
# Se permite, si así se desea, el uso de herramientas de inteligencia 
# artificial generativa que ayuden en el desarrollo código, 
# pero esta herramienta ha de usarse sólo como un asistente que facilite 
# el trabajo, y en ningún caso se debe entregar un código que no se conozca 
# en profundidad, y sobre el que no se sepa responder durante la presentación
# al profesor a cualquier pregunta con el detalle requerido. Si el trabajo se 
# realiza en pareja, cualquiera de los dos miembros del grupo debe de poder
# responder con detalle de código en cualquiera de los apartados del trabajo.  

# Cualquier plagio o entrega de código cuyo funcionamiento no se sea capaz de
# explicar con detalle, supondrá una calificación de cero, sin perjuicio
# de las medidas disciplinarias que se pudieran tomar.  
# *****************************************************************************





# MUY IMPORTANTE: 
# ===============    
    
# * NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS CLASES, MÉTODOS
#   Y ATRIBUTOS QUE SE PIDEN. EN PARTICULAR: NO HACERLO EN UN NOTEBOOK.

# * En este trabajo NO SE PERMITE USAR Scikit Learn. 
  
# * Se recomienda (y se valora especialmente) el uso eficiente de numpy. Todos 
#   los datasets se suponen dados como arrays de numpy. 

# * Este archivo (con las implementaciones realizadas), ES LO ÚNICO QUE HAY QUE ENTREGAR.
#   AL FINAL DE ESTE ARCHIVO hay una serie de ejemplos a ejecutar que están comentados, y que
#   será lo que se ejecute durante la presentación del trabajo al profesor.
#   En la versión final a entregar, descomentar esos ejemplos del final y no dejar 
#   ninguna otra ejecución de ejemplos. 



import math
import random
import numpy as np



# *****************************************
# CONJUNTOS DE DATOS A USAR EN ESTE TRABAJO
# *****************************************

# Para aplicar las implementaciones que se piden en este trabajo, vamos a usar
# los siguientes conjuntos de datos. Para cargar (casi) todos los conjuntos de datos,
# basta con tener descomprimido el archivo datos-trabajo-1-iacd.tgz (en el mismo sitio
# que este archivo) Y CARGARLOS CON LA SIGUIENTE ORDEN. 
    
from carga_datos import *    

# Como consecuencia de la línea anterior, se habrán cargado los siguientes 
# conjuntos de datos, que pasamos a describir, junto con los nombres de las 
# variables donde se cargan. Todos son arrays de numpy: 


# * Conjunto de datos de la planta del iris. Se carga en las variables X_iris,
#   y_iris.  

# * Datos sobre votos de cada uno de los 435 congresitas de Estados Unidos en
#   17 votaciones realizadas durante 1984. Se trata de clasificar el partido al
#   que pertenece un congresita (0:republicano o 1:demócrata) en función de lo
#   votado durante ese año. Se carga en las variables X_votos, y_votos. 

# * Datos sobre concesión de prestamos en una entidad bancaria. En el propio
#   archivo datos/credito.py se describe con más detalle. Se carga en las
#   variables X_credito, y_credito.   


# * Datos de la Universidad de Wisconsin sobre posible imágenes de cáncer de
#   mama, en función de una serie de características calculadas a partir de la
#   imagen del tumor. Se carga en las variables X_cancer, y_cancer.

  
# * Críticas de cine en IMDB, clasificadas como positivas o negativas. El
#   conjunto de datos que usaremos es sólo una parte de los textos del dataset original. 
#   Los textos se han vectorizado usando CountVectorizer de Scikit Learn, con la opción
#   binary=True. Como vocabulario, se han usado las 609 palabras que ocurren
#   más frecuentemente en las distintas críticas. La vectorización binaria
#   convierte cada texto en un vector de 0s y 1s en la que cada componente indica
#   si el correspondiente término del vocabulario ocurre (1) o no ocurre (0)
#   en el texto (ver detalles en el archivo carga_datos.py). Los datos se
#   cargan finalmente en las variables X_train_imdb, X_test_imdb, y_train_imdb,
#   y_test_imdb.    

# Además, en la carpeta datos/digitdata se tiene el siguiente dataset, que
# habrá de ser procesado y cargado:  

# * Un conjunto de imágenes (en formato texto), con una gran cantidad de
#   dígitos (de 0 a 9) escritos a mano por diferentes personas, tomado de la
#   base de datos MNIST. En la carpeta digitdata están todos los datos.
#   Para preparar estos datos habrá que escribir funciones que los
#   extraigan de los ficheros de texto (más adelante se dan más detalles). 



# ==================================================
# EJERCICIO 1: SEPARACIÓN EN ENTRENAMIENTO Y PRUEBA 
# ==================================================
#           [*][*][*]   COMPLETADO   [*][*][*] 
#           [*][*][*]   COMPLETADO   [*][*][*] 
#           [*][*][*]   COMPLETADO   [*][*][*] 

# Definir una función 

#           particion_entr_prueba(X,y,test=0.20)

def particion_entr_prueba(X, y, test=0.20):
    clases = np.unique(y)
    indices_entre = []
    indices_prueba  = []
    
    for cls in clases:
        # índices de la clase actual
        clase_indices = np.where(y == cls)[0].tolist()
        random.shuffle(clase_indices)
        
        # Número de muestras para test
        n_test = math.ceil(len(clase_indices) * test)
        
        indices_prueba.extend(clase_indices[:n_test])
        indices_entre.extend(clase_indices[n_test:])
    
    # Mezclar los índices finales
    random.shuffle(indices_entre)
    random.shuffle(indices_prueba)
    
    X_train = X[indices_entre]
    X_test  = X[indices_prueba]
    y_train = y[indices_entre]
    y_test  = y[indices_prueba]
    
    return X_train, X_test, y_train, y_test


# que recibiendo un conjunto de datos X, y sus correspondientes valores de
# clasificación y, divide ambos en datos de entrenamiento y prueba, en la
# proporción marcada por el argumento test. La división ha de ser ALEATORIA y
# ESTRATIFICADA respecto del valor de clasificación. Por supuesto, en el orden 
# en el que los datos y los valores de clasificación respectivos aparecen en
# cada partición debe ser consistente con el orden original en X e y.   
# 

# ------------------------------------------------------------------------------
# Ejemplos:
# =========

# En votos:

# >>> Xe_votos,Xp_votos,ye_votos,yp_votos=particion_entr_prueba(X_votos,y_votos,test=1/3)


# Xe_votos,Xp_votos,ye_votos,yp_votos=particion_entr_prueba(X_votos,y_votos,test=1/3)


# Como se observa, se han separado 2/3 para entrenamiento y 1/3 para prueba:
# >>> y_votos.shape[0],ye_votos.shape[0],yp_votos.shape[0]
#    (435, 290, 145)



# Las proporciones entre las clases son (aprox) las mismas en los dos conjuntos de
# datos, y la misma que en el total: 267/168=178/112=89/56


# print(f"Clases en train: {np.unique(ye_votos, return_counts=True)}")
# print(f"Clases en test:  {np.unique(yp_votos, return_counts=True)}")


# >>> np.unique(y_votos,return_counts=True)
#  (array([0, 1]), array([168, 267]))
# >>> np.unique(ye_votos,return_counts=True)
#  (array([0, 1]), array([112, 178]))
# >>> np.unique(yp_votos,return_counts=True)
#  (array([0, 1]), array([56, 89]))

# La división en trozos es aleatoria y, por supuesto, en el orden en el que
# aparecen los datos en Xe_votos,ye_votos y en Xp_votos,yp_votos, se preserva
# la correspondencia original que hay en X_votos,y_votos.


# Otro ejemplo con los datos del cáncer, en el que se observa que las proporciones
# entre clases se conservan en la partición. 
    
# >>> Xev_cancer,Xp_cancer,yev_cancer,yp_cancer=particion_entr_prueba(X_cancer,y_cancer,test=0.2)

# Xev_cancer,Xp_cancer,yev_cancer,yp_cancer=particion_entr_prueba(X_cancer,y_cancer,test=0.2)


# >>> np.unique(y_cancer,return_counts=True)
# (array([0, 1]), array([212, 357]))

# >>> np.unique(yev_cancer,return_counts=True)
# (array([0, 1]), array([170, 286]))

# >>> np.unique(yp_cancer,return_counts=True)
# (array([0, 1]), array([42, 71]))    


# Podemos ahora separar Xev_cancer, yev_cancer, en datos para entrenamiento y en 
# datos para validación.

# >>> Xe_cancer,Xv_cancer,ye_cancer,yv_cancer=particion_entr_prueba(Xev_cancer,yev_cancer,test=0.2)

# >>> np.unique(ye_cancer,return_counts=True)
# (array([0, 1]), array([170, 286]))

# >>> np.unique(yv_cancer,return_counts=True)
# (array([0, 1]), array([170, 286]))


# Otro ejemplo con más de dos clases:

# >>> Xe_credito,Xp_credito,ye_credito,yp_credito=particion_entr_prueba(X_credito,y_credito,test=0.4)

# >>> np.unique(y_credito,return_counts=True)
# (array(['conceder', 'estudiar', 'no conceder'], dtype='<U11'),
#  array([202, 228, 220]))

# >>> np.unique(ye_credito,return_counts=True)
# (array(['conceder', 'estudiar', 'no conceder'], dtype='<U11'),
#  array([121, 137, 132]))

# >>> np.unique(yp_credito,return_counts=True)
# (array(['conceder', 'estudiar', 'no conceder'], dtype='<U11'),
#  array([81, 91, 88]))
# ------------------------------------------------------------------
























# =========================================================
# EJERCICIO 2: IMPLEMENTACIÓN DE CLASIFICADORES NAIVE BAYES
# =========================================================


# Se pide implementar clasificadores Naive Bayes, tanto en su versión categórica
# como en su versión gaussiana, con suavizado y log probabilidades 
# (descritos en el tema 2, diapositivas 22 a 34 y diapositivas 48 a 50). 
# En concreto:


# ---------------------------------------------
# 2.1) Implementación de Naive Bayes categórico
# ---------------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Definir una clase NaiveBayesCat con la siguiente estructura:

# class NaiveBayesCat():

#     def __init__(self,k=1):
#                 
#          .....
         
#     def entrena(self,X,y):

#         ......

#     def clasifica_prob(self,ejemplo):

#         ......

#     def clasifica(self,ejemplo):

#         ......

#       [*][*][*]   Solución   [*][*][*]

class NaiveBayesCat():

    def __init__(self,k=1):
        self.k = k
        self.entrenado = False
        

         
    def entrena(self,X,y):
        # Para entrenar calcular prob a priori y condicionadas
        # Formula con suavizado: n(A = v | C = c) + k / n(C = c) + k|A|
        #
        # Mediante diccionarios
        # Para cada instancia: { clase -> { índice_atributo -> { valor -> frecuencia } } }
        # Para cada clase: {clase -> frecuencia }
        self.clases = list(set(y)) 
        self.prob_condicionada = {} 
        self.prob_a_priori = {}

        # Inicializar estructura: {clase: {j_atributo: {}}}
        for c in self.clases:
            self.prob_condicionada[c] = {j: {} for j in range(len(X[0]))}
            self.prob_a_priori[c] = 0

        # Rellenar frecuencias
        for instancia, clase in zip(X, y):
            self.prob_a_priori[clase] += 1
            for j, valor in enumerate(instancia):
                frec_atr = self.prob_condicionada[clase][j]
                frec_atr[valor] = frec_atr.get(valor, 0) + 1 # get(valor,0) obtiene la frecuencia actual o 0 si no ha aparecido
        
        self.entrenado = True # Proceso de entrenamiento realizado


    def clasifica_prob(self,ejemplo):
        # Error si no se entrena primero
        if not self.entrenado:
            raise ClasificadorNoEntrenado("El clasificador no ha sido entrenado. Llama a entrena() primero.")
        
        total_prob = sum(self.prob_a_priori.values())
        dist_prob = {}

        for clase in self.clases:
            # Probabilidad a priori P(C=c) 
            prob = self.prob_a_priori[clase] / total_prob

            # Producto de P(Xj=vj | C=c) con suavizado
            for j, valor in enumerate(ejemplo):
                n_vc = self.prob_condicionada[clase][j].get(valor, 0)
                n_c  = self.prob_a_priori[clase]
                n_A  = len(self.prob_condicionada[clase][j])
                prob *= (n_vc + self.k) / (n_c + self.k * n_A)

            dist_prob[clase] = prob # p(+) * p(a|+) ...
        
        suma_normalizar = sum(dist_prob.values())
        dist_prob_normalizada = {c: p / suma_normalizar for c, p in dist_prob.items()}

        return dist_prob_normalizada


    def clasifica(self,ejemplo):
        # Error si no se entrena primero
        if not self.entrenado:
            raise ClasificadorNoEntrenado("El clasificador no ha sido entrenado. Llama a entrena() primero.")
        
        dist_prob = self.clasifica_prob(ejemplo)
        clase_mayor_prob = max(dist_prob, key=dist_prob.get) # maximo de las distribuciones 

        return np.array(clase_mayor_prob)



# * El constructor recibe como argumento la constante k de suavizado (por
#   defecto 1) 
# * Método entrena, recibe como argumentos dos arrays de numpy, X e y, con los
#   datos y los valores de clasificación respectivamente. Tiene como efecto el
#   entrenamiento del modelo sobre los datos que se proporcionan. NOTA: Se valorará
#   que el entrenamiento se haga con un único recorrido del dataset. 
# * Método clasifica_prob: recibe un ejemplo (en forma de array de numpy) y
#   devuelve una distribución de probabilidades (en forma de diccionario) que
#   a cada clase le asigna la probabilidad que el modelo predice de que el
#   ejemplo pertenezca a esa clase. 
# * Método clasifica: recibe un ejemplo (en forma de array de numpy) y
#   devuelve la clase que el modelo predice para ese ejemplo.   

# Si se llama a los métodos de clasificación antes de entrenar el modelo, se
# debe devolver (con raise) una excepción:

class ClasificadorNoEntrenado(Exception): pass

  
# Ejemplo "jugar al tenis": 


# >>> nb_tenis=NaiveBayesCat(k=0.5)
# >>> nb_tenis.entrena(X_tenis,y_tenis) 
# >>> ej_tenis=np.array(['Soleado','Baja','Alta','Fuerte'])
# >>> nb_tenis.clasifica_prob(ej_tenis)
# {'no': 0.7564841498559081, 'si': 0.24351585014409202}
# >>> nb_tenis.clasifica(ej_tenis)
# 'no'

# nb_tenis=NaiveBayesCat(k=0.5)
# nb_tenis.entrena(X_tenis,y_tenis) 
# ej_tenis=np.array(['Soleado','Baja','Alta','Fuerte'])
# print("Distribucion tenis:\n", nb_tenis.clasifica_prob(ej_tenis))
# print("Clasificacion tenis:\n", nb_tenis.clasifica(ej_tenis))


# Ejemplo de credito:
# Xe_credito,Xp_credito,ye_credito,yp_credito=particion_entr_prueba(X_credito,y_credito,test=0.4)
# nb_credito = NaiveBayesCat(k=1)
# nb_credito.entrena(Xe_credito,ye_credito)
# ej_bueno = ['laboral','dos','ninguna','tres','soltero','altos']
# ej_malo = ['laboral','cinco','ninguna','cinco','viudo','bajos']
# print("Distribucion 1 \n", nb_credito.clasifica_prob(ej_bueno))
# print("Clasificacion 1 \n", nb_credito.clasifica(ej_bueno))

# print("Distribucion 2 \n", nb_credito.clasifica_prob(ej_malo))
# print("Clasificacion 2 \n", nb_credito.clasifica(ej_malo))




# ----------------------------------------------
# 2.2) Implementación del cálculo de rendimiento
# ----------------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Definir una función "rendimiento(clasificador,X,y)" que devuelve la
# proporción de ejemplos bien clasificados (accuracy) que obtiene el
# clasificador sobre un conjunto de ejemplos X con clasificación esperada y. 

# Comentarip, no funcionaba comprar si era array y siempre estoy usando la misma funcion para arrays y no arrays como en la clase anterior
def rendimiento(clasificador,X,y):
    aciertos = 0
    for xi, yi in zip(X, y):
        pred = clasificador.clasifica(xi)

        # Caso de que la prediccion sea formato array
        if isinstance(pred, np.ndarray):
            if pred.ndim == 0:
                pred = pred.item() # si es array(pred)
            else:
                pred = pred[0]  # si es array([pred])
        
        if pred == yi:
            aciertos += 1
            
    return aciertos / len(y)

# Ejemplo:

# >>> rendimiento(nb_tenis,X_tenis,y_tenis)
# 0.9285714285714286

# print("Rendimiento nb en en tenis:\n", rendimiento(nb_tenis,X_tenis,y_tenis))



# -------------------------------------
# 2.3) Aplicando Naive Bayes categórico
# -------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Usando el clasificador Naive Bayes categórico implementado, 
# obtener clasificadores con el mejor rendimiento posible para los 
# siguientes conjunto de datos:

# - Votos de congresistas US
# - Concesión de prestamos
# - Críticas de películas en IMDB 

# En todos los casos, será necesario separar un conjunto de test para dar la
# valoración final de los clasificadores obtenidos (ya realizado en el ejerciio 
# anterior). Ajustar también el valor del parámetro de suavizado k, usando un 
# conjunto de validación. 

# Describir (dejándolo comentado) el proceso realizado en cada caso, 
# y los rendimientos obtenidos. 



# SOLUCION: 
# 1) Único hiperparametro a optimizar es el valor de suavizado k para cada dataset.       
# 2) Como los conjuntos de entrenamiento varía en cada ejecución, he ido recopilando las 5 últimas ejecuciones con los mejores resultados

            ### [*][*][*]   Votos de congresistas US   [*][*][*]
# Xe_votos,Xp_votos,ye_votos,yp_votos=particion_entr_prueba(X_votos,y_votos,test=0.2)
# Xent_votos,Xev_votos,yent_votos,yev_votos=particion_entr_prueba(Xe_votos,ye_votos,test=0.2)

# mejor_k = None
# mejor_val = 0
# for k in np.linspace(0.001,5,100):
#     nb_votos = NaiveBayesCat(k)
#     nb_votos.entrena(Xent_votos,yent_votos)
#     rendimiento_obtenido = rendimiento(nb_votos, Xev_votos,yev_votos)
#     if mejor_val < rendimiento_obtenido:
#         print(f"Para k={k} rendimiento={rendimiento_obtenido}")
#         mejor_val = rendimiento_obtenido
#         mejor_k = k

# print(f"Mejor rendimiento para Votos de congresistas US con k={mejor_k} y rendimiento {rendimiento(nb_votos, Xp_votos,yp_votos)}")
#>>> Mejor rendimiento para Votos de congresistas US con k=0.7079292929292929 y rendimiento 0.9204545454545454
#>>> Mejor rendimiento para Votos de congresistas US con k=0.001 y rendimiento 0.9772727272727273
#>>> Mejor rendimiento para Votos de congresistas US con k=0.001 y rendimiento 0.875
#>>> Mejor rendimiento para Votos de congresistas US con k=0.001 y rendimiento 0.9090909090909091
#>>> Mejor rendimiento para Votos de congresistas US con k=0.001 y rendimiento 0.8977272727272727

# Parece que el mejor k = 0.001, puede deberse a que ya hay suficientes datos y no necesita tanta regularización

            ### [*][*][*]  Concesión de prestamos   [*][*][*]
# Xe_credito,Xp_credito,ye_credito,yp_credito=particion_entr_prueba(X_credito,y_credito,test=0.2)
# Xent_credito,Xev_credito,yent_credito,yev_credito=particion_entr_prueba(Xe_credito,ye_credito,test=0.2)

# mejor_k = None
# mejor_val = 0
# for k in np.linspace(0.001,5,100):
#     nb_credito = NaiveBayesCat(k)
#     nb_credito.entrena(Xent_credito,yent_credito)
#     rendimiento_obtenido = rendimiento(nb_credito, Xev_credito,yev_credito)
#     if mejor_val < rendimiento_obtenido:
#         print(f"Para k={k} rendimiento={rendimiento_obtenido}")
#         mejor_val = rendimiento_obtenido
#         mejor_k = k

# print(f"Mejor rendimiento para concesión de prestamos con k={mejor_k} y rendimiento {rendimiento(nb_credito, Xp_credito,yp_credito)}")
#>>> Mejor rendimiento para concesión de prestamos con k=3.5356464646464643 y rendimiento 0.6259541984732825
#>>> Mejor rendimiento para concesión de prestamos con k=2.3237676767676763 y rendimiento 0.6870229007633588
#>>> Mejor rendimiento para concesión de prestamos con k=3.7881212121212116 y rendimiento 0.6412213740458015
#>>> Mejor rendimiento para concesión de prestamos con k=0.001 y rendimiento 0.6641221374045801
#>>> Mejor rendimiento para concesión de prestamos con k=2.98020202020202 y rendimiento 0.6717557251908397

# Parece que el mejor k = [2,3], puede deberse a que no hay suficientes datos y necesita tanta regularización


            ### [*][*][*]  Críticas de películas en IMDB    [*][*][*]
# Xp_imdb = X_test_imdb
# yp_imdb = y_test_imdb
# Xent_imdb,Xev_imdb,yent_imdb,yev_imdb=particion_entr_prueba(X_train_imdb,y_train_imdb,test=0.2)

# mejor_k = None
# mejor_val = 0
# for k in np.linspace(0.001,5,100):
#     nb_imdb = NaiveBayesCat(k)
#     nb_imdb.entrena(Xent_imdb,yent_imdb)
#     rendimiento_obtenido = rendimiento(nb_imdb, Xev_imdb,yev_imdb)
#     if mejor_val < rendimiento_obtenido:
#         print(f"Para k={k} rendimiento={rendimiento_obtenido}")
#         mejor_val = rendimiento_obtenido
#         mejor_k = k

# print(f"Mejor rendimiento para críticas de películas en IMDB con k={mejor_k} y rendimiento {rendimiento(nb_imdb, Xp_imdb,yp_imdb)}")
#>>> Mejor rendimiento para críticas de películas en IMDB con k=0.001 y rendimiento 0.78
#>>> Mejor rendimiento para críticas de películas en IMDB con k=2.2227777777777775 y rendimiento 0.7775
#>>> Mejor rendimiento para críticas de películas en IMDB con k=3.182181818181818 y rendimiento 0.79
#>>> Mejor rendimiento para críticas de películas en IMDB con k=1.8188181818181814 y rendimiento 0.8025
#>>> Mejor rendimiento para críticas de películas en IMDB con k=0.9604040404040403 y rendimiento 0.7975

# Parece que el mejor k = [1,2], en este caso hay mas variabilidad del tamaño de k y habría que estudiar mejor el motivo




# --------------------------------------------
# 2.4) Implementación de Naive Bayes gaussiano
# --------------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Definir una clase NaiveBayesGauss con la misma estructura que la descrita en 
# el apartado 2.1



class NaiveBayesGauss():

    def __init__(self):
        self.entrenado = False

    def entrena(self, X, y):

        self.clases = list(set(y))
        self.prob_a_priori = {}   # {clase: n(C=c)}
        self.medias = {}  # {clase: [mu_j para cada atributo j]}
        self.varianzas = {}  # {clase: [sigma^2_j para cada atributo j]}

        total = len(y)

        for c in self.clases:
            X_c = X[y == c]  # filas de la clase c
            self.prob_a_priori[c] = len(X_c) / total
            self.medias[c]    = np.mean(X_c, axis=0) # media por atributo
            self.varianzas[c] = np.var(X_c, axis=0) # varianza por atributo

        self.entrenado = True

    def _gauss(self, valor, media, varianza): #Definimos dist gaussina
        if varianza == 0:
            return 1.0 if valor == media else 0.0
        exponente = -((valor - media) ** 2) / (2 * varianza)
        return (1 / math.sqrt(2 * math.pi * varianza)) * math.exp(exponente)

    def clasifica_prob(self, ejemplo):
        if not self.entrenado:
            raise ClasificadorNoEntrenado("Llama a entrena() primero.")

        ejemplo = np.array(ejemplo, dtype=float)
        dist_prob = {}

        for clase in self.clases:
            # P(C=c) —> probabilidad a priori
            prob = self.prob_a_priori[clase]

            # P(Xj=vj | C=c) —> densidad gaussiana por atributo
            for j, valor in enumerate(ejemplo):
                prob *= self._gauss(valor, self.medias[clase][j],
                                          self.varianzas[clase][j])

            dist_prob[clase] = prob

        # Normalizar para que sumen 1
        suma = sum(dist_prob.values())
        return {c: p / suma for c, p in dist_prob.items()}

    def clasifica(self, ejemplo):
        if not self.entrenado:
            raise ClasificadorNoEntrenado("Llama a entrena() primero.")

        dist_prob = self.clasifica_prob(ejemplo)
        return max(dist_prob, key=dist_prob.get)


class ClasificadorNoEntrenado(Exception):
    pass










# ------------------------------------
# 2.5) Aplicando Naive Bayes gaussiano
# ------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]


# Aplicar el clasificador NaiveBayesGauss a los datos del cáncer de mama. 



          ### [*][*][*]  Cancer    [*][*][*]
# Xe_cancer,Xp_cancer,ye_cancer,yp_cancer=particion_entr_prueba(X_cancer,y_cancer,test=0.2)
# Xent_cancer,Xev_cancer,yent_cancer,yev_cancer=particion_entr_prueba(Xe_cancer,ye_cancer,test=0.2)


# nb_cancer = NaiveBayesGauss()
# nb_cancer.entrena(Xent_cancer,yent_cancer)

# print("X", np.shape(Xp_cancer))
# print("y", np.shape(yp_cancer))

# print(f"Rendimiento para cancer = {rendimiento(nb_cancer, Xp_cancer,yp_cancer)}")
# >>> Rendimiento para cancer = 0.9043478260869565








# ==================================
# EJERCICIO 3: NORMALIZADOR ESTÁNDAR
# ==================================
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Definir la siguiente clase que implemente la normalización "standard", es 
# decir aquella que traslada y escala cada característica para que tenga
# media 0 y desviación típica 1. 

# En particular, definir la clase: 


# class NormalizadorStandard():

#    def __init__(self):

#         .....
        
#     def ajusta(self,X):

#         .....        

#     def normaliza(self,X):

#         ......

# 


class NormalizadorStandard():

    def __init__(self):
        self.normalizacion = False

        
    def ajusta(self,X):
        self.media = np.mean(X, axis=0) 
        self.desviacion_estandar = np.std(X, axis=0)

        self.normalizacion = True
        


    def normaliza(self,X):
        if not self.normalizacion:
            raise NormalizadorNoAjustado("Llama a ajusta() primero.")
        
        X_norm = (X - self.media ) / (self.desviacion_estandar)
        return X_norm





# donde el método ajusta calcula las corresondientes medias y desviaciones típicas
# de las características de X necesarias para la normalización, y el método 
# normaliza devuelve el correspondiente conjunto de datos normalizados. 

# Si se llama al método de normalización antes de ajustar el normalizador, se
# debe devolver (con raise) una excepción:

class NormalizadorNoAjustado(Exception): pass


# Por ejemplo:
    
    
# >>> normst_cancer=NormalizadorStandard()
# >>> normst_cancer.ajusta(Xe_cancer)
# >>> Xe_cancer_n=normst_cancer.normaliza(Xe_cancer)
# >>> Xv_cancer_n=normst_cancer.normaliza(Xv_cancer)
# >>> Xp_cancer_n=normst_cancer.normaliza(Xp_cancer)

# Una vez realizado esto, la media y desviación típica de Xe_cancer_n deben ser 
# 0 y 1, respectivamente. No necesariamente ocurre lo mismo con Xv_cancer_n, 
# ni con Xp_cancer_n. 

# normst_cancer=NormalizadorStandard()
# normst_cancer.ajusta(Xe_cancer)
# Xe_cancer_n=normst_cancer.normaliza(Xe_cancer)
# Xv_cancer_n=normst_cancer.normaliza(Xev_cancer)
# Xp_cancer_n=normst_cancer.normaliza(Xp_cancer)

# print(f"Normalizacion entrenamiento\n{np.mean(Xe_cancer_n,axis=0)}\n{np.std(Xe_cancer_n,axis=0)}")
# print(f"Normalizacion prueba\n{np.mean(Xp_cancer_n,axis=0)}\n{np.std(Xp_cancer_n,axis=0)}")
# print(f"Normalizacion validacion\n{np.mean(Xv_cancer_n,axis=0)}\n{np.std(Xv_cancer_n,axis=0)}")
# ------ 





























# ==============================================================
# EJERCICIO 4: REGRESIÓN LOGÍSTICA MINI-BATCH CON REGULARIZACIÓN
# ==============================================================
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]


# En este ejercicio se propone la implementación de un clasificador lineal 
# binario basado en regresión logística (mini-batch), con algoritmo de entrenamiento 
# de descenso por el gradiente mini-batch (diapositiva 50 del tema 3). 
# Se pide también incluir regularización L2 (es decir, la función de
# pérdida a minimizar es la entropía cruzada más un sumando de regularización 
# cuadrática) 


# En concreto se pide implementar una clase: 

# class RegresionLogisticaMiniBatch():

#    def __init__(self,rate=0.1,rate_decay=False,n_epochs=100,
#                 batch_tam=64,reg=0.01):

#         .....
        
#     def entrena(self,X,y,Xv=None,yv=None,n_epochs=100,salida_epoch=False,
#                     early_stopping=False,paciencia=3):

#         .....        

#     def clasifica_prob(self,ejemplos):

#         ......
    
#     def clasifica(self,ejemplos):
                        
#          ......

# * Definir la función sigmoide usando la función expit de scipy.special, 
#   para evitar "warnings" por "overflow":

from scipy.special import expit    

def sigmoide(x):
    return expit(x)

# * Usar np.where para definir la entropía cruzada. 

class RegresionLogisticaMiniBatch():

    def __init__(self,rate=0.1,rate_decay=False,n_epochs=100,
                batch_tam=64,reg=0.01):
        self.rate = rate
        self.rate_decay = rate_decay
        self.batch_tam = batch_tam
        self.reg = reg
        self.entrenado = False

        
    def entrena(self,X,y,Xv=None,yv=None,n_epochs=100,salida_epoch=False,
                    early_stopping=False,paciencia=3):


        rate = self.rate
        total = len(X)

        if early_stopping:
            min_error = np.inf
            acum_paciencia = 0

        # Inicializamos pesos aleatorios y el sesgo
        self.pesos = np.random.randn(len(X[0])) 
        self.sesgo = 0
        self.entrenado = True

        self.clases = list(np.unique(y))
        y_binario = np.where(y == self.clases[1], 1, 0)

        if yv is not None:
            yv_bin = np.where(yv == self.clases[1], 1, 0)

        for epoca in range(n_epochs):
            # Recorrido aleatorio del conjunto de datos
            indices = np.arange(total)
            np.random.shuffle(indices)
            X_barajado = X[indices]
            y_barajado = y[indices]
            
            # Para cada batch
            for paso in range(0,total,self.batch_tam):
                X_batch = X_barajado[paso:paso+self.batch_tam]
                y_batch = y_barajado[paso:paso+self.batch_tam]

                # Actualizamos pesos y sesgo

                error = (y_batch - [sigmoide((np.dot(self.pesos,x) + self.sesgo)) for x in X_batch])
                gradiente =   np.dot(error,X_batch) 
                penalizacion = self.reg * self.pesos
                self.pesos = self.pesos + rate * (gradiente - 2 * penalizacion)

                self.sesgo = self.sesgo + rate * np.sum(error)
                

            # Calcular error
            if salida_epoch or early_stopping:
                # Prediccion para ent / val
                y_pred_ent = self.clasifica_prob(X)
                y_pred_v = self.clasifica_prob(Xv)

                # Clip para evitar log(0) cuando prediccion y = 0 o y=1 equivocada
                y_pred_ent = np.clip(y_pred_ent, 1e-15, 1 - 1e-15)
                y_pred_v = np.clip(y_pred_v, 1e-15, 1 - 1e-15)

                # Usamos np.where para separar casos y=1 e y=0
                perdida_por_muestra_ent = np.where(
                    y_binario == 1,
                    -np.log(y_pred_ent), # y=1: -log(ŷ)
                    -np.log(1 - y_pred_ent) # y=0: -log(1-ŷ)
                )

                perdida_por_muestra_val = np.where(
                    yv_bin == 1,
                    -np.log(y_pred_v), # y=1: -log(ŷ)
                    -np.log(1 - y_pred_v) # y=0: -log(1-ŷ)
                )

                penalizacion = self.reg * np.dot(self.pesos, self.pesos)
                perdida_ent = np.sum(perdida_por_muestra_ent) + penalizacion
                perdida_val = np.sum(perdida_por_muestra_val) + penalizacion

                aciertos_ent = np.mean(self.clasifica(X) == y)
                aciertos_val = np.mean(self.clasifica(Xv) == yv)

                if salida_epoch:
                    print(f"Época {epoca+1}:")
                    print(f"\npérdida entrenamiento = {perdida_ent:.4f} | aciertos entrenamiento = {aciertos_ent}")
                    print(f"\npérdida validación = {perdida_val:.4f} | aciertos validación = {aciertos_val}")

                if early_stopping:
                    if perdida_val < min_error:
                        min_error = perdida_val
                        acum_paciencia = 0
                    else:
                        acum_paciencia += 1
                    if acum_paciencia >= paciencia:
                        print(f"Early stopping en época {epoca+1}")
                        break
                    


            if self.rate_decay:
                rate =  (rate)*(1/(1+epoca))
            

    def clasifica_prob(self, ejemplos):
        if not self.entrenado:
            raise ClasificadorNoEntrenado("El clasificador no ha sido entrenado. Llama a entrena() primero.")
        

        probabilidades = ejemplos @ self.pesos + self.sesgo
        return sigmoide(probabilidades)


    def clasifica(self, ejemplos):
        if not self.entrenado:
            raise ClasificadorNoEntrenado("El clasificador no ha sido entrenado. Llama a entrena() primero.")
        
        probs = self.clasifica_prob(ejemplos)

        # Convertimos a 1 si prob >= 0.5, si no 0
        etiquetas_binarias = (probs >= 0.5).astype(int)

        # Mapear 0/1 a clases originales
        clase_neg, clase_pos = self.clases[0], self.clases[1]
        return np.where(etiquetas_binarias == 1, clase_pos, clase_neg)





# * El constructor tiene los siguientes argumentos de entrada:



#   + rate: si rate_decay es False, rate es la tasa de aprendizaje fija usada
#     durante todo el aprendizaje. Si rate_decay es True, rate es la
#     tasa de aprendizaje inicial. Su valor por defecto es 0.1.

#   + rate_decay, indica si la tasa de aprendizaje debe disminuir en
#     cada epoch. En concreto, si rate_decay es True, la tasa de
#     aprendizaje que se usa en el n-ésimo epoch se debe de calcular
#     con la siguiente fórmula: 
#        rate_n= (rate_0)*(1/(1+n)) 
#     donde n es el número de epoch, y rate_0 es la cantidad introducida
#     en el parámetro rate anterior. Su valor por defecto es False. 
#  
#   + batch_tam: tamaño de minibatch
#    
#   + reg: constante de regularización L2

# * El método entrena tiene como argumentos de entrada:
#   
#     +  Dos arrays numpy X e y, con los datos del conjunto de entrenamiento 
#        y su clasificación esperada, respectivamente. Las dos clases del problema 
#        son las que aparecen en el array y, y se deben almacenar en un atributo 
#        self.clases en una lista. La clase que se considera positiva es la que 
#        aparece en segundo lugar en esa lista.
#     
#     + Otros dos arrays Xv,yv, con los datos del conjunto de  validación, que se 
#       usarán en el caso de activar el parámetro early_stopping. Ambos con 
#       valor None por defecto. 

#     + n_epochs es el número máximo de epochs en el entrenamiento. 

#     + salida_epoch (False por defecto). Si es True, al inicio y durante el 
#       entrenamiento, cada epoch se imprime  el valor de la entropía cruzada 
#       del modelo respecto del conjunto de entrenamiento, más la penalización L2, 
#       y su rendimiento (proporción de aciertos). Igualmente para el conjunto 
#       de validación, si lo hubiera. Esta opción puede ser útil para comprobar 
#       si el entrenamiento  efectivamente está haciendo descender la función 
#       de pérdida del modelo (recordemos que el objetivo del entrenamiento es 
#       encontrar los pesos que minimizan la función de pérdida), y está haciendo 
#       subir el rendimiento.
# 
#     + early_stopping (booleano, False por defecto) y paciencia (entero, 3 por defecto).
#       Si early_stopping es True, dejará de entrenar cuando lleve un número de
#       epochs igual a paciencia sin disminuir la menor pérdida conseguida hasta el momento
#       en el conjunto de validación 
#       NOTA: esto se suele hacer con un conjunto de validación, y mecanismo de 
#       "callback" para recuperar el mejor modelo, pero por simplificar implementaremos
#       esta versión más sencilla.  
#        



# * Método clasifica: recibe UN ARRAY de ejemplos (array numpy) y
#   devuelve el ARRAY de clases que el modelo predice para esos ejemplos. 

# * Un método clasifica_prob, que recibe UN ARRAY de ejemplos (array numpy) y
#   devuelve el ARRAY con las probabilidades que el modelo 
#   asigna a cada ejemplo de pertenecer a la clase positiva.       
    


# Si se llama a los métodos de clasificación antes de entrenar el modelo, se
# debe devolver (con raise) una excepción:


class ClasificadorNoEntrenado(Exception): pass

        
  

# RECOMENDACIONES: 


# + IMPORTANTE: Siempre que se pueda, tratar de evitar bucles for para recorrer 
#   los datos, usando en su lugar funciones de numpy. La diferencia en eficiencia
#   es muy grande. 

# + Téngase en cuenta que el cálculo de la función de pérdida no es necesario
#   para el entrenamiento, aunque si salida_epoch o early_stopping es True,
#   entonces si es necesario su cálculo. Tenerlo en cuenta para no calcularla
#   cuando no sea necesario.     

# * Definir la función sigmoide usando la función expit de scipy.special, 
#   para evitar "warnings" por "overflow":

#   from scipy.special import expit    
#
#   def sigmoide(x):
#      return expit(x)

# * Usar np.where para definir la entropía cruzada. 

# -------------------------------------------------------------

# Ejemplo, usando los datos del cáncer de mama (los resultados pueden variar):


# >>> lr_cancer=RegresionLogisticaMiniBatch(rate=0.1,rate_decay=True)

# >>> lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xv_cancer,yv_cancer)

# >>> lr_cancer.clasifica(Xp_cancer_n[24:27])
# array([0, 1, 0])   # Predicción para los ejemplos 24,25 y 26 

# >>> yp_cancer[24:27]
# array([0, 1, 0])   # La predicción anterior coincide con los valores esperado para esos ejemplos

# >>> lr_cancer.clasifica_prob(Xp_cancer_n[24:27])
# array([7.44297196e-17, 9.99999477e-01, 1.98547117e-18])

# Xen_cancer,Xp_cancer,yen_cancer,yp_cancer = particion_entr_prueba(X_cancer,y_cancer)
# Xe_cancer,Xev_cancer,ye_cancer,yev_cancer = particion_entr_prueba(Xen_cancer,yen_cancer)


# Xe_cancer_n = normst_cancer.normaliza(Xe_cancer)
# Xev_cancer_n = normst_cancer.normaliza(Xev_cancer)
# Xp_cancer_n = normst_cancer.normaliza(Xp_cancer)

# lr_cancer=RegresionLogisticaMiniBatch(rate=0.1,rate_decay=True)

# lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xev_cancer_n,yev_cancer,salida_epoch = False)

# print(lr_cancer.clasifica(Xp_cancer_n[24:27]))

# print(f"Clasificación de ejempplos para cancer{lr_cancer.clasifica(Xp_cancer_n[24:27])}\n Con valor real {yp_cancer[24:27]}")

# print(f"Rendimiento para cancer = {rendimiento(lr_cancer, Xp_cancer_n,yp_cancer)}")

# Por ejemplo, los rendimientos sobre los datos (normalizados) del cáncer:
    
# >>> rendimiento(lr_cancer,Xe_cancer_n,ye_cancer)
# 0.9824561403508771

# >>> rendimiento(lr_cancer,Xp_cancer_n,yp_cancer)
# 0.9734513274336283



# Ejemplo con salida_epoch y early_stopping:

# >>> lr_cancer=RegresionLogisticaMiniBatch(rate=0.1,rate_decay=True,reg=0.001)

# >>> lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xv_cancer_n,yv_cancer,salida_epoch=True,early_stopping=True)

# Inicialmente, en entrenamiento LOSS: 155.686323940485, rendimiento: 0.873972602739726.
# Inicialmente, en validación    LOSS: 43.38533009881579, rendimiento: 0.8461538461538461.
# Epoch 1, en entrenamiento LOSS: 32.7750241863029, rendimiento: 0.9753424657534246.
#          en validación    LOSS: 8.4952918658522,  rendimiento: 0.978021978021978.
# Epoch 2, en entrenamiento LOSS: 28.0583715052223, rendimiento: 0.9780821917808219.
#          en validación    LOSS: 8.665719133490596, rendimiento: 0.967032967032967.
# Epoch 3, en entrenamiento LOSS: 26.857182744289368, rendimiento: 0.9780821917808219.
#          en validación    LOSS: 8.09511082759361, rendimiento: 0.978021978021978.
# Epoch 4, en entrenamiento LOSS: 26.120803184993328, rendimiento: 0.9780821917808219.
#          en validación    LOSS: 8.327991940213478, rendimiento: 0.967032967032967.
# Epoch 5, en entrenamiento LOSS: 25.66005010760342, rendimiento: 0.9808219178082191.
#          en validación    LOSS: 8.376171724729662, rendimiento: 0.967032967032967.
# Epoch 6, en entrenamiento LOSS: 25.329200890122557, rendimiento: 0.9808219178082191.
#          en validación    LOSS: 8.408704771704937, rendimiento: 0.967032967032967.
# PARADA TEMPRANA

# Nótese que para en el epoch 6 ya que desde la pérdida obtenida en el epoch 3 
# sobre el conjunto de validación, ésta no se ha mejorado. 


# lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xev_cancer_n,yev_cancer,salida_epoch=True,early_stopping=True)

# -----------------------------------------------------------------























# ===================================================
# EJERCICIO 5: APLICANDO LOS CLASIFICADORES BINARIOS
# ===================================================
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]



# Usando la regeresión logística implementada en el ejercicio 2, obtener clasificadores 
# con el mejor rendimiento posible para los siguientes conjunto de datos:

# - Votos de congresistas US
# - Cáncer de mama 
# - Críticas de películas en IMDB

# Ajustar los parámetros (tasa, rate_decay, batch_tam,reg) para mejorar el rendimiento 
# (no es necesario ser muy exhaustivo, tan solo probar algunas combinaciones). 
# Usar para ello un conjunto de validación. 

# Dsctbir el proceso realizado en cada caso, y los rendimientos finales obtenidos
# sobre un conjunto de prueba (dejarlo todo como comentario)     







# SOLUCION: 
# Como no es necesario que el ajuste sea exhaustivo, simplemente vamos a probar con algunas combinaciones (si se quisiera mejorar, tan solo faltaría aumentar los posibles parámetros)
# 1) Vamos a probar con 3 tamaños distintos de batch (grande, "normal", pequeño)
# 2) Vamos a probar con o sin decay 
# 3) Vamos a probar con 3 tasas de aprendizaje (alta = 0.8, "normal" = 0.1, baja = 0.0125)
# 4) Vamos a probar con 3 parametros de regularizacion (bajo = 0.001, normal = 0.01, alto = 0.1)

            ### [*][*][*]   Votos de congresistas US   [*][*][*]
# Xe_votos,Xp_votos,ye_votos,yp_votos=particion_entr_prueba(X_votos,y_votos,test=0.2)
# Xent_votos,Xev_votos,yent_votos,yev_votos=particion_entr_prueba(Xe_votos,ye_votos,test=0.2)


# normst_votos = NormalizadorStandard()
# normst_votos.ajusta(Xent_votos)

# Xent_votos_n = normst_votos.normaliza(Xent_votos)
# Xev_votos_n = normst_votos.normaliza(Xev_votos)
# Xp_votos_n = normst_votos.normaliza(Xp_votos)

# tasa_lista = [0.0125, 0.1, 0.8] #por defecto y */ 8

# decay_lista = [False, True] # desactivado/activado

# batchtam_lista = [32, 64, 128] 

# reg_lista = [0.001, 0.01, 0.1] #por defecto y */ 10

# mejor_val = 0
# mejores_params = {}
# for tasa in tasa_lista:
#     for decay in decay_lista:
#         for batch in batchtam_lista:
#             for reg in reg_lista:
#                 lr_votos=RegresionLogisticaMiniBatch(rate=tasa, rate_decay = decay, batch_tam=batch, reg = reg)
#                 lr_votos.entrena(Xent_votos_n,yent_votos)

#                 rendimiento_obtenido = rendimiento(lr_votos, Xev_votos_n,yev_votos)
#                 if mejor_val < rendimiento_obtenido:
#                     mejor_val = rendimiento_obtenido
#                     mejores_params = {"rate": tasa, "rate_decay": decay, "batch_tam": batch, "reg_lista": reg}
#                     print(f"Para {mejores_params} rendimiento={rendimiento_obtenido}")

# print(f"Mejor rendimiento para Votos de congresistas US con {mejores_params} y rendimiento {rendimiento(lr_votos, Xp_votos_n,yp_votos)}")

#>>> Mejor rendimiento para Votos de congresistas US con {'rate': 0.1, 'rate_decay': True, 'batch_tam': 64, 'reg_lista': 0.01} y rendimiento 0.9659090909090909
#>>> Mejor rendimiento para Votos de congresistas US con {'rate': 0.8, 'rate_decay': False, 'batch_tam': 128, 'reg_lista': 0.01} y rendimiento 0.9772727272727273
#>>> Mejor rendimiento para Votos de congresistas US con {'rate': 0.1, 'rate_decay': False, 'batch_tam': 64, 'reg_lista': 0.1} y rendimiento 0.9659090909090909


# Obtenemos un rendimiento bastante bueno, indiferentemente de las combiaciones de rate, con o sin decrecimiento, con valor del batch y regularizacion medio/alto (se podría tratar de afinar más pero aumentan las combinaciones nºrate x nºbatch x 2)

            ### [*][*][*]  Cancer   [*][*][*]
# Xe_cancer,Xp_cancer,ye_cancer,yp_cancer=particion_entr_prueba(X_cancer,y_cancer,test=0.2)
# Xent_cancer,Xev_cancer,yent_cancer,yev_cancer=particion_entr_prueba(Xe_cancer,ye_cancer,test=0.2)

# normst_cancer = NormalizadorStandard()
# normst_cancer.ajusta(Xent_cancer)

# Xent_cancer_n = normst_cancer.normaliza(Xent_cancer)
# Xev_cancer_n = normst_cancer.normaliza(Xev_cancer)
# Xp_cancer_n = normst_cancer.normaliza(Xp_cancer)

# tasa_lista = [0.0125, 0.1, 0.8] #por defecto y */ 8

# decay_lista = [False, True] # desactivado/activado

# batchtam_lista = [32, 64, 128] #por defecto y */ 8

# reg_lista = [0.001, 0.01, 0.1] #por defecto y */ 10

# mejor_val = 0
# mejores_params = {}
# for tasa in tasa_lista:
#     for decay in decay_lista:
#         for batch in batchtam_lista:
#             for reg in reg_lista:
#                 lr_cancer=RegresionLogisticaMiniBatch(rate=tasa, rate_decay = decay, batch_tam=batch, reg = reg)
#                 lr_cancer.entrena(Xent_cancer_n,yent_cancer)

#                 rendimiento_obtenido = rendimiento(lr_cancer, Xev_cancer_n,yev_cancer)
#                 if mejor_val < rendimiento_obtenido:
#                     mejor_val = rendimiento_obtenido
#                     mejores_params = {"rate": tasa, "rate_decay": decay, "batch_tam": batch, "reg_lista": reg}
#                     print(f"Para {mejores_params} rendimiento={rendimiento_obtenido}")

# print(f"Mejor rendimiento para cancer con {mejores_params} y rendimiento {rendimiento(lr_cancer, Xp_cancer_n,yp_cancer)}")

#>>> Mejor rendimiento para cancer con {'rate': 0.0125, 'rate_decay': False, 'batch_tam': 64, 'reg_lista': 0.01} y rendimiento 0.9652173913043478
#>>> Mejor rendimiento para cancer con {'rate': 0.0125, 'rate_decay': False, 'batch_tam': 128, 'reg_lista': 0.001} y rendimiento 0.9391304347826087
#>>> Mejor rendimiento para cancer con {'rate': 0.0125, 'rate_decay': False, 'batch_tam': 32, 'reg_lista': 0.01} y rendimiento 0.9826086956521739

# También logramos rendimiento elevado, con un rate bajo (ajuste mas fino), sin decrecimiento de la tase, cualquier combinacion de batch y regularización medio/bajo


            ### [*][*][*]  Críticas de películas en IMDB    [*][*][*]
# Xp_imdb = X_test_imdb
# yp_imdb = y_test_imdb
# Xent_imdb,Xev_imdb,yent_imdb,yev_imdb=particion_entr_prueba(X_train_imdb,y_train_imdb,test=0.2)

# normst_imdb = NormalizadorStandard()
# normst_imdb.ajusta(Xent_imdb)

# Xent_imdb_n = normst_imdb.normaliza(Xent_imdb)
# Xev_imdb_n = normst_imdb.normaliza(Xev_imdb)
# Xp_imdb_n = normst_imdb.normaliza(Xp_imdb)

# tasa_lista = [0.0125, 0.1, 0.8] #por defecto y */ 8

# decay_lista = [False, True] # desactivado/activado

# batchtam_lista = [32, 64, 128] #por defecto y */ 8

# reg_lista = [0.001, 0.01, 0.1] #por defecto y */ 10

# mejor_val = 0
# mejores_params = {}
# for tasa in tasa_lista:
#     for decay in decay_lista:
#         for batch in batchtam_lista:
#             for reg in reg_lista:
#                 lr_imdb=RegresionLogisticaMiniBatch(rate=tasa, rate_decay = decay, batch_tam=batch, reg = reg)
#                 lr_imdb.entrena(Xent_imdb_n,yent_imdb)

#                 rendimiento_obtenido = rendimiento(lr_imdb, Xev_imdb_n,yev_imdb)
#                 if mejor_val < rendimiento_obtenido:
#                     mejor_val = rendimiento_obtenido
#                     mejores_params = {"rate": tasa, "rate_decay": decay, "batch_tam": batch, "reg_lista": reg}
#                     print(f"Para {mejores_params} rendimiento={rendimiento_obtenido}")

# print(f"Mejor rendimiento para imdb con {mejores_params} y rendimiento {rendimiento(lr_imdb, Xp_imdb_n,yp_imdb)}")

#>>> Mejor rendimiento para imdb con {'rate': 0.0125, 'rate_decay': False, 'batch_tam': 32, 'reg_lista': 0.1} y rendimiento 0.735
#>>> Mejor rendimiento para imdb con {'rate': 0.8, 'rate_decay': True, 'batch_tam': 32, 'reg_lista': 0.001} y rendimiento 0.73
#>>> Mejor rendimiento para imdb con {'rate': 0.8, 'rate_decay': True, 'batch_tam': 64, 'reg_lista': 0.01} y rendimiento 0.7675

# Este ejemplo obtiene el peor rendimiento, aunque parece que con una tasa de crecimiento alta mayoritariamente, tamaño del batch medio/bajo y combinaciones con todas las penalizaciones



























# =====================================================
# EJERCICIO 6: CLASIFICACIÓN MULTICLASE CON ONE vs REST
# =====================================================
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Se pide implementar un algoritmo de regresión logística para problemas de
# clasificación en los que hay más de dos clases, usando  la técnica One vs Rest. 


#  Para ello, implementar una clase  RL_OvR con la siguiente estructura, y que 
#  implemente un clasificador OvR (one versus rest) usando como base el
#  clasificador binario RegresionLogisticaMiniBatch


# class RL_OvR():

#     def __init__(self,rate=0.1,rate_decay=False,
#                   batch_tam=64,reg=0.01):

#        ......

#     def entrena(self,X,y,n_epochs=100,salida_epoch=False):

#        .......

#     def clasifica(self,ejemplos):

#        ......
            
class RL_OvR():

    def __init__(self, rate=0.1, rate_decay=False, batch_tam=64, reg=0.01):
        self.rate = rate
        self.rate_decay = rate_decay
        self.batch_tam = batch_tam
        self.reg = reg
        self.entrenado = False

    def entrena(self, X, y, n_epochs=100, salida_epoch=False):
        # Guardar lista de clases
        self.clases = list(np.unique(y))

        # Diccionario: clase -> modelo binario
        self.modelos = {}

        # Para cada clase, entrenar un modelo one-vs-rest
        for c in self.clases:
            # y_bin = 1 si y == c, si no 0
            y_bin = (y == c).astype(int)

            # Crear modelo binario 
            modelo = RegresionLogisticaMiniBatch(rate=self.rate,rate_decay=self.rate_decay,batch_tam=self.batch_tam,reg=self.reg)

            # Entrenar modelo uno-vs-rest
            modelo.entrena(X, y_bin, n_epochs=n_epochs, salida_epoch=salida_epoch)

            # Guardar modelo asociado a la clase c
            self.modelos[c] = modelo

        self.entrenado = True

    def clasifica(self,ejemplos):
        if not self.entrenado:
            raise ClasificadorNoEntrenadoRL_OvR("Llama a la función entrena() primero")
        
        # Queremos una matriz (n_ejemplos x n_clases) con prob de cada clase
        n_ejemplos = ejemplos.shape[0]
        n_clases = len(self.clases)
        probs = np.zeros((n_ejemplos, n_clases))
        for idx, clase in enumerate(self.clases):
            modelo = self.modelos[clase]
            probs[:,idx] = modelo.clasifica_prob(ejemplos)

        idx_max = np.argmax(probs,axis=1) #mayor probabilidad
        clasificacion = np.array(self.clases)[idx_max]
        return clasificacion



       


class ClasificadorNoEntrenadoRL_OvR(Exception): pass

#  Los parámetros de los métodos significan lo mismo que en el apartado
#  anterior, aunque ahora referido a cada uno de los k entrenamientos a 
#  realizar (donde k es el número de clases) (
#  Por simplificar, supondremos que no hay conjunto de validación ni parada
#  temprana.  

 

#  Un ejemplo de sesión, con el problema del iris:



# --------------------------------------------------------------------
# >>> Xe_iris,Xp_iris,ye_iris,yp_iris=particion_entr_prueba(X_iris,y_iris)

# Xe_iris,Xp_iris,ye_iris,yp_iris=particion_entr_prueba(X_iris,y_iris)

# >>> rl_iris_ovr=RL_OvR(rate=0.001,batch_tam=8)

# rl_iris_ovr=RL_OvR(rate=0.001,batch_tam=8)

# >>> rl_iris_ovr.entrena(Xe_iris,ye_iris)

# rl_iris_ovr.entrena(Xe_iris,ye_iris)

# >>> rendimiento(rl_iris_ovr,Xe_iris,ye_iris)
# 0.8333333333333334

# print(rendimiento(rl_iris_ovr,Xe_iris,ye_iris))

# >>> rendimiento(rl_iris_ovr,Xp_iris,yp_iris)
# >>> 0.9
# --------------------------------------------------------------------




















# =====================================================
# EJERCICIO 7: APLICANDO LOS CLASIFICADORES MULTICLASE
# =====================================================
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]


# -------------------------
# 7.1) Codificación one-hot
# -------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Los conjuntos de datos en los que algunos atributos son categóricos (es decir,
# sus posibles valores no son numéricos, o aunque sean numéricos no hay una 
# relación natural de orden entre los valores) no se pueden usar directamente
# con los modelos de regresión logística, o con redes neuronales, por ejemplo.

# En ese caso es usual transformar previamente los datos usando la llamada
# "codificación one-hot". Básicamente, cada columna se reemplaza por k columnas
# en los que los valores psoibles son 0 o 1, y donde k es el número de posibles 
# valores del atributo. El valor i-ésimo del atributo se convierte en k atributos
# (0 ...0 1 0 ...0 ) donde todas las posiciones son cero excepto la i-ésima.  

# Por ejemplo, sin un atributo tiene tres posibles valores "a", "b" y "c", ese atributo 
# se reemplazaría por tres atributos binarios, con la siguiente codificación:
# "a" --> (1 0 0)
# "b" --> (0 1 0)
# "c" --> (0 0 1)    

# Definir una función:    
    
#     codifica_one_hot(X) 

def codifica_one_hot(X):
    n_muestras, n_atributos = X.shape

    valores_por_atrib = []
    tam_por_atrib = []
    total_dim = 0
    # Guardamos los distintos valores diferntes para cada atributos
    for j in range(n_atributos):
        vals = np.unique(X[:, j])
        valores_por_atrib.append(list(vals))
        tam_por_atrib.append(len(vals))
        total_dim += len(vals) # Nueva dimension de columnas

    X_one_hot = np.zeros((n_muestras,total_dim), dtype=float)
    for idx_muestra, x in enumerate(X):
        x_one_hot = []
        for idx_atributo, atributo in enumerate(x):
                lista_booleana = [ atributo == valor for valor in valores_por_atrib[idx_atributo]] # True solo en el atributo posicion correcta
                x_one_hot.extend(lista_booleana) # Extendemos cada columnna con la representacion one-hot en booleano
        X_one_hot[idx_muestra, :] = np.array(x_one_hot, dtype=float) # Añadimos a nuestra representacion X one-hot de la nueva instancia  
    
    return(np.array(X_one_hot))
    


# que recibe un conjunto de datos X (array de numpy) y devuelve un array de numpy
# resultante de aplicar la codificación one-hot a X.Por simplificar supondremos 
# que el array de entrada tiene todos sus atributos categóricos, y que por tanto 
# hay que codificarlos todos.

# NOTA: NO USAR PANDAS NI SKLEARN PARA ESTA FUNCIÓN

# Aplicar la función para obtener una codificación one-hot de los datos sobre
# concesión de prestamo bancario.     
  
# Xc=np.array([["a",1,"c","x"],
#                  ["b",2,"c","y"],
#                  ["c",1,"d","x"],
#                  ["a",2,"d","z"],
#                  ["c",1,"e","y"],
#                  ["c",2,"f","y"]])

# X_one_hot = codifica_one_hot(Xc)

# print(X_one_hot)

# print(type(X_one_hot))
# print(X_one_hot.shape)

# >>> codifica_one_hot(Xc)
# 
# array([[1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0.],
#        [0., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 0.],
#        [0., 0., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0.],
#        [1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 1.],
#        [0., 0., 1., 1., 0., 0., 0., 1., 0., 0., 1., 0.],
#        [0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 1., 0.]])

# En este ejemplo, cada columna del conjuto de datos original se transforma en:
#   * Columna 0 ---> Columnas 0,1,2
#   * Columna 1 ---> Columnas 3,4
#   * Columna 2 ---> Columnas 5,6,7,8
#   * Columna 3 ---> Columnas 9, 10,11     

    
  

























# ---------------------------------------------------------
# 7.2) Conjunto de datos de la concesión de crédito
# ---------------------------------------------------------
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]
#       [*][*][*]   COMPLETADO   [*][*][*]

# Aplicar la implementación OvR del ejercicio anterior y la de one-hot del
# apartado anterior, para obtener un clasificador que aconseje la concesión, 
# estudio o no concesión de un préstamo, basado en los datos X_credito, y_credito. 

# Ajustar adecuadamente los parámetros (nuevamente, no es necesario ser demasiado 
# exhaustivo). Describirlo en los comentarios. 


# # # SOLUCIóN
            ### [*][*][*]  prestamo bancario    [*][*][*]
# X_credito_hot = codifica_one_hot(X_credito)
# Xe_credito_hot,Xp_credito_hot,ye_credito_hot,yp_credito_hot=particion_entr_prueba(X_credito_hot,y_credito,test=0.2)
# Xent_credito_hot,Xev_credito_hot,yent_credito_hot,yev_credito_hot=particion_entr_prueba(Xe_credito_hot,ye_credito_hot,test=0.2)

# tasa_lista = [0.0125, 0.1, 0.8] #por defecto y */ 8

# decay_lista = [False, True] # desactivado/activado

# batchtam_lista = [32, 64, 128] #por defecto y */ 8

# mejor_val = 0
# mejores_params = {}


# for tasa in tasa_lista:
#     for decay in decay_lista:
#         for batch in batchtam_lista:
#             lr_OvR_credito_hot=RL_OvR(rate=tasa, rate_decay = decay, batch_tam=batch)
#             lr_OvR_credito_hot.entrena(Xent_credito_hot,yent_credito_hot)

#             rendimiento_obtenido = rendimiento(lr_OvR_credito_hot, Xev_credito_hot,yev_credito_hot)
#             if mejor_val < rendimiento_obtenido:
#                 mejor_val = rendimiento_obtenido
#                 mejores_params = {"rate": tasa, "rate_decay": decay, "batch_tam": batch}
#                 print(f"Para {mejores_params} rendimiento={rendimiento_obtenido}")

# print(f"Mejores parametros: {mejores_params} y rendimiento: {rendimiento(lr_OvR_credito_hot, Xp_credito_hot,yp_credito_hot)}")


#>>> Mejores parametros: {'rate': 0.8, 'rate_decay': True, 'batch_tam': 64} y rendimiento: 0.7862595419847328
#>>> Mejores parametros: {'rate': 0.8, 'rate_decay': True, 'batch_tam': 128} y rendimiento: 0.7709923664122137
#>>> Mejores parametros: {'rate': 0.1, 'rate_decay': False, 'batch_tam': 64} y rendimiento: 0.7251908396946565
# Rendimiento peor al de los otros ejemplos, tamaño batch y rate medio/alto



# ---------------------------------------------------------
# 7.3) Clasificación de imágenes de dígitos escritos a mano
# ---------------------------------------------------------


#  Aplicar la implementación OvR del ejercicio anterior, para obtener un
#  clasificador que prediga el dígito que se ha escrito a mano y que se
#  dispone en forma de imagen pixelada, a partir de los datos que están en la 
#  carpeta datos/digitdata que se suministra.  Cada imagen viene dada por 28x28
#  píxeles, y cada pixel vendrá representado por un caracter "espacio en
#  blanco" (pixel blanco) o los caracteres "+" (borde del dígito) o "#"
#  (interior del dígito). En nuestro caso trataremos ambos como un pixel negro
#  (es decir, no distinguiremos entre el borde y el interior). En cada
#  conjunto las imágenes vienen todas seguidas en un fichero de texto, y las
#  clasificaciones de cada imagen (es decir, el número que representan) vienen
#  en un fichero aparte, en el mismo orden. Será necesario, por tanto, definir
#  funciones python que lean esos ficheros y obtengan los datos en el mismo
#  formato numpy en el que los necesita el clasificador. 

#  Los datos están ya separados en entrenamiento, validación y prueba. 

# Se pide:
    
# * Definir las funciones auxiliares necesarias para cargar el dataset desde los 
#   archivos de texto, y crear variables:
#       X_entr_dg, y_entr_dg
#       X_val_dg, y_val_dg
#       X_test_dg, y_test_dg
#   que contengan arrays de numpy con el dataset proporcionado (USAR ESOS NOMBRES).  

# * Obtener un modelo de clasificación RL_OvR    

# * Ajustar los parámetros de tamaño de batch, tasa de aprendizaje, constante de
#   regulrización y rate_decay para tratar de obtener un rendimiento aceptable 
#   (por encima del 75% de aciertos sobre test). 


def _carga_imagenes_ascii(path_imagenes, n_imagenes):
    # Cargamos las imágenes en formato ascii y devolvemos un array (n_imagenes, ancho*alto)
    # de modo que valores 0 (si ' ') o 1 (si '+' o '#') 

    # imagenes 28x28
    ancho = 28
    alto = 28
    X = np.zeros((n_imagenes, ancho * alto), dtype=float)
    with open(path_imagenes, 'r') as f:
        for i in range(n_imagenes):
            pixels = []
            for _ in range(alto):
                linea = f.readline()
                linea = linea.rstrip('\n')
                for ch in linea:
                    if ch == ' ':
                        pixels.append(0.0)
                    else: # (si '+' o '#') 
                        pixels.append(1.0)
            X[i, :] = np.array(pixels)
    return X


def _carga_labels_ascii(path_labels):
    # Cargamos las etiquetas de dígitos desde el fichero de texto, una por línea.
    labels = []
    with open(path_labels, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea != '':
                labels.append(int(linea))
    return np.array(labels)


def carga_dataset_digitos(base_path="datos/digitdata/"):
    import os

    # Entrenamiento
    path_train_img = os.path.join(base_path, "trainingimages")
    path_train_lab = os.path.join(base_path, "traininglabels")
    y_train = _carga_labels_ascii(path_train_lab)
    X_train = _carga_imagenes_ascii(path_train_img, len(y_train))

    # Validación
    path_val_img = os.path.join(base_path, "validationimages")
    path_val_lab = os.path.join(base_path, "validationlabels")
    y_val = _carga_labels_ascii(path_val_lab)
    X_val = _carga_imagenes_ascii(path_val_img, len(y_val))

    # Test
    path_test_img = os.path.join(base_path, "testimages")
    path_test_lab = os.path.join(base_path, "testlabels")
    y_test = _carga_labels_ascii(path_test_lab)
    X_test = _carga_imagenes_ascii(path_test_img, len(y_test))

    # Variables globales como pide el enunciado
    global X_entr_dg, y_entr_dg, X_val_dg, y_val_dg, X_test_dg, y_test_dg
    X_entr_dg, y_entr_dg = X_train, y_train
    X_val_dg, y_val_dg = X_val, y_val
    X_test_dg, y_test_dg = X_test, y_test


# SOLUCIÓN:
# Tarda mucho más que el resto de metodos, como tiene sentido, por lo que no he realizado una busqueda más exhaustiva ()

carga_dataset_digitos()

# tasa_lista = [0.0125, 0.1, 0.8] # Muy bajo 0.001, normal 0.01 y alto 0.8 

# decay_lista = [False, True] # desactivado/activado

# batchtam_lista = [32, 64, 128] # tamaño menor, normal y mayor

# # No vamos a añdir reg_lista = [0.001, 0.01, 0.1] ya que con lo anterior superamos 75% y tendriamos que buscar x3 combinaciones

# # regularizacion por defecto, se podria haber evitado hacer division tan grande de rates y probar con alguna regularizacion

# mejor_val = 0
# mejores_params = {}

# acum = 0
# for tasa in tasa_lista:
#     for decay in decay_lista:
#         for batch in batchtam_lista:
#             acum +=1
#             print(f"Vuelta {acum}")
#             lr_OvR_dg_hot=RL_OvR(rate=tasa, rate_decay = decay, batch_tam=batch)
#             lr_OvR_dg_hot.entrena(X_entr_dg,y_entr_dg)

#             rendimiento_obtenido = rendimiento(lr_OvR_dg_hot, X_val_dg,y_val_dg)
#             if mejor_val < rendimiento_obtenido:
#                 mejor_val = rendimiento_obtenido
#                 mejores_params = {"rate": tasa, "rate_decay": decay, "batch_tam": batch}
#                 print(f"Para {mejores_params} rendimiento={rendimiento_obtenido}")

# print(f"Mejores parametros: {mejores_params} y rendimiento: {rendimiento(lr_OvR_dg_hot, X_test_dg,y_test_dg)}")


# >>> Mejores parametros: {'rate': 0.8, 'rate_decay': True, 'batch_tam': 32} y rendimiento: 0.843
# >>> Mejores parametros: {'rate': 0.01, 'rate_decay': False, 'batch_tam': 32} y rendimiento: 0.885
# Rate alto/bajo con o sin decay y tamaño del batch bajo

# --------------------------------------------------------------------------





















# ********************************************************************************
# ********************************************************************************
# ********************************************************************************
# ********************************************************************************

# EJEMPLOS DE PRUEBA

# LAS SIGUIENTES LLAMADAS SERÁN EJECUTADAS POR EL PROFESOR EL DÍA DE LA PRESENTACIÓN.
# UNA VEZ IMPLEMENTADAS LAS DEFINICIONES Y FUNCIONES (INCLUIDAS LAS AUXILIARES QUE SE
# HUBIERAN NECESITADO) Y REALIZADOS LOS AJUSTES DE HIPERPARÁMETROS, 
# DEJAR COMENTADA CUALQUIER LLAMADA A LAS FUNCIONES QUE SE TENGA EN ESTE ARCHIVO 
# Y DESCOMENTAR LAS QUE VIENE A CONTINUACIÓN.

# EN EL APARTADO FINAL DE RENDIMIENTOS FINALES, USAR LA MEJOR COMBINACIÓN DE 
# HIPERPARÁMETROS QUE SE HAYA OBTENIDO EN CADA CASO, EN LA FASE DE AJUSTE. 

# ESTE ARCHIVO trabajo-1-iacd-24-25.py SERA CARGADO POR EL PROFESOR, 
# TENIENDO EN LA MISMA CARPETA LOS ARCHIVOS OBTENIDOS
# DESCOMPRIMIENDO datos-trabajo-1-iacd.zip.
# ES IMPORTANTE QUE LO QUE SE ENTREGA SE PUEDA CARGAR SIN ERRORES Y QUE SE EJECUTEN LOS 
# EJEMPLOS QUE VIENEN A CONTINUACIÓN. SI ALGUNO DE LOS EJERCICIOS NO SE HA REALIZADO 
# O DEVUELVE ALGÚN ERROR, DEJAR COMENTADOS LOS CORRESPONDIENTES EJEMPLOS. 



# *********** DESCOMENTAR A PARTIR DE AQUÍ

print("************ PRUEBAS EJERCICIO 1:")
print("**********************************\n")
Xe_votos,Xp_votos,ye_votos,yp_votos=particion_entr_prueba(X_votos,y_votos,test=1/3)
print("Partición votos: ",y_votos.shape[0],ye_votos.shape[0],yp_votos.shape[0])
print("Proporción original en votos: ",np.unique(y_votos,return_counts=True))
print("Estratificación entrenamiento en votos: ",np.unique(ye_votos,return_counts=True))
print("Estratificación prueba en votos: ",np.unique(yp_votos,return_counts=True))
print("\n")

Xev_cancer,Xp_cancer,yev_cancer,yp_cancer=particion_entr_prueba(X_cancer,y_cancer,test=0.2)
print("Proporción original en cáncer: ", np.unique(y_cancer,return_counts=True))
print("Estratificación entr-val en cáncer: ",np.unique(yev_cancer,return_counts=True))
print("Estratificación prueba en cáncer: ",np.unique(yp_cancer,return_counts=True))
Xe_cancer,Xv_cancer,ye_cancer,yv_cancer=particion_entr_prueba(Xev_cancer,yev_cancer,test=0.2)
print("Estratificación entrenamiento cáncer: ", np.unique(ye_cancer,return_counts=True))
print("Estratificación validación cáncer: ",np.unique(yv_cancer,return_counts=True))
print("\n")

Xe_credito,Xp_credito,ye_credito,yp_credito=particion_entr_prueba(X_credito,y_credito,test=0.4)
print("Estratificación entrenamiento crédito: ",np.unique(ye_credito,return_counts=True))
print("Estratificación prueba crédito: ",np.unique(yp_credito,return_counts=True))
print("\n\n\n")





print("************ PRUEBAS EJERCICIO 2:")
print("**********************************\n")

nb_tenis=NaiveBayesCat(k=0.5)
nb_tenis.entrena(X_tenis,y_tenis)
ej_tenis=np.array(['Soleado','Baja','Alta','Fuerte'])
print("NB Clasifica_prob un ejemplo tenis: ",nb_tenis.clasifica_prob(ej_tenis))
# print("NB Clasifica un ejemplo tenis: ",nb_tenis.clasifica([ej_tenis])) # Por que poner [ej_tenis] en vez de ej_tenis como siempre?
print("NB Clasifica un ejemplo tenis: ",nb_tenis.clasifica(ej_tenis))

print("\n")

nb_votos=NaiveBayesCat(k=1)
nb_votos.entrena(Xe_votos,ye_votos)
print("NB Rendimiento votos sobre entrenamiento: ", rendimiento(nb_votos,Xe_votos,ye_votos))
print("NB Rendimiento votos sobre test: ", rendimiento(nb_votos,Xp_votos,yp_votos))
print("\n")


nb_credito=NaiveBayesCat(k=1)
nb_credito.entrena(Xe_credito,ye_credito)
print("NB Rendimiento crédito sobre entrenamiento: ", rendimiento(nb_credito,Xe_credito,ye_credito))
print("NB Rendimiento crédito sobre test: ", rendimiento(nb_credito,Xp_credito,yp_credito))
print("\n")


nb_imdb=NaiveBayesCat(k=1)
nb_imdb.entrena(X_train_imdb,y_train_imdb)
print("NB Rendimiento imdb sobre entrenamiento: ", rendimiento(nb_imdb,X_train_imdb,y_train_imdb))
print("NB Rendimiento imdb sobre test: ", rendimiento(nb_imdb,X_test_imdb,y_test_imdb))
print("\n")




normst_cancer=NormalizadorStandard()
normst_cancer.ajusta(Xe_cancer)
Xe_cancer_n=normst_cancer.normaliza(Xe_cancer)
Xv_cancer_n=normst_cancer.normaliza(Xv_cancer)
Xp_cancer_n=normst_cancer.normaliza(Xp_cancer)

print("Normalización cancer entrenamiento: ",np.mean(Xe_cancer_n,axis=0))
print("Normalización cancer validación: ",np.mean(Xv_cancer_n,axis=0))
print("Normalización cancer test: ",np.mean(Xp_cancer_n,axis=0))

print("\n\n\n")



nb_cancer=NaiveBayesGauss()
nb_cancer.entrena(Xe_cancer_n,ye_cancer)
print("NB rendimiento cáncer entrenamiento: ", rendimiento(nb_cancer,Xe_cancer_n,ye_cancer))
print("NB rendimiento cáncer prueba: ", rendimiento(nb_cancer,Xp_cancer_n,yp_cancer))




print("************ PRUEBAS EJERCICIO 5:")
print("**********************************\n")


lr_cancer=RegresionLogisticaMiniBatch(rate=0.1,rate_decay=True)
lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xv_cancer,yv_cancer)
print("LR clasifica cuatro ejemplos cáncer (y valor esperado): ",lr_cancer.clasifica(Xp_cancer_n[17:21]),yp_cancer[17:21])
print("LR clasifica_prob cuatro ejemplos cáncer: ", lr_cancer.clasifica_prob(Xp_cancer_n[17:21]))
print("LR rendimiento cáncer entrenamiento: ", rendimiento(lr_cancer,Xe_cancer_n,ye_cancer))
print("LR rendimiento cáncer prueba: ", rendimiento(lr_cancer,Xp_cancer_n,yp_cancer))

print("\n\n CON SALIDA Y EARLY STOPPING**********************************\n")

lr_cancer=RegresionLogisticaMiniBatch(rate=0.1,rate_decay=True)
lr_cancer.entrena(Xe_cancer_n,ye_cancer,Xv_cancer_n,yv_cancer,salida_epoch=True,early_stopping=True)

print("\n\n\n")

print("************ PRUEBAS EJERCICIO 6:")
print("**********************************\n")

Xe_iris,Xp_iris,ye_iris,yp_iris=particion_entr_prueba(X_iris,y_iris)

rl_iris_ovr=RL_OvR(rate=0.001,batch_tam=16)

rl_iris_ovr.entrena(Xe_iris,ye_iris)

print("OvR Rendimiento entrenamiento iris: ",rendimiento(rl_iris_ovr,Xe_iris,ye_iris))
print("OvR Rendimiento prueba iris: ",rendimiento(rl_iris_ovr,Xp_iris,yp_iris))
print("\n\n\n")



print("************ RENDIMIENTOS FINALES REGRESIÓN LOGÍSTICA EN CRÉDITO, IMDB y DÍGITOS")
print("*******************************************************************************\n")


# ATENCIÓN: EN CADA CASO, USAR LA MEJOR COMBINACIÓN DE HIPERPARÁMETROS QUE SE HA 
# DEBIDO OBTENER EN EL PROCESO DE AJUSTE

print("==== MEJOR RENDIMIENTO RL SOBRE VOTOS:")
RL_VOTOS=RegresionLogisticaMiniBatch(rate=0.8,rate_decay=False,batch_tam=128,reg=0.01) # ATENCIÓN: sustituir aquí por los mejores parámetros tras el ajuste
RL_VOTOS.entrena(Xe_votos,ye_votos) # Aumentar o disminuir los epochs si fuera necesario
print("Rendimiento RL entrenamiento sobre votos: ",rendimiento(RL_VOTOS,Xe_votos,ye_votos))
print("Rendimiento RL test sobre votos: ",rendimiento(RL_VOTOS,Xp_votos,yp_votos))
print("\n")


print("==== MEJOR RENDIMIENTO RL SOBRE CÁNCER:")
RL_CANCER=RegresionLogisticaMiniBatch(rate=0.0125,rate_decay=False,batch_tam=32,reg=0.01) # ATENCIÓN: sustituir aquí por los mejores parámetros tras el ajuste
RL_CANCER.entrena(Xe_cancer,ye_cancer) # Aumentar o disminuir los epochs si fuera necesario
print("Rendimiento RL entrenamiento sobre cáncer: ",rendimiento(RL_CANCER,Xe_cancer,ye_cancer))
print("Rendimiento RL test sobre cancer: ",rendimiento(RL_CANCER,Xp_cancer,yp_cancer))
print("\n")


print("==== MEJOR RENDIMIENTO RL_OvR SOBRE CREDITO:")
X_credito_oh=codifica_one_hot(X_credito)
Xe_credito_oh,Xp_credito_oh,ye_credito,yp_credito=particion_entr_prueba(X_credito_oh,y_credito,test=0.3)

RL_CLASIF_CREDITO=RL_OvR(rate=0.8,rate_decay=True,batch_tam=64) # ATENCIÓN: sustituir aquí por los mejores parámetros tras el ajuste
RL_CLASIF_CREDITO.entrena(Xe_credito_oh,ye_credito) # Aumentar o disminuir los epochs si fuera necesario
print("Rendimiento RLOVR  entrenamiento sobre crédito: ",rendimiento(RL_CLASIF_CREDITO,Xe_credito_oh,ye_credito))
print("Rendimiento RLOVR  test sobre crédito: ",rendimiento(RL_CLASIF_CREDITO,Xp_credito_oh,yp_credito))
print("\n")


print("==== MEJOR RENDIMIENTO RL SOBRE IMDB:")
RL_IMDB=RegresionLogisticaMiniBatch(rate=0.8,rate_decay=True,batch_tam=64,reg=0.01) # ATENCIÓN: sustituir aquí por los mejores parámetros tras el ajuste
RL_IMDB.entrena(X_train_imdb,y_train_imdb) # Aumentar o disminuir los epochs si fuera necesario
print("Rendimiento RL entrenamiento sobre imdb: ",rendimiento(RL_IMDB,X_train_imdb,y_train_imdb))
print("Rendimiento RL test sobre imdb: ",rendimiento(RL_IMDB,X_test_imdb,y_test_imdb))
print("\n")


print("==== MEJOR RENDIMIENTO RL SOBRE DIGITOS:")
RL_DG=RL_OvR(rate=0.01,rate_decay=False,batch_tam=32) # ATENCIÓN: sustituir aquí por los mejores parámetros tras el ajuste
RL_DG.entrena(X_entr_dg,y_entr_dg) # Aumentar o disminuir los epochs si fuera necesario
print("Rendimiento RL entrenamiento sobre dígitos: ",rendimiento(RL_DG,X_entr_dg,y_entr_dg))
print("Rendimiento RL validación sobre dígitos: ",rendimiento(RL_DG,X_val_dg,y_val_dg))
print("Rendimiento RL test sobre dígitos: ",rendimiento(RL_DG,X_test_dg,y_test_dg))








