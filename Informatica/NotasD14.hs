import Data.List
import Mates.Aleatorios


data Expr = Num Int |
             Suma Expr Expr |
             Producto Expr Expr |
             X deriving (Show, Eq)

numVars:: Expr -> Int
--numVars me tiene que decir el numero de variables de la expresion
{-
numVars (Num 3) = 0
numVars x = 1
numVars suma x (suma (num 3 ) x) = 2
numVars suma x (suma x x) = 3
-}

numVars (Num z) = 0
numVars (Suma e1 e2) = numVars e1 + numVars e2
numVars (Producto e1 e2) = numVars e1 + numVars e2
numVars (X) = 1









































