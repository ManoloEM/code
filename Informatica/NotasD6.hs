import Test.QuickCheck

{-
repaso de recursividad normal que construye una list
me dan n construyo una lista de 1 a n[4,3,2,1]
si n 3s 4

hacerlista 1 = [1]
hacerlista n = n : hacerlista (n-1)

hacerlista2 1 = [1]
hacerlista2 n = hacerlista2 (n-1) ++ [n]

como hacerlo con acumuladores
1) Necesito una variable donde ir construyendo el
resultado.
hago una funcion  axiliar donde añado un parametro mas
2)Inicializo la variable nueva, con el caso base
3)Para el caso base, devuelvo la variable donde constr
uyo el resultado
4) la llamda recursiva es directamente una llamada a la
funcion . y en la varianle resultado "añado, sumo,.."

-}


hacerlist2 n = hacerlistaAux n []
  where
  	hacerlistaAux 0 acum = acum
  	hacerlistaAux n acum = hacerlistaAux (n-1) (n:acum)

--hacerlista 4 -> hacerlista 4 []
--hacerlistaaux 4 [] -> hacerlistaaux 3 [4] "viene de 4:[]"
--hacerlistaaux 2 [3, 4]
--hacerlistaaux 1 [2,3,4]
--hacerlistaaux 0 [1,2,3,4]
--[1,2,3,4]

hacerlista n = hacerlistaAux n []
  where
  	hacerlistaAux 0 acum = acum
  	hacerlistaAux n acum = hacerlistaAux (n-1) (acum ++ [n])

--sumar los n elementsos hasta que sea <= a x
-- [1,3,2,1,5,4,3,6,4] 9 -> [1,3,2,1], [5,4,3,6,4]

preMax lista n = preMaxAux lista n []
  where
   preMaxAux [] n acum = error "no hay suficientes numbers"
   preMaxAux (x:xs) n acum
     | ((sum acum) + x) > n = (acum, x:xs) ---me he pasado
     | otherwise = preMaxAux xs n (acum ++ [x])

{-
longitud [] = 0
longitud [x] = 1 -- no necesaria
longitud (x:xs) = 1 + longitud xs
-}

longitudA l = longitudAaux l 0
   where
   	longitudAaux []     acum = acum
   	longitudAaux (x:xs) acum = longitudAaux xs (acum + 1)

{-
sumarP [] = 0
sumarP [x] = 0
sumarP [x, y] = y
sumarP (x:y:xs) = y + sumarP xs
-}

sumarElemPares l = sumarElemParesAux l 0
   where
   	sumarElemParesAux [] acum = acum
   	sumarElemParesAux (x:xs) acum 
   	  | even x = sumarElemParesAux xs (acum + x)
   	  | otherwise = sumarElemParesAux xs acum

{-
repetir2 0 _ = []
repetir2 n elemento = [elemento] ++ repetir2 (n-1) elemento
-}

repetir n elem = repetirAux n elem []
  where
  	repetirAux 0 elem acum = acum
  	repetirAux n elem acum = repetirAux (n-1) elem (elem:acum)


































