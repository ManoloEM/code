import Test.QuickCheck

doble :: Int -> Int
doble x = x * 2

doble_p x = doble x == (x + x)

cuadrado x = x * x

--signox :: Int -> Int --cuando tengo mas de dos condiciones mejor usar guardas

--signo x = if (x < 0) then -1
	--else if (x > 0) then 1
		--else 0
--tipo de signo--
signo2 x
    | (x<0)  = -1
    | (x>0)  = 1
    | otherwise = 0
--tipo de huracan--continuar.
--119 153 154 177 178 209
huracan x
    | (x<119) = 0
    | (x>=119) && (x<153) = 1


sumacien = sum [2,4..100]
sumanpares n = sum [2,4..n]
factorial n = product [n,(n-1)..1]

--SIEMPRE ES UNA LISTA []
--[OPERACION que aplico a toda la lista
-------nombre-elemento <- [una lista]
--, ( puede haber o no ) condiciones]-- tipo mod (div) 5 == 0

imparesC :: [Int] -> [Int]

imparesC l = [x | x <- l, odd x]

sumaPositivo l = sum [ x | x <- l, x>0]












