import Test.QuickCheck

{-
map, filter, iterate f l, foldr, zipWith f l1 l2,
takeWhile f l, dropWhile f l, all f l 
(comprueba que todos lo cump),
any f l (comprueba si alguno lo cump),
concatMap f l

-ej: 

cuadrado x = x*x
map cuadrado [1,2,3]


map (\a ->a*a) [1,2,3])   <- defines dentro la funcion
map (\x -> x*x +5)

-}

--Lista de conversion
-- [(1,2),(3,2),(6,2)] -> 3 5 8
sumapares l = [ x + y| (x,y) <-l]
--recursividad
sumapR [] = []
sumapR ((a,b):xs) = a+b : sumapR xs
--recursividad normal
sumapares2 l = sumapares2Aux l []
 where
 	sumapares2Aux [] acum = reverse acum
 	sumapares2Aux ((a,b):xs) acum = sumapares2Aux xs (a+b : acum)

--funciones de orden superior

sumapresFOS l = map (\(x,y) -> x+y) l

sumapares_p l = sumapares2 l == sumapresFOS l


esSuave :: [Integer] -> Bool

esSuave [] = True
esSuave [x,y] = abs (x - y) == 1
esSuave (x:y:xs) 
  | abs (x - y) == 1 = esSuave  (y:xs)
  | otherwise = False


--En funciones de orden superior
--zipWith (x:xs) (xs) primer elem con el segundo

esSuaveFOS :: [Integer] -> Bool
esSuaveFOS (x:xs) = and (zipWith (\a b -> (abs (a- b) == 1)) (x:xs) xs)


esSuaveFOS2 (x:xs) = all (\(r,s) ->(abs (r- s) == 1)) --landa que comprueba
                        (zipWith (\a b -> (a,b)) (x:xs) xs) --landa que combina


--suaves n
suaves2 1 = [[0]]
suaves2 n
  | n>0 = concatMap (\ (x:xs) -> [x+1:x:xs, x-1:x:xs]) (suaves2 (n-1))
  | otherwise = error "n debe ser mayor que 0"

p_suaves n = n > 0 ==>  and (map (esSuave) (suaves2 n))























