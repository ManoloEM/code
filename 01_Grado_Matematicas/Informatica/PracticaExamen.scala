import java.io.FileReader
import java.util

import inform.util.aleatorios.Aleatorio


/*
P R A C T I C A, E X A M E N
 */

////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Julio 2017
/*
object ej1 extends App {

  import java.io.File
  import java.util.Scanner
  import scala.io.StdIn._

  case class Punto(x: Double, y: Double) // el case para autodefinir el toString o comparar....

  def leerFichero(fichero: String): List[Punto] = {
    val f = new File(fichero)
    if (f.isFile) {
      var puntos = List[Punto]()
      val sc = new Scanner(f)
      while(sc.hasNextLine) {
        val linea = sc.nextLine()
        val scl = new Scanner(linea)
        val x = scl.nextDouble()
        val y = scl.nextDouble()
        val p = Punto(x, y)
        puntos ::= p

        scl.close()
      }
      sc.close()
      return puntos.sortBy(_.x)

    } else sys.error("Fichero " + fichero + " es tonot")
  }

    def funcion: Unit = {
      var lista = leerFichero("datos.txt")
      println("Escribe el valor de z ")
      var z = readDouble()
      val posiA = lista.filter(_.x <= z).sortBy(_.x).reverse
      val posiB = lista.filter(_.x >= z).sortBy(_.x)
      val aproxA = posiA(0)
      val aproxB = posiB(0)
      val fDez = aproxB.y + (aproxA.y - aproxB.y) / (aproxA.x - aproxB.x) * (z - aproxB.x)
      println("f("+z+") = %.2f".format(fDez))
    }

    println(funcion)

}

object ejer20172 extends App {

  def prueba(lon : Int, texto : String, funci : Char => Boolean) : List[String]= {
    var lista = List[String]()
    var acum = 0
    var letra : String = ""
    while(acum < lon) {

      if(!funci(texto(acum)))
      {
        letra = letra:+texto(acum)
        acum += 1
      }
      else
      {
        var seSigue = true
        lista = lista :+ letra
        letra = ""
        while(seSigue && acum < lon){
          if(funci(texto(acum))) acum += 1
          else seSigue = false
        }
      }

    }

    return lista
  }

  case class Analizador(texto : String,funci : Char => Boolean){
    var contador = 0
    val lon = texto.length

    var pru = prueba(lon,texto,funci)
    def haySiguiente : Boolean = contador < pru.length
    def siguiente() : String = {
      val palabra = pru(contador)
      contador += 1
      return palabra

    }

  }

  val an = Analizador("la   casa,de ,la  bomba;  ", " ,;".contains(_))
  while(an.haySiguiente){
    println(an.siguiente())}




}
*/
////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Julio 2016
/*
object Ejercico1 extends  App {
  def sinUsarDatos(n : Int) : Int = {
    var lista = List[Int](0, 1, 2) //entendemos que empezamos por el término 0
    if(n <= 2) lista(n) else {
      for (i <- 3 to n) {
        lista = (lista(i - 3) + lista(i - 2) + lista(i - 1)) :: lista.reverse
        lista = lista.reverse
      }
      return lista(n)
    }
  }

  def sinUsarDatos2(n : Int) : Int = {
    var acum1 = 0
    var acum2 = 1
    var acum3 = 2
    if(n != 0 && n != 1 && n != 2) {
    var contador = 1
    var esn = 3
      while (n != esn) {
        esn = esn + 1
        if (contador == 1) {
          contador = 2
          acum1 = acum1 + acum2 + acum3
        } else {
          if (contador == 2) {
            contador = 3
            acum2 = acum1 + acum2 + acum3
          } else {
            contador = 1
            acum3 = acum1 + acum2 + acum3
          }
        }
      }
      return acum1 + acum2 + acum3
    } else return n

  }
//print(sinUsarDatos2(4))

  def sinUsarBucles(n : Int) : Int = {
    if(n != 0 && n != 1 && n != 2) {
    recursi(0,1,2,1,n-3)} else n
  }
  def recursi(x : Int,y : Int,z : Int, contador : Int, cuentAtras : Int) : Int = {
    if(cuentAtras != 0) {
        if(contador == 1) {
          recursi(x+y+z,y,z,2,cuentAtras-1)
        }
        else {
          if (contador == 2) {
            recursi(x,y+x+z,z,3,cuentAtras-1)
          } else {
            recursi(x,y,z+y+x,1,cuentAtras-1)
          }
        }
      }
    else return x+y+z
    }

  //print(sinUsarBucles(7))
  import scala.collection.immutable.Stack

  def usandoPilas(n : Int) : Stack[Int] = {
    var pila : Stack[Int] = Stack()
    if(n != 0 && n != 1 && n != 2 && n != 3) {
      pila = pila.push(0,1,2)
      while(pila.length != n) {
        var primero = pila.top
        pila = pila.pop
        var segundo = pila.top
        pila = pila.pop
        var tercero = pila.top
        pila = pila.pop
        pila = pila.push(tercero,segundo,primero,tercero+segundo+primero)
      }
      return pila
      }
     else {if(n >0) {for(i <- 0 until n) {
      pila = pila.push(i)
    }
      return pila
    }
    else return pila
  }
  }
  //print(usandoPilas(8))
  }


object Ejercicio2 extends App {

  def mezcla(lista: List[List[Int]]): List[Int] = {
    var resultado = List[Int]()
    for (i <- 0 until lista.length) {
      var longitud = lista(i).length
      for (j <- 0 until longitud) {
        var resto = List[Int]()
        var longi = resultado.length
        var seSigue = true
          while(longi != 0 && seSigue) {
            if(lista(i)(j) > resultado.head) {
              resto = resultado.head :: resto
              resultado = resultado.tail
              longi = resultado.length
            } else seSigue = false

          }
          resultado = resto.reverse ++ (lista(i)(j) :: resultado)
      }
    }
    return resultado
  }
  print(mezcla(List(List(100,2,300), List(100,100,200), List(1,10,0))))

}
/*
object Ejercicio3 extends App {
  trait Iterador[A] {
    def haySiguiente() : Boolean
    def siguiente() : A
  }
  case class IteradorArray(var xs : Array[Any]) extends Iterador[Any]{
    def haySiguiente = xs.length != 0
    def siguiente   = {
      var siguiente = xs(0)
      xs = xs.drop(1)
      siguiente
    }
    val it1 = IteradorArray(Array(10,20,30))
  }


  def prueba(xs : Array[Int]) : Int = {
    var xp = IteradorArray(xs)
    var s = 0
    while(xp.haySiguiente())
      s = s + xp.siguiente()
    return s
  }

}
*/
object Ejercicio3 extends App {
  import java.io._

  trait Iterador[A] {
    def haySiguiente() : Boolean
    def siguiente() : A

  }

case class IteradorArray[A](var xs : Array[A]) extends Iterador[A]{
def haySiguiente = xs.length != 0
def siguiente()   = {
  var siguiente = xs(0)
  xs = xs.drop(1)
  siguiente
}
}
  /*
var s = 0
val it1 = IteradorArray(Array(10,20,30))
while(it1.haySiguiente())
  s = s + it1.siguiente()
println(s)


      case class IteradorFichero(nombre :  String) {
    val fich = new File(nombre)
    val fr = new FileReader(fich)
    var n : Int = fr.read()
    while(n!= -1){
      print(n.toChar)
      n = fr.read()
    }
  }

  val it2 = IteradorFichero("MiFichero.txt")2013
*/


  case class IteradorFichero(nombre :  String) extends Iterador[Char]{
    val fich = new File(nombre)
    val fr = new FileReader(fich)
    var longitud = fich.length()
    var n : Int = 0
    def haySiguiente : Boolean ={
      longitud >= 1
    }
    def siguiente: Char = {
      n = fr.read()
      longitud -= 1
      return n.toChar
    }
  }

  val it2 = IteradorFichero("MiFichero.txt")
  while(it2.haySiguiente()){
    println(it2.siguiente())}

}
*/
////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Junio 2016
/*
object losTresAlumnos extends App {
  import inform.util.aleatorios._
  val alt = Aleatorio(1)
  def probabilidad : Double = {
    var seLibran = 0
    for( i <- 1 to 10000) {
      var alum1 = alt.entero(1, 4)
      var alum2 = alt.entero(1, 4)
      var alum3 = alt.entero(1, 4)
      if(alum3 == alum1 && alum1 == alum2) seLibran = seLibran + 1
    }
    return (seLibran.toDouble / 10000)
  }

print(probabilidad)

}
object representacionBinaria extends App {
  import scala.collection.immutable.{Map,Set}


}

*/
object ejer3dejun2016 extends App {

  class Polinomio(val grado : Int) {
    private var coeficientes = new Array[Int](grado + 1)
    def update(gr: Int, coef: Int) {
      if (gr >= 0 && gr <= grado)
        coeficientes(gr) = coef
      else
        sys.error("Grado no válido")
    }
    def horner(x : Int) : Int = {
      var sumando = 0
      for(i<- 0 to grado){
        println(coeficientes(i)+" coeficiente "+i)
        sumando += Math.pow(x, i).toInt * coeficientes(i)
        println((x^i) * coeficientes(i))
        println(Math.pow(x, i))
      }
      return sumando
    }
  }

  Math.pow(3.0, 2.0)
  var polinom = new Polinomio(2)
  polinom.update(2,10)
  polinom.update(1,-5)
  polinom.update(0,3)
println(polinom.horner(1))

}






////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Junio 2015

object ejercicio1 extends App {
  //usando map y sum
  var xss : Array[Array[Int]] = Array[Array[Int]](Array[Int](1,2,3),Array[Int](1,2,3))
  xss.map(_.sum).sum

  var total : Int = 0
  for(i <-0 until xss.length){
    for(j <-0 until xss(i).length){
      total = total + xss(i)(j)
    }
  }

}

object ejer4del2015 extends App {
  import scala.collection.mutable.Set

  def reflexiva[A](xs : Set[A]) : Set[Set[A]] ={
    var ys = xs.clone()
    var elVoid : Set[Set[A]]= Set(Set())
    while(ys.nonEmpty){
      val copi = elVoid
      val cabeza = ys.head
      println(elVoid+"primera parte")
      elVoid = elVoid.map(_ += cabeza)
      elVoid += ys.tail
      println(elVoid+"segunda parte")
      elVoid = elVoid.union(copi)
      println(elVoid+"tercera parte")
      ys -= cabeza
    }
    return elVoid
  }


  println(reflexiva(Set(1,2)))


}

object ejer3del2015 extends App{
import inform.util.aleatorios._

  case class Banach(semilla : Int,var n1 : Int,var n2 : Int){
    //require(n1> -1 && n2 > -1)
    val alt = Aleatorio(semilla)
    var acum = 0
    while (n1 != 0 && n2 != 0) {
      acum += 1
      val num = alt.entero(0,1)
      if(num == 1) n1 = n1 - 1 else n2 = n2 - 1
    }

    def quedan : Int =  if(n1 == 0) n2 else n1
    def sacadas : Int = acum

  }
  class Subclase(var semilla2 : Int,var n3 : Int) extends Banach(semilla2,n3,n3) {
  }

  def prueba(k : Int, n : Int) : Unit = {
    var exitos =0
    for(i <- 1 to 10000){
      val xs = new Subclase(i,n)
      if(xs.quedan == k) exitos += 1
    }
    return println("La probabilidad es de %.2f".format(exitos.toDouble / 10000))

  }
println(prueba(4,5))
}











////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Junio 2013
/*
object ejercicio1del2013 extends App {

  def pertenece[A](elem : A,array : Array[A]) : Boolean ={
    var perte = false
    val longi = array.length
    var contador = 0
    while(contador < longi && perte == false) {
      if (array(contador) == elem)
        perte = true
      else {
        contador += 1
      }

    }
    return perte
  }
  pertenece(1, Array(3,7,1,1))
  pertenece(true, Array(false,false))

  def esPermutacion( array : Array[Int]) : Boolean = {
    var seSigue = true
    var elemento = 0
    while(seSigue && elemento < array.length){
      var vamosBien = false
      var posicion = 0
      do{ if(array(posicion) == elemento)
      { vamosBien = true
        elemento += 1}  else
      { if(posicion == array.length-1)
      {seSigue = false}
      else {posicion += 1}}
      } while(vamosBien == false && seSigue)
    }
    return seSigue


  }
  println(esPermutacion(Array[Int](3,1,0,2)))
}

object ej3de2013 extends App {
  import scala.collection.mutable.Queue

  def hamming(n :Int) : List[Int] = {
    var lista = List[Int]()
    var cola2 = new Queue[Int]()
    var cola3 = new Queue[Int]()
    var cola5 = new Queue[Int]()
    cola2.enqueue(1)
    cola3.enqueue(1)
    cola5.enqueue(1)
    for(i <- 1 to n){
      var menor = List[Int](cola2.front,cola3.front,cola5.front).min
      lista = lista :+ menor
      if(cola2.front == menor) cola2 = cola2.tail
      if(cola3.front == menor) cola3 = cola3.tail
      if(cola5.front == menor) cola5 = cola5.tail
      cola2.enqueue(menor*2)
      cola3.enqueue(menor*3)
      cola5.enqueue(menor*5)
    }
    return lista.sorted
  }

  print(hamming(20))
}

object ej4de2013 extends App {

  case class BigNat(num : String){
    def +(that : BigNat) : BigNat= {
      var meLLevo = 0
      var n1 = num.reverse
      var n2 = that.num.reverse
      var menor = List[Int](n1.length,n2.length).min

      var n3 : String = ""
      for(i <- 0 until menor){
        val suma = n1(i).toString.toInt + n2(i).toString.toInt + meLLevo
        val resto = suma - suma / 10 * 10
        n3 = (resto).toString + n3
        meLLevo = suma / 10

      }
      while(meLLevo != 0){
        if(n1.length > n2.length){

          val suma = n1(menor).toString.toInt + meLLevo
          val resto = suma - suma / 10 * 10
          n3 = (resto).toString + n3
          meLLevo = suma / 10
          menor += 1
        } else {
          val suma = n2(menor).toString.toInt + meLLevo
          val resto = suma - suma / 10 * 10
          n3 = (resto).toString + n3
          meLLevo = suma / 10
          menor += 1

        }
      }
      n3 = (n1.drop(menor)).reverse ++ (n2.drop(menor)).reverse ++ n3
      return BigNat(n3)
    }

  }


  val n1 = new BigNat("7813678136786126816812678136781367861268168126")
  val n2 = new BigNat("7565612575656125756561257565612575656125756561257565612575656125")
  val n3 : BigNat = n1 + n2
  println(n3)



}

*/
////////////////////////////////////////////////////////////////////////////////
//////////////////// Examen Julio 2011
/*

object ejer4 extends App {
  import java.util.Scanner
  import java.io.File

  def cuatroOmas(nombre : String) : Int = {
    val fichero = new File(nombre)
    val scLn = new Scanner(fichero).useDelimiter("[^a-zA-ZáéíóúñÁÉÍÓÚÑ]+")
    var contador = 0
    while(scLn.hasNext()){
      var longi = scLn.next().length
      if(longi == 4) contador += 1
    }
    return contador

  }

  println(cuatroOmas("MiFichero.txt"))

}
*/


object prueba extends App {


  def congruenciaConUnoelevadoA(n : Int,e : Int) : List[Int] = {
    var lista : List[Int]= List()
    for(i <- 1 until n){
      var exp = 1
      for(j <- 1 to e){
        exp *= i
      }
      if(exp % n == 1) lista = i+: lista
    }
    return  lista
  }

  println(congruenciaConUnoelevadoA(21,2))
}




































































