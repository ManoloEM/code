import Mates.Aleatorios

--fromIntegral para cuando de error "No instance for (Fractional Int)"

data Direccion = Norte | Sur | Este | Oeste deriving (Show, Eq, Ord)

data Car = Car String String Int deriving (Show)

dados :: Semilla -> [Int]
dados s = aleatoriosDe [1..6] s

--E j e r c i c i o s de dado con 1 6 1€ 2 6 2€ 3 6 3€ 0 6 -1€

chuckalista s = simular lista
   where
   	lista = take 3000 (dados s)
   	simular [] = []
   	simular (x:y:z:xs) = contar [x,y,z] : simular xs

contar lista
  | numElem == 0 = -1
  | otherwise = numElem
    where 
    	numElem = length (filter (==6) lista)

saldo = fromIntegral (sum [sum (chuckalista n)| n <-[1..1000]]) / 1000

--para hacer la media es dividir entre 1000


--E j e r c i c i o dos habitaciones y 3 personajes
-- Cada segundo uno se mueve a una estancia
-- Pueden ir y volver entre las habitaciones
-- Pero cada movimiento consume 1 sec

data Abeja = Maya | Willy | Casandra deriving (Eq, Show)

movimientos :: Semilla -> [Abeja]
movimientos s = aleatoriosDe [Maya, Willy, Casandra] s
{-
Representacion de las estancias
Una lista con dos listas, la de la iz es la estancia
inicial y la de la derecha es la estancia final
quiero empezar con las 3 en la iz y terminar 3 en de

jugadas n = jugadasAux n s 0
  where
  	jugadasAux n s 3 = s
  	jugadasAux n s acum = 
-}
hacerMvto (eizq, eder ) unaAbeja
   | elem unaAbeja eizq = ((filter (/= unaAbeja) eizq), (unaAbeja : eder))
   | otherwise = ((unaAbeja : eizq), (filter (/= unaAbeja) eder))

simular s = aux ([Maya, Willy, Casandra], []) lista 0
	where
		lista = movimientos s
		aux (eizq, eder) (x:xs) segundo
		  | null eizq = segundo
		  | otherwise = aux (hacerMvto (eizq,eder) x) xs (1+segundo)
{-

hacerMvto (eizq, eder ) unaAbeja
   | elem unaAbeja eizq = ((filter (/= unaAbeja) eizq), (unaAbeja : eder))
   | otherwise = ((unaAbeja : eizq), (filter (/= unaAbeja) eder))

simular s = aux ([Maya, Willy, Casandra], []) lista ([Maya, Willy, Casandra], [])
	where
		lista = movimientos s
		aux (eizq, eder) (x:xs) cambio
		  | null eizq = reveres cambio
		  | otherwise = aux nuevaSituacion xs (nuevaSituacion : cambio)


-}



















