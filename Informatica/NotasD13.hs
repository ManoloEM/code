	import Mates.Aleatorios
import Data.List



--Definimos un tipo nuevo que llamo forma
data Forma = Circulo Float Float Float -- x1 x2 radio
             |Rectangulo Float Float Float Float-- x1 y1 x2 y2
             |Cuadrado Float Float Float--x1 y1  centro
             deriving (Show, Eq)

-- las variables del tipo empiezan por la palabra
--cada opcion
circulo1 = Circulo 2.0 3.5 21.0 
cuadrado2 = Cuadrado 2.0 2.4 12.7
rectangulo1 = Rectangulo 1.0 3.0 2.3 43.2

-- para cado caso del data tiene que haber una linea
--en la funcion
area (Circulo x1 x2 radio) = pi * radio * radio
area (Rectangulo x1 y1 x2 y2) = (x2 - x1) * (y2 - y1)
area (Cuadrado x1 y1 lado) = lado * lado


--EJERCICIO RED SOCIAL

type Persona = String
type Mensajes = [String]
type Seguidores = [Persona]
type Siguiendo = [Persona]
data Cuenta = Usuario Persona Mensajes Seguidores Siguiendo
              deriving Show

lm = ["2016 3 12 9 23 Siempre he cocinado con el objetivo de aportar algo técnico y conceptual a la cocina y de emocionar a los clientes, como mis amigos @berasategui @sandavoal y @luisjanez","2015 3 10 23 10 La cocina de @osuna es de alta calidad y creativa, sin fronteras, como la de @berasategui"]
se = ["@berasategui", "@dacosta", "@danigarica", "@ramonluis"]
si = ["@berasategui", "@davidmunoz", "@joseandres", "@luisjanez", "@sandoval"]




adria :: Cuenta
adria = Usuario "@adria" lm se si
creaUsuario usuario = Usuario ("@" ++ usuario) [] [] []

getCitando (Usuario identificador listaMensajes listaSeguidores listaSiguiendo) =
    sort (nub [ unaPalabra | n <- listaMensajes, unaPalabra <- words n, (head unaPalabra) == '@' ])

addMensaje (Usuario identificador listaMensajes listaSeguidores listaSiguiendo) mensaje =
      Usuario identificador nuevalista listaSeguidores listaSiguiendo
        where
          nuevalista = sort (mensaje : listaMensajes)

--Sintaxis de registro
-- se pueden definir tipos dando nombre a los campos, Se da nombre
--a os campos

data Coche0 = Coche0 String String Int deriving (Show) --marca modelo año
micoche0::Coche0
micoche0 = Coche0 "Citroen" "Saxo" 2001

data Coche1 = Coche1 {marca::String, modelo::String, anio::Int} deriving (Show)

micoche1::Coche1
micoche1 = Coche1 {modelo = "Leon", marca  = "Seat", anio = 2010} --cualquier orden

-- definicion del tipo con parametros

---TIPOS RECURSIVOS--- 
-- Es un tipo donde el propio tipo es parte de la definicion
-- Ejercicio de tortuga

data MovTortuga = Av | Dr | Rp Int [MovTortuga] deriving Show
type CaminoTortuga = [MovTortuga] -- lista de movimientos

camino1:: CaminoTortuga
camino1 = [Av,Dr,Av,Dr,Dr,Dr,Rp 4 [Av,Dr,Dr,Dr],Dr]


longitud:: CaminoTortuga -> Int

longitud [] = 0
longitud (Av:xs) = 1                                               + longitud xs
longitud (Dr:xs) =                                                   longitud xs
longitud (Rp veces listaMvtos: xs)= (veces * (longitud listaMvtos )) + longitud xs


data Orientacion = N | S | E | O deriving Show

--orientacion :: Orientacion -> CaminoTortuga -> Orientacion

--Orientacion E camino1


orientacion N [] = N
orientacion S [] = S
orientacion E [] = E
orientacion O [] = O




orientacion N (Av:xs) = orientacion N xs
orientacion N (Dr:xs) = orientacion E xs
orientacion x (Rp n listaMvtos : xs) = orientacion x nuevalista 
   where 









