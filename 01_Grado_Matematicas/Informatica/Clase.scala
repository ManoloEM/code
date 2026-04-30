//import inform.util.aleatorios._

//import EjemploEntradaYSalida.x
///////////////////////////////////////////////////////////////////////////////
// DIA 1
/*
object EjemploEntradaYSalida extends App {

  import scala.io.StdIn._

  val x : Int = 10
  var y : Int = 0

  println(10 + 5)
  print(" ")
  println(x)
 // En la x no pone le .toString porque el programa te lo reconoce (al igual que la y)
  println("el numero "+y.toString+" no es igual a "+x )

  println("Dame tu nick: ")
   val str = readLine()
   println("No sabia que eso era un nombre, "+str)


  println("Cuantos años tienes "+str)
   val n = readInt()
   println(str+" nunca lo hubiera dicho, enserio que tienes "+n.toString)

  var opt3 : Option[Int] = None

  val  h = opt3 match {
    case None => 0
    case Some(x) => x

      println(h)


  var xs = List(10,20)

  val z = xs match {
    case List() => 0
    case List(x) => x * x
    case List(x,y) => x * y


  }
  println(z)



  def suma(xs : List[Int]): Int = xs match {
    case List() => 0
    case y::ys => y + suma(ys)
  }

  println(suma(List(1,2,3,4)))


  def enOrden(xs : List[Int]): Boolean = xs match {
    case List() => true
    case List(x) => true
    case y::z::vs => if (y <= z && enOrden(z::vs)) true else false
  }

  println(enOrden(List(1,1,1,2,3,3,2,4)))

  }

}


///////////////////////////////////////////////////////////////////////////////
// DIA 2

object segundodia extends App {


  val f = 7 + 2
  val z = {
    val y = 2 * 2
    val h = y * f
    h ^ (h-1) }
  println(f)
  //no furula
  //var funcion = while (i<20) println("quedan 21 min")
  def factorial(x:Int): Long = if (x == 0) 1 else x * factorial(x-1)
  println(factorial(912))
  }

*/
///////////////////////////////////////////////////////////////////////////////
// DIA 3
/*
object  tercerdia extends App {
   import .util.aleatorios._

  for(i <- 1 to 10 by 2) {
    println(i)

  }

  def experimento(semilla : Int) : Int = {
    val alt = Aleatorio(semilla)

  }
*/

object TiradasDado extends App {

  // importamos la biblioteca para generación de valores aleatorios
  import inform.util.aleatorios._

  // Dada una semilla para el experimento aleatorio, esta función
  // devuelve en nº de tiradas previas que necesitamos realizar
  // con el dado hasta obtener el primer seis (previas significa
  // que la tirada donde sale el primer seis no se cuenta).
  // Pasando distintas semillas, podemos realizar distintas
  // simulaciones del proceso
  def experimento(semilla: Int): Int = {
    val alt = Aleatorio(semilla) // crea un objeto para generar aleatorios con la semilla dada
    var tiradas = 0              // esta variable va a contar el nº de tiradas del dado
    var encontrado = false       // este centinela pasará a valer true cuando salga el primer seis
    while (!encontrado) {        // mientras el seis no haya salido
      val d = alt.uniforme(1, 7) // tiramos un dado (obtener un valor aleatorio uniforme entre 1 y 6)
      encontrado = d == 6        // si ha salido un seis, encontrado pasa a valer true
      if (!encontrado)           // si no ha salido un seis aún, contabilizados esta tirada
        tiradas += 1
    }
    return tiradas               // cuando acabe el bucle, la variable tiradas contiene el resultado
  }


  // vamos a realizar 1 millón de experimentos distintos
  val númeroExperimentos = 1000000
  // creamos un array de enteros con 1 millón de casillas.
  // En cada casilla guardaremos el resultado de cada uno
  // de los experimentos a realizar
  val resultados = new Array[Int](númeroExperimentos)

  // Usando 1 millón de semillas distintas
  for (s <- 0 until númeroExperimentos) {
    // realizamos el experimento con la correspondiente semilla y obtenemos el resultado
    val r = experimento(s)
    // guardamos el resultado del experimento con semilla s en la casilla s del array
    resultados(s) = r
  }

  // Esta función tomará el array que contiene los resultados de los experimentos
  // y calculará varias estadísticas sobre éstos:
  //   * El valor promedio o media (https://es.wikipedia.org/wiki/Media_aritm%C3%A9tica)
  //   * La desviación estándar (https://es.wikipedia.org/wiki/Desviaci%C3%B3n_t%C3%ADpica)
  //   * El valor mínimo
  //   * El valor máximo
  def estadísticas(xs: Array[Int]): (Double, Double, Int, Int) = {
    require(xs.length>0, "El array debe contener algún elemento")

    // sumamos en la variable suma todos los resultados
    var suma = 0
    for (i <- 0 until xs.length)
      suma = suma + xs(i)

    // y calculamos la media aritmética (como suma es entero, hay que pasar a Double antes de hacer la división)
    val media = suma.toDouble / xs.length

    // buscamos el valor mínimo
    var mínimo = xs(0)            // en principio, consideramos como mínimo el valor en la casilla 0
    for (i <- 1 until xs.length)  // miramos las demás casillas
      if (xs(i) < mínimo)         // si el valor en dicha casilla es menor al mínimo
        mínimo = xs(i)            // el mínimo pasa a ser dicho valor

    // buscamos el valor máximo de forma análoga
    var máximo = xs(0)
    for (i <- 1 until xs.length)
      if (xs(i) > máximo)
        máximo = xs(i)

    // para calcular la desviación, sumamos los cuadrados de la diferencia de los valores con la media
    var sCuadDesv = 0.0
    for (i <- 0 until xs.length)
      sCuadDesv = sCuadDesv + scala.math.pow(xs(i) - media, 2)

    // dividimos por el nº de valores y tomamos raíz cuadrada
    val desviación = scala.math.sqrt(sCuadDesv / xs.length)

    // devolvemos una tupla con las cuatro estadísticas
    return (media, desviación, mínimo, máximo)
  }


  // llamamos a la función anterior para obtener las estadísticas
  val (m, d, min, max) = estadísticas(resultados)

  // y las mostramos por pantalla
  println("La media de tiradas en los experimentos ha sido: "+m)
  println("La desviación ha sido: "+d)
  println("El menor número de tiradas en los experimentos ha sido: "+min)
  println("El mayor número de tiradas en los experimentos ha sido: "+max)


  // mostramos un histograma con los resultados de los experimentos
  // (lo veremos en detalle en un tema posterior)
  import inform.graphics.plot._
  val chart = HistogramChart("Sacar un 6"
    , "nº de tiradas necesarias"
    , "Frecuencia relativa"
    , resultados, buckets=max)
  chart.config(relativeFreq=true)
  chart.draw(800, 600)
}

///////////////////////////////////////////////////////////////////////////////
// DIA 4

object dia4 extends App {
  import inform.graphics.draw2D._
  import inform.graphics.color._

  val w = GraphicsWindow(450,450)
  w.setColor(Color.red)
  w.draw(Rectangle(-200,-100,150,200))
  w.setColor(Color.green)
  w.fill(Rectangle(50,20,150,75))
  val rect = Rectangle(50,-100,75,75)
  val pincel = Stroke(10)
  w.setStroke(pincel)
  w.setColor(Color.yellow)
  w.fill(rect)
  w.setColor(Color.blue)
  w.draw(rect)

  def dibuja(g2D : Graphics2D) {
    g2D.setColor(Color.red)
    g2D.draw(Ellipse(-200,-100,150,200))
    g2D.setColor(Color.green)
    g2D.fill(Ellipse(50,20,150,75))
    val elipse = Ellipse(50,-100,75,75)
    val pincel = Stroke(10)
    g2D.setStroke(pincel)
    g2D.setColor(Color.yellow)
    g2D.fill(elipse)
    g2D.setColor(Color.blue)
    g2D.draw(elipse)
  }
  val wind = GraphicsWindow(600,600)
  wind.drawWith(dibuja)
/*
  def dibujo(m : Graphics2D) {
    m.setColor(Color.orange)
    m.draw(Rectangle(0,0,-200,-150))
    m.setColor(Color.black)
    m.fill(Rectangle(0,0,-200,-150))
  }

  val wind = GraphicsWindow(600,600)
  wind.drawWith(dibujo)


*/
}

///////////////////////////////////////////////////////////////////////////////
// DIA 5

import inform.graphics.plot._
import inform.graphics.color._

object EjTarta extends App {
  val pieDataset = PieDataset()
  pieDataset += ("Suspenso", 103)
  pieDataset += ("Aprobado", 11)
  pieDataset += ("Notable", 5)
  pieDataset += ("Sobresaliente", 1)
  val chart = PieChart("Notas", pieDataset)
  chart.draw(600, 400) }





