import Mates.Aleatorios

{-
--COLA CON PRIORIDAD

type Prioridad = Int
data ColaPrioridad a = CP [(a,Prioridad)]

instance (Show a) => Show (ColaPrioridad a) where
	show (CP xs) = "{" ++ elementosDe xs ++ "}"
	  where
	  	elementosDe [] = ""
	  	elementosDe [(x,p)] = show (x,p)
	  	elementosDe ((x,p):xs) = show (x,p) ++ "<" ++ elementosDe xs


vacia :: ColaPrioridad a
vacia = CP []

estaVacia :: ColaPrioridad a -> Bool
estaVacia (CP xs) = null xs

mete :: a -> Prioridad -> ColaPrioridad a -> ColaPrioridad a
mete x p (CP xs) = CP (inserta (x,p) xs)
  where
  	inserta (a,p) [] = [(a,p)]
  	inserta (a,p) ((b,p2): xs)
  	   | p>p2 = (a,p) : ((b,p2): xs)
  	   | otherwise = (b,p2): inserta (a,p) xs


primero :: ColaPrioridad a -> a
primero (CP []) = error "cola vacia"
primero (CP ((a,b):xs)) = a

saca :: ColaPrioridad a -> (a, ColaPrioridad a)
saca (CP ((a,b):xs)) = (a, CP xs)

-}

vertices :: Semilla -> [Int]
vertices s = aleatoriosDe [1..8] s


siguientes 1 = [2, 4, 5]
siguientes 2 = [1, 3, 4]
siguientes 3 = [2, 4, 7]
siguientes 4 = [1, 3, 8]
siguientes 5 = [1, 6, 8]
siguientes 6 = [2, 5, 7]
siguientes 7 = [3, 6, 8] -- estan envenenados no haria falta
siguientes 8 = [4, 5, 7]-- estan envenenados no haria falta

experimentos inicio semilla envenenados = experimentosAux inicio (vertices semilla) envenenados
   where
    	experimentosAux inicio (x:xs) envenenados 
   	          | elem x envenenados = [inicio,x] --se muere, a tomar por culo la hormiga
        	  | elem x (siguientes inicio) = experimentosAux x xs envenenados ++ [inicio]
              | otherwise = experimentosAux inicio xs envenenados


{-
experimento ini envenenados sem = expe ini [] (aleatoriosDe [-10000 .. 10000] sem) envenenados
   where
   	expe ini li (x : xs) envenenados
   	   | elem ini envenenados = li ++ [ini]
   	   | otherwise = expe (head (aleatoriosDe (siguientes ini)x)) (li ++ [ini]) xs envenenados
-}
experimento3 v0 s enve = aux3 v0  (vertices s) enve []
   where
    	 aux3 v0 (x:xs) enve acum
    	     | elem v0 enve = acum ++ [v0]
   	         | elem x (siguientes v0) = aux3 x xs enve (acum ++ [v0])
             | otherwise = aux3 v0 xs enve acum

promedio s inicio envenenados = promedio2 inicio envenenados (take 1000 (aleatoriosDe [1..1000] s))
   where
   	 promedio2 inicio envenenados semillas = 
   	 	div (sum (map (\unaSemilla -> length (experimento3 inicio unaSemilla envenenados) -1 )) )








