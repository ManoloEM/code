import Data.List
import Data.Char

longitudCadena  ::  IO  ()  
longitudCadena  = do  
    putStr  "Escribe  una cadena: " 
    xs <- getLine
    putStr  "La cadena  tiene  " 
    putStr  (show (length xs))  
    putStrLn  " caracteres" 

ejSecuenciacion :: IO (Char,Char)
ejSecuenciacion = do 
   putStrLn (" -------------------------------------------------- ")
   x <- getChar
   getChar -- el espacio para introducir dato ( solo tiene en cuenta le 1 y el 3 )
   y <- getChar
   putStrLn ("  ")
   putStrLn (" -------------------------------------------------- ") --escribe por pantalla ----- y salta 
   return (x,y) 


main = do
    putStrLn "Y tu eres...?"
    firstName <- getLine
    putStrLn "conocido como...?"
    lastName <- getLine
    let bigFirstName = map toUpper firstName
        bigLastName = map toUpper lastName
    putStrLn $ "Eres el PTO " ++ bigFirstName ++ " " ++ bigLastName ++ ", pensaba que eras mas alto"


data Arbol a = Vacio | Nodo a [Arbol a] deriving Show
arbol1 :: Arbol Int
arbol1 = Nodo 1 [ Nodo 2 [ Nodo 4 []
                         , Nodo 5 []
                         , Nodo 6 []
                        ]
                , Nodo 3 [ Nodo 7 [] 
                         , Nodo 8 []]
                ]

ramas :: Arbol a -> [ [a] ]

ramas Vacio = []
ramas ( Nodo a []) = [[a]]
ramas ( Nodo a as) = [a:z | z <- concatMap ramas as]

algunoCadaRama p a = and[ any p r | r <- ramas a]




















