import Mates.Aleatorios

dados :: Semilla -> [Int]
dados s = aleatoriosDe [1..6] s


numero s = aleatoriosDe [1..10] s



{-  "BLANCAS Y NEGRAS"

1) Genero una lista de aleatorios para el azar, cojo el
primer numero para las blancas y el segundo para negras

2) Represento las blancas como 0 y las negras como 1

3) ¿como represento el casillero?  -> lista de n elem

4) Cual es el inicio de la funcion -> simular tamaño
casilleros semilla para aleatorios

5) ¿como llamo los casilleros iniciales?
 lista con n unos -> replicate
 lista con n ceros -> replicate

6) Intercambiar las listas de 0 con la lista de 1

7) contar cuantos elementos (0 a 1) en un casillero

--ejem:

intercambiar [0,0,0,0] [1,1,1,1] 2 4 -> 
-> [0,1,0,0] [1,1,1,0] 



-}


intercambiar ci cd pi pd = (nuevoI, nuevoD)
   where
		elementoI = ci !! (pi-1)
		elementoD = cd !! (pd-1)
		nuevoI = take (pi-1) ci ++ [elementoD] ++ drop (pi) ci
		nuevoD = take (pd-1) cd ++ [elementoI] ++ drop (pd) cd


-- contar 0 [1,2,3,0,0] -> 2

contar n l1 = length(filter (==n) l1)

--para contar el numero de intentos un acum desde 0 que se sume 1

simular numBolas semilla
  | odd numBolas = error "debe ser un num div entre 2"
  | otherwise = probar ci cd aleatorios []
    where
    	ci = replicate numBolas 0
    	cd = replicate numBolas 1
    	aleatorios = aleatoriosDe [1..numBolas] semilla


probar ci cd (x:y:xs) acum 
  | (contar 0 ci) == (contar 0 cd) = reverse((ci,cd):acum)
  | otherwise = probar nuevoD nuevoI xs ((ci,cd):acum)
    where
    	(nuevoD, nuevoI) = intercambiar ci cd x y
-- Esto tambien te lo cuenta si las balncas fuesen
-- una letra y las negras tambien.
-- data Bolas Blanca|Negra deriving (Show)














































