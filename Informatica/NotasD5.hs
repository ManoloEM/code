import Test.QuickCheck

{- pasar dado un numero de n digitos ->
decir cuantos digitos tiene. ej
2345 --> [2, 3, 4, 5]
0 --> ][0]
[mod n 10]
sabes cuando has terminado cuando n<10
-}

numAlista n
  | n < 10 = [n]
  | otherwise = numAlista (div n 10) ++ [mod n 10]

listaAnum [] = 0
listaAnum [x] = if x>10
	then error "Numero de mas de un digito"
	else x
listaAnum (x:xs) = if x>10 
	then error "Numero de mas de un digito"
	else x * 10^p + listaAnum xs 
	   where
	   	p = length (x:xs) - 1
    	
{-
listaAnum l
  | [x] = x
  | otherwise = 
--[mod n 10] ++ numAlista (n-1)
- - - - - -
funcion recursiva que devuelva la 
suma de los digitos de un numero

sumaDigitos1 2345 --14
sumaDigitos* 2345 -- 14 -- 5


sumaDigitos n
  | suma < 10 = suma
  | otherwise   = sumaDigitos suma
    where
    	sumaDigitos1 num = suma (numAlista n)
    	suma = sumaDigitos1 n

-- ahora quiero guardar los sucesivos valores

suma


sumaDigitos1 n
  | suma < 10 = suma
  | otherwise   = sumaDigitos suma
    where
    	sumaDigitos1 num = suma (numAlista n)
    	suma = sumaDigitos1 n



sumadigitoslista n
  | n < 10 = [n] ++ [suma]
  | otherwise = [n] ++ sumaDigitosLista suma
  where
  	sumaDigitos1 num = sum (numAlista n)
  	suma = sumaDigitos n

 decir cual es el digito que ocupa la posicion n de
un numero, empezando a comtar por la derecha
posdigito 1234 2 --> 2 dig de la posicion 2 es 2
pos 0 -> 4
pos 1 -> 3
pos 2 -> 2
pos 3 -> 1
-}
{-
posDigito n pos = lista !! pos
	where
		lista = reverse (numAlista n)
-}
posDigito n p = if (length lista) > p
	then lista !! p
	else error "no furula, i am sorry try again" 
	where
	lista = reverse (numAlista n)

posdigitos2 n 0 = mod n 10
posdigitos2 n p = posdigitos2 (div n 10) (p -1)

-- 12345 -> 54321
darVuelta n = listaAnum(reverse(numAlista n))
{-
Numeros felices son aquellos numeros que la suma
de los cuadrados de sus digitos sucesivamente
es = 1
-}
esCapicuo n = darVuelta n == n

esCapicuoR n = esCapicuo2 (numAlista n)
esCapicuo2 [] = True
esCapicuo2 [x] = True
esCapicuo2 (x:xs)
  | x == last xs  = esCapicuo2 (init xs)
  | otherwise     = False

sumaCuadrados n = 
	sum [x^2| x<- numAlista n]

esFeliz :: Int -> Bool
esFeliz 1 = True
esFeliz n = esFeliz (sumaCuadrados n)




















