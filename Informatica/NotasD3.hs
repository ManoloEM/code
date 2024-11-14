import Data.List

--copiar ->:l /Users/enciso/Desktop/NotasD3.hs- - -

--espar :: Int -> Bool
--espar x = mod x 2 == 0

--numeros pares de una lista--

pareslista ::[Int] -> [Int] 
pareslista l = [x | x <-l, mod x 2 == 0]

--pareslista2 l = [x | x <-l, espar x]
      --where
      	--z = cccc
      	--espar:: Int -> Bool
      	--espar x = mod x 2 == 0

-- funcion replicar 4 True
--- - >[True, True, True, True] 
--- - > Con listas por compresion


--repite veces elem = [elem | x <- [1..veces]]
repite u y = [y | x <- [1..u]]

longitudl l = sum [1 | x <- l]

--calcular todos numeros que al dividir da 0--
factores n = [ x | x <- [1..n], mod n x == 0]

--sacar los n perfectos( suma de sus factores son el n)--

esperfect n = sum (factores n) == n
     where
     factores n = [ x | x <- [1..(n-1)], mod n x == 0]

lesperfect n = [ x | x <- [1..n], esperfect x]

--producto cartesiano de 2 conj y luego 3--
-- l1 -> [1,2,3]
-- l2 -> [4,5]
--devuelve [(1,4)]
productoc2 l1 l2 = [ (x,y)| x <-l1, y <- l2]
productoc3 l1 l2 l3 = [ (x,y,z)| x <-l1, y <- l2, z <- l3]



--ordenar l1 l2 = sort (productoc2 l1 l2) --sort ordena por el primer valor de la dupla
--where
		--productoc2 l1 l2 = [ (x,y)| x <-l1, y <- l2]
        --productoc = productoc2 l1 l2

--quiero ordenar por el segundo elemento de la dupla
--el sort solo ordena teniendo en cuenta el primer elemento de la dupla
-- solu. le doy la vuelta, lo ordeno, le vuelvo a dar la vuelta
-- [ ( 1,9), (1,5) (1,12)] --> (9,1) (5,1) (12,1)
--ordenarPC2 l1 l2 = listafinal
--darvuelta l = [(x,y) | (x,y) <- l] --da la vuelta duplas
--productoC = productoc2 l1 l2 --hace el producto cartesiano
--listaordenada = sort (darvuelta productoC) --da la vuelta al PC y luego ordena
--listafinal = darlavuelta listaordenada --le vuelve a dar la vuelta

-- esTerna

esterna x y z = (x^2 + y^2) == z^2

tternas n = [ (x,y,z) | x <- [1..n], y <- [1..n], z <- [1..n], esterna x y z]











