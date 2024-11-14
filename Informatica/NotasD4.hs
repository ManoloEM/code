import Test.QuickCheck

{- factorial 1 = 1 ; factorial n =
 = n * factorial (n-1)
 Factorial n 
  | n == 1  =1
  | n == 0  =1
  | otherwise = n * factorial (n-1)

Suma n = sum [1..n]
sumR 1 = 1
sumR n = n + sumR (n-1)}

Recursividad -}

factorial 0 = 1
factorial 1 = 1
factorial n = if n>0 
	then n * factorial (n-1) 
	else 0

--p_factorial n>0 = factorial n == product [1..n]

--forma 2

factorial2 n
  | n <= 0 = 1
  | n == 1 = 1
  | otherwise = n * factorial (n-1)


--suma n primero numeros naturales de 1 a n
--sum [1..n]
sumaR 1 = 1;
sumaR n = n + sumaR (n-1)

-- sumar los pares de 1 hasta 
sumapR 0 = 0
sumapR 2 = 2
sumapR n
  | (n<2) = 0 
  | even n = n + sumapR (n-2)
  | otherwise = sumapR (n-1)

{- R. numerica . R listas.
[1,2,3,4] -> l = 4 / l= 1+ [2,3,4] . . . 
[] lista vacia
(x:xs) 
x / quier elem lista
xs resto ( la cola )
[x] lista de 1 elem 
[x,y] lista de 2 elem
(x:y:xs) 
x 1er elem
y 2nd elem}
patrones. recorrer listas
[] --> lista vacia
[x] --> lista 1 elem
[x,y] --> lista 2 elem
(x:xs) --> x 1er elem. xs el resto
(x:y:xs) --> x 1er, y 2nd. xs el resto
-}

longitud [] = 0
longitud [x] = 1 -- no necesaria
longitud (x:xs) = 1 + longitud xs

sumarL [] = 0
sumarL (x:xs) = x + sumarL xs  -- recursividad des cola

sumarLP [] = 0
sumarLP (x:xs)
 | even x = x + sumarLP xs
 | otherwise = sumarLP xs

--sumar los elem de posicion pares
--suponemos que la primera posicion es 1
-- sumarP ( sumar posicion ) [1, 2 ,3 ,2 ,5 ,5] = 9

sumarP [] = 0
sumarP [x] = 0
sumarP [x, y] = y
sumarP (x:y:xs) = y + sumarP xs

{- construir listas.  con numeros recursividad
 numerica para construir una lista
 replicate veces x --> hace una lista con 
 elemento x n veces.
 ej. replicate 5 1 -> [1,1,1,1,1]
 LC [x | a <- [1..n]]

 DOS FORMAS. 1) con : 2) con ++
 con : "lo que añado" : llamada recursiva
     en ese caso el caso base tiene que ser una lista
3:[4]. lo que añado va a la izquierda
con ++  : [ "lo que añado"] ++ llamada recursiva
--en ese caso el caso base tiene que ser una lista
si tengo que añadir a la deecha uso ++
llamada recursiva ++ ["lo que añado"]

-}
--replicate1 0 elemento = [] // _ --> da igual elem

repetir1 0 _ = []
repetir1 n elemento = elemento : repetir1 (n-1) elemento

repetir2 0 _ = []
repetir2 n elemento = [elemento] ++ repetir2 (n-1) elemento

repetir3 0 _ = []
repetir3 n elemento = repetir3 (n-1) elemento ++ [elemento]
--este solo se puede hacer con el ++ porque da igual si se suma por der o izq


--recursividad numerica lista1N 5 = [1, 2, 3, 4, 5]
{-}
lista1N2 0 = []
--lista1N n = lista1N (n-1) ++ [n]
lista1N2 n = n : lista1N (n-1)
-}
lista1N n = reverse (lista1Naux n)
    where
    	lista1Naux 0 = []
    	lista1Naux n = n : lista1Naux (n-1)















