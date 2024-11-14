--import Test.QuickCheck
-- 18. Septiembre 2014. UnosYCeros. Tema 3.
-- 1ª opción: pasar una lista infinita pasando todos los números a binario
--data Binario = Cero | Uno deriving (Show, Eq) 
--aBinarioL :: Int -> [Binario]
aBinarioL numero 
  | numero > 1 && (mod numero 2) == 0 = aBinarioL (div numero 2) ++ [0]
  | numero > 1 && (mod numero 2) == 1 = aBinarioL (div numero 2) ++ [1]
  | otherwise = [1]
listaAnum [] = 0
listaAnum [x] = if x>10
    then error "Numero de mas de un digito"
    else x
listaAnum (x:xs) = if x>10
    then error "Numero de mas de un digito"
    else x*(10^exponente) + listaAnum xs
      where
      exponente = length (x:xs) - 1
unosYCeros = map (listaAnum) [ aBinarioL x | x <- [1,2..] ] -- faltan listaAnum

-- 2ª opción: 
unosYCeros2 = 1 : concat [ [x*10, x*10+1] | x <- unosYCeros2 ]

-- 3ª opción:
siguiente n = listaAnum (aux1 n)
numAlista n 
  | n < 10 = [n]
  | otherwise = numAlista (div n 10) ++ numAlista (mod n 10)
aux1 n 
  | all (==1) l = 1:(take (length l) (repeat 0))
  | otherwise = reverse (aux2 (reverse l))
  where
  l = numAlista n
aux2 (x:xs)
  | x == 0 = 1:xs
  | otherwise = 0:(aux2 xs)
unosYCeros3 = iterate (\n -> siguiente n) 1

-- otro apartado
multUnosYCeros n f = filter (\x -> mod x n == 0) f 
{-
-- propiedad quickCheck
prop2 n f = (n>0) && not (null (multUnosYCeros n f))
prop3 n f = (n>0) ==> not (null (multUnosYCeros n f))

--tutorías martes y jueves, por la mañana en informatica
--preguntas en foro

-- 32.Febrero 2016. CalculoMul. Tema 3
-- 1) calculoMul:
calculoMul lista n = if product resultado == n then resultado else []
  where
  resultado = calculoMul' lista n
calculoMul' [] n = []
calculoMul' (x:xs) n 
  | mod n x == 0 = x:calculoMul (x:xs) (div n x)
  | otherwise = calculoMul xs n

-}
calculoMulA lista n = calculoMulAux lista n []
   where
     comprobar lista
       | product lista == n = lista
       | otherwise = []
     calculoMulAux [] n acum = comprobar (reverse acum)
     calculoMulAux (x:xs) n acum
       | mod n x == 0 = calculoMulAux (x:xs) (div n x) (x:acum)
       | otherwise = calculoMulAux xs n acum



calculoSumasMul lista numero 
    | comprobacion == numero = resultado
    | elem [] resultado = error "digito no in scope"
    | otherwise = error " try again with computer"
    where
      convertir n -- convierte el 235 en [2, 3, 5]
        | n < 10 = [n]
        | otherwise = convertir (div n 10) ++ [mod n 10]
      descomposicion n = [ (x * 10)^y | (x, y) <- zip (convertir n) [2, 1, 0], x /= 0]
      resultado = [calculoMulA lista x | x <- descomposicion numero, x /= 0]
      comprobacion = sum [ product x | x <- resultado]

-- lo que hacia ella era sacar por decena centena etc 


-- QUIERO UN CASO POR CADA CASO DEL TIPO
data Expr a = Null | Sum [Expr a] | Prod [a] deriving Show

--expresionDe :: [[a]] -> Expr

expresionDe [] = Null
expresionDe lista = Sum [ Prod x | x <- lista] 

evaluaExpr Null = 0
evaluaExpr (Sum lista) = sum [(evaluaExpr x) | x <- lista ] --tambien se puede sustituir evalua por produt
evaluaExpr (Prod lista) = product lista
 
-- read "4" :: Int

expresionToString Null = " "
expresionToString (Sum []) = " "
expresionToString (Sum [x]) = "(" ++ expresionToString x ++ ")"
expresionToString (Sum (x:xs)) = 
  "(" ++ expresionToString (x) ++ ")" ++ "+" ++ expresionToString (Sum xs)
expresionToString (Prod []) = " "
expresionToString (Prod [x]) = show x
expresionToString (Prod (x:xs)) = 
  show x ++ "*" ++ expresionToString (Prod xs)


{-
-- ac es el acum 
foldr (\x ac -> XXX) lista []

(x:y:xs)

zip [4, 3, ,2 , 1] [3, 2, 1] --> (4, 3) (3, 2) (2 ,1)
foldr (\(x, y) ac) zip --> ac ++ show x ++ "*" ++ show y  ) zip [(4, 3) (3, 2) (2 ,1)]


intpor 

-}

