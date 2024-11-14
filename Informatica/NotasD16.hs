--import Grafo
--import Pila

valida1 cadena = valida1Aux cadena 0
   where
   	valida1Aux [] acum = acum == 0 
   	valida1Aux (x:xs) acum 
   	    | acum < 0 = False
   	    | x == '('   = valida1Aux xs (acum + 1)
   	    | x == ')'   = valida1Aux xs (acum - 1)
   	    | otherwise  = valida1Aux xs acum


valida2 cadena = sumar [ convertir x| x <- cadena] 0
    where
        convertir x
        	| x == ')' = -1
            | x == '(' = 1
            | otherwise = 0
        sumar [] contador = contador == 0
        sumar (x:xs) contador
           | contador < 0 = False
           | otherwise = sumar xs ( contador + x )
 

{-
import pila

valida3 cadena pares = valida3Aux cadena pares Vacia
   where
      abrir = [ a | (a,b) <- pares ]
      cerrar = [ b | (a,b) <- pares ]
      valida3Aux [] pares pila = estaVacia pila
      valida3Aux (x:xs) pares pila
          | elem x abrir = valida3Aux xs pares (mete x pila)
          | (elem x cerrar) && not (estaVacia pila) && (elem (y, x) pares)
              = valida3Aux xs pares --porque la pila ha cambiado 
          | otherwise = valida3Aux xs pares pila
              where
              	 (y, p1) = saca pila
-}




















































