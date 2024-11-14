import Test.QuickCheck

{-
LISTAS INFINITAS
1) con rangos [1..] o [2,4..]
2) Funciones del lenguaje:
  repeat -> repeat 5 = [5,5,5,5..] 
  cycle -> cycle [1,2] = [1,2,1,2,1,2..] 
  iterate -> iterate (+2) 0 = [0,2,4,6,8..]
3) Con recursividad
  Es recursividad de listas, normas a seguir
  No tengo caso base
  NO HACER CON ACUM
-}

--contar de 1 a infinito

contar inicio = inicio : contar (inicio +1)

contar1 inicio = [inicio] ++ contar1 (inicio +1)

--RECURSIVIDAD CON ACUM NO VALE PARA LISTAS INFINITAS
contar2 inicio = contarAux (inicio +1) [inicio]
   where
   	contarAux n acum = contarAux (n+1) (n:acum)

{--COMO TRABAJAR CON LISTAS INFINITAS--}

--Devolver las posiciones pares de una lista
--con zip
posicionesPares lista = 
	[ x | (x,y) <- parejas, even y]
	where
		parejas = zip lista [1..]

-- take porque saca los n primeros elementos 



{-- PROBLEMAS CON LISTA INFINITAS --}

-- Fibonacci, collatz, criba
-- Lap, lookandsay, Nicomano, numeros pi


-- Serie de Fibonacii
--0 1 1 2
-- término 0 --> 0 término 1 --> 1  término n --> (n-1) + (n-2)


fibi 0 = 0
fibi 1 = 1
fibi n = fibi (n-1) + fibi (n-2)


fibs = [fibi x| x<- [1..]]


{-
fib2 0 = 0
fib2 1 = 1
fib2 n = aux 0 1
  where
  	aux x y = x : fib2 y (x + y) 
-}

-- SACAR LISTA DE NUMEROS PRIMOS
-- Método division por tentativa

-- saco todos los divisores de un numero
-- los primos de n, es un numero que sus divisores solo
-- son el 1 y el mismo numero

divisores n = [x | x<-[1..n], mod n x == 0]


esprimo p = divisores p == [1,p]

primos = [x | x<-[1..], esprimo x]


-- CRIBA DE ERATOSTENES
-- Tengo una lista de numeros, que empieza por 2
-- Saco de la lista todos los multiplos del primer elemento
-- de la lista
-- Me apunto el 1
-- Repito el proceso con el resto de la lista


primos2 = criba [2..]
criba (x:xs) = x: criba [y | y<- xs, mod y x /= 0]

{-
1- 


-}

--anagramas :: [[Char]] -> [[Char]] -> Bool
anagramas pal1 pal2 = pares
   where
   	pares = zip ['a'..'z'] primos2
   	valorNum l = head [valor | (letra, valor) <- pares, letra == l]
    valorPal palabra = sum[valorNum letra| letra <- palabra]











































