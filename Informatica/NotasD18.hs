--import qualified Arbol as A
--import qualified Cola as C
--import qualified Pila as P
--import Grafo
import Data.List



--1febrero 2013 fun tema 2
--a
h f1 f2= f2 + f1

fun xs = sum [ h 5 x | x <- xs ]

fun2 xs = sum (map (\x -> h 5 x) xs)

--a

fun' x = not (even (abs x))
fun3 xs = not . even . abs $ xs

-- 3 Febrero 2013 menorNatural
{-
Funcoiones auxilires:
factorial
pasar numero a lista _> numalista o show (sring)
cuantosCeros ultimos o una lista


-}
factorial 1 = 1
factorial 0 = 1
factorial n = n * (factorial (n-1))
listaFactorial = repetir 1
   where
   	repetir n = (factorial n) : (repetir (n+1)) 

{-
factorail2 = 1: (iterate (\n -> n * (n+1)) 1)  <-- Mal

listaFactoria = repetir 1
   where
   	repetir n = (factorial n) : (repetir (n+1)) 




-}
{-
convertirNum x = convertirNumAux x []
   where
   	convertirNumAux 0 acum = acum
   	convertirNumAux x acum = convertirNumAux (div x 10) ((mod x 10) : acum)

cuantosCeros list = cuantosCerosAux (reverse list) 0 40  -- el 40 se puede cambiar por cualquiera
   where
   cuantosCerosAux (x:xs) n fin 
      | (n == fin )&& (head xs /= 0) = True
      | x /= 0 = False
      | otherwise = cuantosCerosAux xs (n+1) fin


contar elementos lista = contarAux elemento lista 0
   where
   	contarAux elemento [] acum = acum
   	contarAux elemento (x:xs) acum
   	  | x == elemento = contarAux elemento xs (acum + 1)
   	  | otherwise = acum

contarCeros2 lista = length ( takeWhile (==0) (reverse lista))

menorNatural2 = (filter (x\ -> contarCeros2 (convertir x) == 1987)) listaFactorail

menorNatural2 = (filter (\x -> contarCeros2 (convertirNum x) == 200)) listaFactorial

menorNatural = menorNaturalAux 1
   where
   	menorNaturalAux n = if cuantosCeros (convertirNum n )
   		then n
   		else menorNaturalAux (n+1)


contarCeros2 lista = length ( takeWhile (==0) (reverse lista))
-}
--menorNatural2 = (filter (x\ -> contarCeros2 (convertir x) == 200)) listaFactorail
menorNatural3 numeroCeros =
	(fst (head (filter (\(x,f) -> contarCerosFinal2 (convertirNum f ) == numeroCeros) listaFactorial)))

contarCerosFinal2 lista = length (takeWhile (==0) (reverse lista))

contar elemento lista = contarAux elemento lista 0
   where
   	contarAux elemento [] acum = acum
   	contarAux elemento (x:xs) acum
   	  | x == elemento = contarAux elemento xs (acum + 1)
   	  | otherwise = acum

convertirNum x = convertirNumAux x []
   where
   	convertirNumAux 0 acum = acum
   	convertirNumAux x acum = convertirNumAux (div x 10) ((mod x 10) : acum)





