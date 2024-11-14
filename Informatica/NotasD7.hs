import Test.QuickCheck

{-
tengo un numero y si es par lo divido entre 2, si es
impar lo multiplico por 3 + 1, se llama secuencia
collatz
-}

collatz3 :: Int -> [Int]
collatz3 n = n:collatzAux n [] 
    where
    	collatzAux 1 acum = acum
    	collatzAux n acum 
    	  | even n = collatzAux (div n 2) (acum ++ [div n 2])
    	  | otherwise = collatzAux (n * 3+1) (acum ++ [n * 3+1])


collatz :: Int -> [Int]
collatz 1 = [1]
collatz n
  | even n = n : collatz (div n 2)
  | otherwise = n : collatz (n * 3 + 1)


collatz2 1 = [1]
collatz2 n
  | even n = [n] ++ collatz2 (div n 2)
  | otherwise = [n] ++ collatz2 (3*n +1)

{-
saber cuantas succuencias de collaps hay hasta  n

-}

cuantosCollatz n = sum[1 | x<- [1..100], (length (collatz x)) > n]


cuantosCollatzN n = [1 | l <- map (collatz) [1..100], length l > n]

cuantosCollatzN2 n = length (filter (\x -> length x > n) (map (collatz) [1..100]))

numAlista n
  | n < 10 = [n]
  | otherwise = numAlista (div n 10) ++ [mod n 10]

calcularcubo x = x^3
cubos = [l | l <- [2..500], sum (map (calcularcubo) (numAlista l)) == l]
--["hola", "algun", "neumatico"] -- True
serpiente [] = True
serpiente [x] = True
serpiente (x:y:xs) 
  | last x == head y = serpiente (y:xs)
  | otherwise = False










































