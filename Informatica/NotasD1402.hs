import Data.List
import Mates.Aleatorios



data Expresi = N Integer
     | X
     | Expresi :+ Expresi
     | Expresi :- Expresi
     | Expresi :* Expresi
     | Expresi :^ Int
  deriving (Eq, Show)
-- Febrero 2014 Expr Tema 5
e1 :: Expresi
e1 = (N 3 :* X) :- ((X :+ N 2) :^ 7)
-- 2X^2 +1
e2 :: Expresi
e2 = (N 2 :* (X :^2 )) :+ (N 1)

{-
evalua e2 1 = 3
evalua e2 2 = 7
evalua :: Expresi -> Int -> Int
-}

evalua (N numero) valor = numero
evalua (X)        valor = valor
evalua (e1 :+ e2) valor = (evalua e1 valor) + (evalua e2 valor)
evalua (e1 :- e2) valor = (evalua e1 valor) - (evalua e2 valor)
evalua (e1 :* e2) valor = (evalua e1 valor) * (evalua e2 valor)
evalua (e1 :^ potencia) valor = (evalua e1 valor) ^ potencia


--Calculo el maximo valor, lo apunto
-- Luego busco que valores sx an ese maximo valor
-- hago las tuplas

maximo expresion rango = (maximoValor, valoresX)
	where
		maximoValor = maximum [ evalua expresion x | x <- rango]
		valoresX = [x | x<-rango, evalua expresion x == maximoValor ]

--maximoValor expresion rango = [(evalua expresion x, x) | x <- rango]

calculaValores expresion rango = [evalua expresion x| x <- rango]


data Expr a = Null | Sum [Expr a] | Prod [a] deriving (Show)
 
expresionDe [] = Null
expresionDe lista = Sum [Prod x | x <- lista]






 
























