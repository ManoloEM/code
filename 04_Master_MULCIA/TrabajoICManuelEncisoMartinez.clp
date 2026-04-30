;;;============================================================================
;;;
;;; Trabajo: Juego de piezas deslizantes
;;; 
;;; Asignatura: Ingeniería del Conocimiento del MULCIA Universidad de Sevilla
;;;
;;; Autor: Manuel Enciso Martínez
;;; DNI: ************
;;;
;;;============================================================================

;;;============================================================================
;;; MODULO MAIN: Definición de estructuras y datos iniciales
;;;============================================================================

(defmodule MAIN (export ?ALL))

;;; Plantilla para las casillas del tablero
(deftemplate MAIN::casilla
   (slot fila (type INTEGER) (range 1 4) (default ?NONE))
   (slot columna (type INTEGER) (range 1 4) (default ?NONE))
   (slot valor (allowed-values 0 1 2 3 4 5 6 7 8 9 10 11 A B X) (default ?NONE))) ;Añadimos allowed-values, para restringir los valores según el problema dado

;;; Plantilla para control del fases y modo de juego.
;;; llevar la cuenta de los movimientos nos sera util para
;;; actualizar el estado incluso cuando los movimientos sean
;;; invalidos, para activar de nuevo reglas de seleccion
(deftemplate MAIN::estado
   (slot fase (allowed-symbols inicio validacion jugando fin) (default inicio))
   (slot modo (allowed-symbols manual auto sin-elegir) (default sin-elegir))
   (slot movimientos (type INTEGER) (default 0)))

;;; Hecho inicializacion de la fase
(deffacts MAIN::inicializacion
   (estado (fase inicio)))

;;; He completado con los 3 posibles tableros (variando letras dentro o fuera del núcleo) para hacer pruebas
;;; Tableros de control (para comprobar que resuelve correctamente distintas disposiciones)
;;; Tablero original del enunciado (Letra dentro y fuera)
(deffacts MAIN::tablero
   ;; Fila 1
   (casilla (fila 1) (columna 1) (valor 6))
   (casilla (fila 1) (columna 2) (valor 11))
   (casilla (fila 1) (columna 3) (valor 3))
   (casilla (fila 1) (columna 4) (valor 10))
   ;; Fila 2
   (casilla (fila 2) (columna 1) (valor 1))
   (casilla (fila 2) (columna 2) (valor X)) ; FIJO
   (casilla (fila 2) (columna 3) (valor 0)) ; HUECO ORIGINAL
   (casilla (fila 2) (columna 4) (valor 5))
   ;; Fila 3
   (casilla (fila 3) (columna 1) (valor 8))
   (casilla (fila 3) (columna 2) (valor A))
   (casilla (fila 3) (columna 3) (valor X)) ; FIJO
   (casilla (fila 3) (columna 4) (valor B))
   ;; Fila 4
   (casilla (fila 4) (columna 1) (valor 9))
   (casilla (fila 4) (columna 2) (valor 2))
   (casilla (fila 4) (columna 3) (valor 7))
   (casilla (fila 4) (columna 4) (valor 4)))

; ;;; Tablero con A y B fuera
; (deffacts MAIN::tablero
;    ;; Fila 1
;    (casilla (fila 1) (columna 1) (valor 6))
;    (casilla (fila 1) (columna 2) (valor 11))
;    (casilla (fila 1) (columna 3) (valor 3))
;    (casilla (fila 1) (columna 4) (valor 10))
;    ;; Fila 2
;    (casilla (fila 2) (columna 1) (valor 1))
;    (casilla (fila 2) (columna 2) (valor X)) ; FIJO
;    (casilla (fila 2) (columna 3) (valor 0)) ; HUECO 
;    (casilla (fila 2) (columna 4) (valor 5))
;    ;; Fila 3
;    (casilla (fila 3) (columna 1) (valor A)) 
;    (casilla (fila 3) (columna 2) (valor 8))
;    (casilla (fila 3) (columna 3) (valor X)) ; FIJO
;    (casilla (fila 3) (columna 4) (valor B))
;    ;; Fila 4
;    (casilla (fila 4) (columna 1) (valor 9))
;    (casilla (fila 4) (columna 2) (valor 2))
;    (casilla (fila 4) (columna 3) (valor 7))
;    (casilla (fila 4) (columna 4) (valor 4)))

; ;;; Tablero con A y B dentro
; (deffacts MAIN::tablero
;    ;; Fila 1
;    (casilla (fila 1) (columna 1) (valor 6))
;    (casilla (fila 1) (columna 2) (valor 11))
;    (casilla (fila 1) (columna 3) (valor 3))
;    (casilla (fila 1) (columna 4) (valor 10))
;    ;; Fila 2
;    (casilla (fila 2) (columna 1) (valor 1))
;    (casilla (fila 2) (columna 2) (valor X)) ; FIJO
;    (casilla (fila 2) (columna 3) (valor A)) 
;    (casilla (fila 2) (columna 4) (valor 5))
;    ;; Fila 3
;    (casilla (fila 3) (columna 1) (valor 0)) ; HUECO
;    (casilla (fila 3) (columna 2) (valor B))
;    (casilla (fila 3) (columna 3) (valor X)) ; FIJO
;    (casilla (fila 3) (columna 4) (valor 8))
;    ;; Fila 4
;    (casilla (fila 4) (columna 1) (valor 9))
;    (casilla (fila 4) (columna 2) (valor 2))
;    (casilla (fila 4) (columna 3) (valor 7))
;    (casilla (fila 4) (columna 4) (valor 4)))

;;; Regla de inicio
(defrule MAIN::inicio
   ?h <- (estado (fase inicio))
   =>
   (modify ?h (fase validacion))
   (focus DIBUJAR VALIDACION))

;;;============================================================================
;;; MODULO DIBUJAR: Mostrar por pantalla el tablero
;;;============================================================================
(defmodule DIBUJAR (import MAIN ?ALL) (export ?ALL))

;;; Mostramos por pantalla el tablero
(deffunction formato (?v)
   (if (eq ?v 0) then "  "                     ; Si es 0 (hueco), imprime espacios
    else (if (eq ?v X) then "XX"               ; Si es X, imprime XX
     else (if (not (numberp ?v)) then          ; Si NO es numero (es A o B)
            (str-cat " " ?v)                   ; Imprime " A" o " B" con espacio
           else                                ; Si ES numero (1-11)
            (if (< ?v 10) then (str-cat " " ?v); Un digito: añade espacio
             else (str-cat ?v ""))))))         ; Dos digitos: imprime tal cual

(defrule DIBUJAR::pintar
   (casilla (fila 1) (columna 1) (valor ?v11)) (casilla (fila 1) (columna 2) (valor ?v12))
   (casilla (fila 1) (columna 3) (valor ?v13)) (casilla (fila 1) (columna 4) (valor ?v14))
   (casilla (fila 2) (columna 1) (valor ?v21)) (casilla (fila 2) (columna 2) (valor ?v22))
   (casilla (fila 2) (columna 3) (valor ?v23)) (casilla (fila 2) (columna 4) (valor ?v24))
   (casilla (fila 3) (columna 1) (valor ?v31)) (casilla (fila 3) (columna 2) (valor ?v32))
   (casilla (fila 3) (columna 3) (valor ?v33)) (casilla (fila 3) (columna 4) (valor ?v34))
   (casilla (fila 4) (columna 1) (valor ?v41)) (casilla (fila 4) (columna 2) (valor ?v42))
   (casilla (fila 4) (columna 3) (valor ?v43)) (casilla (fila 4) (columna 4) (valor ?v44))
   =>
   (printout t "+----+----+----+----+" crlf)
   (printout t "| " (formato ?v11) " | " (formato ?v12) " | " (formato ?v13) " | " (formato ?v14) " |" crlf)
   (printout t "+----+----+----+----+" crlf)
   (printout t "| " (formato ?v21) " | " (formato ?v22) " | " (formato ?v23) " | " (formato ?v24) " |" crlf)
   (printout t "+----+----+----+----+" crlf)
   (printout t "| " (formato ?v31) " | " (formato ?v32) " | " (formato ?v33) " | " (formato ?v34) " |" crlf)
   (printout t "+----+----+----+----+" crlf)
   (printout t "| " (formato ?v41) " | " (formato ?v42) " | " (formato ?v43) " | " (formato ?v44) " |" crlf)
   (printout t "+----+----+----+----+" crlf))
;*He tenido que modificar el codigo para representar, no me funcionaba correctamente

;;;============================================================================
;;; MODULO VALIDACION: Validacion del tablero 
;;;============================================================================

(defmodule VALIDACION (import MAIN ?ALL) (import DIBUJAR ?ALL) (export ?ALL))


;;; Regla para comprobar que que las casillas fijas se encuentran en las posiciones (2,2) y (3,3) unicamente
(defrule VALIDACION::comprueba-fijas
   (or (casilla (fila 2) (columna 2) (valor ~X)) ;comprobar (2,2) y (3,3) tiene algun valor distinto a X
       (casilla (fila 3) (columna 3) (valor ~X)))
   =>
   (printout t "ERROR: Las casillas (2,2) y (3,3) deben ser fijas (X)." crlf)
   (halt))

(defrule VALIDACION::comprueba-fijas-triplicadas
   (casilla (fila ?f) (columna ?c) (valor X))
   (test (not (or (and (eq ?f 2) (eq ?c 2)) (and (eq ?f 3) (eq ?f 3)) ))) ;comprobar existencia otra casilla X disntinta de (2,2) o (3,3) 
   =>
   (printout t "ERROR: La casilla ("(formato ?f)","(formato ?c)") no pueden ser fijas (X)." crlf)
   (halt))

;;; Regla para comprobar que no hay números/letras duplicadas
(defrule VALIDACION::comprueba-duplicados
   (casilla (fila ?f1) (columna ?c1) (valor ?v&~X))
   (casilla (fila ?f2) (columna ?c2&:(or (neq ?f1 ?f2) (neq ?c1 ?c2))) (valor ?v))
   =>
   (printout t "ERROR: Valor duplicado en el tablero en casillas ("(formato ?f1)","(formato ?c1)") y ("(formato ?f2)","(formato ?c2)"): " ?v crlf)
   (halt))

;;; Regla de verificación, si ninguna de las anteriores se activó. Todo esta correcto.
(defrule VALIDACION::tablero-correcto
   (declare (salience -10))
   ?h <- (estado (fase validacion))
   =>
   (printout t "Tablero válido." crlf)
   (modify ?h (fase jugando))
   (focus JUEGO))

;;;============================================================================
;;; MODULO JUEGO: Modo de juego y resolucion
;;;============================================================================

(defmodule JUEGO (import MAIN ?ALL) (import DIBUJAR ?ALL) (import VALIDACION ?ALL) (export ?ALL))

;;; Preguntar modo de juego
(defrule JUEGO::elegir-modo
   ?h <- (estado (modo sin-elegir))
   =>
   (printout t "Elige si quieres jugar manual o automatico: (m/a)" )
   (bind ?resp (read))
   (if (eq ?resp m) then (modify ?h (modo manual))
    else (if (eq ?resp a) then (modify ?h (modo auto))
     else (printout t "Opcion no valida." crlf))))

;;; Detectar FINAL DEL JUEGO 
;;; Comprobar con prioridad maxima si el tablero se encuentra ordenado
(defrule JUEGO::meta-alcanzada
   (declare (salience 100))
   (estado (fase jugando))
   ;; Fila 1: 1, 2, 3, 4
   (casilla (fila 1) (columna 1) (valor 1)) (casilla (fila 1) (columna 2) (valor 2))
   (casilla (fila 1) (columna 3) (valor 3)) (casilla (fila 1) (columna 4) (valor 4))
   ;; Columna 4 (hacia abajo): 5, 6, 7
   (casilla (fila 2) (columna 4) (valor 5)) (casilla (fila 3) (columna 4) (valor 6))
   (casilla (fila 4) (columna 4) (valor 7))
   ;; Fila 4 (hacia izq): 8, 9, 10
   (casilla (fila 4) (columna 3) (valor 8)) (casilla (fila 4) (columna 2) (valor 9))
   (casilla (fila 4) (columna 1) (valor 10))
   ;; Columna 1 (hacia arriba): 11, Hueco (0)
   (casilla (fila 3) (columna 1) (valor 11))
   (casilla (fila 2) (columna 1) (valor 0))
   ;; Letras A y B deben quedar en los espacios resultantes. Como da igual la posición entre (2,3) y (3,2) no hace falta comprobar nada más.
   =>
   (printout t "Se ha completado correctamente el tablero." crlf)
   (halt))

;;;============================================================================
;;; MODO AUTOMÁTICO: Resolucion automática
;;;============================================================================
;; Estrategia de resolución:
; Siguiendo las instrucciones del enunciado, vamos a implementar distintas fases para repetir en bucle los siguientes pasos:
; 1º Comprobar A y B estan en las casillas seguras/buffer (2,3) y (3,2)
; 2º Mover el número n a ordenar a la casilla seguro (2,3). He distinguido entre dos casos para asegurarme que siempre mantenga el orden de los numeros que ya tengo ordenados 
; (se podría intentar implementar una estrategia que no distinga de orden, pero no estaba seguro al comienzo de que no se iba a desordenar. Y de este modo si lo estaba, aunque lo complica un poco)

; ; Caso 1: Si n se encuentra próximo en sentido horario, lo metemos en (2,3) desde (1,3) 
; SENTIDO HORARIO (distancia máxima 2 )
;      +----+----+----+----+        +----+----+----+----+   
;      | 2  | 4  | 3  | x  |        | 2  | 4  |    | x  |
;      +----+----+----+----+        +----+----+----+----+      
;      | 1  |||||| B  |    |        | 1  |||||| 3  | B  | 
;      +----+----+----+----+        +----+----+----+----+ 
;  --> | x  | A  |||||| x  |   -->  | x  | A  |||||| x  |  
;      +----+----+----+----+        +----+----+----+----+
;      | x  | x  | x  | x  |        | x  | x  | x  | x  | 
;      +----+----+----+----+        +----+----+----+----+   

; ; Caso 2: Si n se encuentra próximo en sentido antihorario, lo metemos en (2,3) desde (2,4) 
; SENTIDO ANTIHORARIO (siempre que no sea horario)
;      +----+----+----+----+        +----+----+----+----+   
;      | x  | x  |    | x  |        | x  | x  | B  | x  |
;      +----+----+----+----+        +----+----+----+----+      
;      | x  |||||| B  | 3  |        | x  |||||| 3  |    | 
;      +----+----+----+----+        +----+----+----+----+ 
;  --> | x  | A  |||||| 1  |   -->  | x  | A  |||||| 1  |  
;      +----+----+----+----+        +----+----+----+----+
;      | x  | x  | x  | 2  |        | x  | x  | x  | 2  | 
;      +----+----+----+----+        +----+----+----+----+   

; 3º Rotar la sucesion ordenada al lugar correspondiente e intrudcir el n en su orden. Pasar a n+1 y repetir desde el 1º paso hasta n= 10
; 4º Para n=10 es más complejo y no he conseguido unirlo con el resto de reglas. Hay que usar los buffers (2,3) y (3,2) en caso de que 10 y 11 esten desordenados (implemento una secuencia de reglas)

;; *Comentarios sobre el código:
; Por falta de tiempo, no le he podido dedicarle todo el tiempo que hubiera requerido para mejorar el rendimiento y claridad del codigo. Aun asi me gustaría comentar varias mejoras que he querido añadir y no he consigo:
; 1) No siempre rotar sentido horario. Sería mas conveniente saber cuando rotar en sentido antihorario reduce los movimientos (se podría utilizar una funcion auxiliar que calcule distancias y devuelva el sentido minimo)
; 2) No siempe usar el hueco en (2,3) para las permutaciones. Sería mas conveniente también estudiar en que ocasiones nos encontramos más cerca del (3,2) y ahorrarnos movimientos.
; 3) Podría haberse implementado que una sucesion de inputs modo: 'd' 'b' 'i' 'a' se traduzcan a una sucesion de movimientos para ahorrarnos implementaciones de reglas secuenciales.
; 4) Mejor eficiencia para RETE si estudiamos cuales son las condiciones más restrictivas y las ponemos primero. Además de remplazar (test ...) por condiciones en las variables (esto último me ha dado problemas y por eso he continuado con test para el funcionamiento correcto)
;;;============================================================================
;;; PLANTILLAS Y ESTRUCTURAS DE CONTROL
;;;============================================================================

;;; Plantilla para controlar la fase actual de la resolución
(deftemplate JUEGO::control-fase
   (slot fase 
      (allowed-symbols 
         ORDENAR-N             ; Fase 1: Verificar si N está colocado
         ORDENAR-A-B           ; Fase 2: Asegurar pivotes A y B en el centro
         ORDENAR-PIEZA         ; Fase 3: Llevar N al buffer (2,3)
         COLOCAR-N             ; Fase 4: Insertar N en su sitio desde el buffer
         ESPECIAL-10-PREPARAR  ; Inicio secuencia del 10
         ESPECIAL-10-METER     ; Meter 10 al buffer
         ESPECIAL-10-MANIOBRA-1; Primera rotación y ajuste
         ESPECIAL-10-MANIOBRA-2; Segunda rotación y ajuste
         ESPECIAL-10-FIN)      ; Bucle final
      (default ORDENAR-N)))

;;; Plantilla para solicitar movimientos específicos (A, B o Numero N)
(deftemplate JUEGO::objetivo-mov
   (slot pieza)           ; Valor: A, B o numero 1..11
   (slot destino-f)       ; Fila destino
   (slot destino-c))      ; Columna destino

;;;============================================================================
;;; FUNCIÓN DE ANÁLISIS DE POSICIÓN: calcular-sentido
;;;============================================================================
;;; Determina si un número está ordenado o qué rotación necesita
;;; Entrada: ?v (valor actual), ?n (número a ordenar como referencia del sentido)
;;; Contruimos una lista con los valores ordenados y comprobamos en que posicion se situa el valor ?v
;;; Nos será útil para poder ordenar los números (ya que no podemos resolver de la misma manera si el 
;;; valor se encuentra adyacente sentido antihorario que adyacente sentido horario)
(deffunction JUEGO::calcular-sentido (?v ?n)

   (bind ?lista (create$))
   
   ;; Coordenadas del anillo en orden horario
   (bind ?coords (create$ 1 1  1 2  1 3  1 4  
                          2 4  3 4  4 4  
                          4 3  4 2  4 1  
                          3 1  2 1))
   
   ;; Iteramos para sacar los valores del tablero
   (loop-for-count (?i 1 12) do
      (bind ?f (nth$ (- (* ?i 2) 1) ?coords)) ; Fila
      (bind ?c (nth$ (* ?i 2) ?coords))       ; Columna
      
      ;; Buscamos el hecho casilla correspondiente
      (do-for-all-facts ((?casilla casilla)) 
         (and (= ?casilla:fila ?f) (= ?casilla:columna ?c))
         (bind ?lista (create$ ?lista ?casilla:valor)))
   )

   ;; Determinar la referencia (n-1).
   (bind ?ref (- ?n 1))
   
   (bind ?pos-ref FALSE)
   (bind ?pos-val FALSE)
   
   ;; Buscamos indices en la lista (1..12)
   (loop-for-count (?i 1 12) do
      (bind ?elem (nth$ ?i ?lista))
      (if (eq ?elem ?ref) then (bind ?pos-ref ?i))
      (if (eq ?elem ?v) then (bind ?pos-val ?i))
   )
   
   ;; Si no encuentra referencia (ej: buscando el 1 y el 0 no cuenta), devolvemos error o default
   (if (eq ?pos-ref FALSE) then (return "Error-Referencia"))
   (if (eq ?pos-val FALSE) then (return "Error-Valor"))
   
   ;; Contar distancia hacia la derecha (bucle) saltando los 0
   (bind ?distancia 0)
   (bind ?indice ?pos-ref)
   (bind ?encontrado FALSE)
   
   ;; Recorremos maximo 12 veces para evitar bucles infinitos
   (loop-for-count (?k 1 12) do
      (if (eq ?encontrado TRUE) then (break))
      
      ;; Avanzamos indice (modulo 12)
      (bind ?indice (+ ?indice 1))
      (if (> ?indice 12) then (bind ?indice 1))
      
      (bind ?elemento-actual (nth$ ?indice ?lista))
      
      ;; Si encontramos el valor objetivo, paramos
      (if (eq ?elemento-actual ?v) then 
          (bind ?encontrado TRUE)
          (break))
      
      ;; Si NO es 0 (hueco), incrementamos contador
      (if (neq ?elemento-actual 0) then
          (bind ?distancia (+ ?distancia 1)))
   )
   
   ;; Evaluar retorno segun reglas del enunciado

   
   ;; "Devuelve Horario: si está en 2º o 1º posición continuando la secuencia"
   ;;  Significa que hay 0 o 1 numero en medio (distancia <= 1)
   (if (<= ?distancia 1) then (return "Horario"))
   
   ;; "Devuelve Antihorario: Resto de situaciones"
   (return "Antihorario")
)

;;;============================================================================
;;; INICIALIZACIÓN DEL MODO AUTOMÁTICO
;;;============================================================================

;;; Inicialización: Al entrar en modo auto, arrancamos la Fase 1 y el contador N
(defrule JUEGO::inicio-auto
   (declare (salience 20))
   (estado (modo auto) (fase jugando))
   (not (control-fase))
   =>
   (printout t ">>> INICIO AUTOMATICO" crlf)
   (assert (control-fase (fase ORDENAR-N)))
   (assert (ordenar-n 2)))

;;;============================================================================
;;; FASE 1: ORDENAR-N
;;;============================================================================
;;; Objetivo: Verificar si cada número (2 a 9) ya está colocado en secuencia
;;; Si está ordenado, incrementa N; si no, pasa a preparar A y B

;;; Comprobar si el número actual N está en su posición correcta
(defrule JUEGO::fase-comprobar-orden
   (declare (salience 20))
   ?f <- (control-fase (fase ORDENAR-N))
   ?o <- (ordenar-n ?n&:(<= ?n 9)) 
   
   ;; Comprobamos si N ya está en su sitio correcto.
   (casilla (fila ?f_act) (columna ?c_act) (valor ?n))
      
      ;; Caso N>1: Correcto si sigue a N-1
           (casilla (fila ?f_prev) (columna ?c_prev) (valor ?prev&:(eq ?prev (- ?n 1))))
           (test (or (and (= ?f_prev 1) (< ?c_prev 4) (= ?f_act 1) (= ?c_act (+ ?c_prev 1)))  ; Fila 1
                     (and (= ?c_prev 4) (< ?f_prev 4) (= ?f_act (+ ?f_prev 1)) (= ?c_act 4))  ; Col 4
                     (and (= ?f_prev 4) (> ?c_prev 1) (= ?f_act 4) (= ?c_act (- ?c_prev 1)))  ; Fila 4
                     (and (= ?c_prev 1) (> ?f_prev 1) (= ?f_act (- ?f_prev 1)) (= ?c_act 1))  ; Col 1
         ))
   =>
   ;; Si está colocado, pasamos al siguiente número
   (printout t ">> Numero " ?n " ya colocado. Pasando al siguiente." crlf)
   (retract ?o)
   (assert (ordenar-n (+ ?n 1))))

;;; Si N NO está colocado correctamente, pasamos a Fase 2 (Preparar A/B)
(defrule JUEGO::fase-1-pasar-a-fase-2
   (declare (salience 10))
   ?f <- (control-fase (fase ORDENAR-N))
   (ordenar-n ?n)
   ;; Condición negativa: No está colocado (simplificada para activar el cambio)
   =>
   (printout t ">> El numero " ?n " no esta en su sitio. Asegurando A y B..." crlf)
   (modify ?f (fase ORDENAR-A-B)))

;;; Detección de llegada al número 10: cambia a secuencia especial
(defrule JUEGO::fase-1-fin
   (declare (salience 30))
   ?f <- (control-fase (fase ORDENAR-N))
   (ordenar-n 10)
   =>
   (printout t ">>> INICIANDO SECUENCIA ESPECIAL DEL 10 <<<" crlf)
   (modify ?f (fase ESPECIAL-10-PREPARAR)))

;;;============================================================================
;;; FASE 2: ORDENAR-A-B
;;;============================================================================
;;; Objetivo: Asegurar que las letras A y B están en posiciones centrales
;;; seguras (2,3) o (3,2) antes de continuar con la colocación de números

;;; Detectar si A está fuera de los centros y solicitar su colocación
(defrule JUEGO::1-A-fuera-recuperar
   (declare (salience 20))
   (control-fase (fase ORDENAR-A-B))
   (not (objetivo-mov)) ; Solo si no hay una orden en curso
   ;; A esta fuera de los centros
   (casilla (fila ?fa) (columna ?ca) (valor A))
   (test (or (neq ?fa 2) (neq ?ca 3)))
   (test (or (neq ?fa 3) (neq ?ca 2)))
   ;; Miramos donde esta B para no machacarla
   (casilla (fila ?fb) (columna ?cb) (valor B))
   =>
   ;; Si (2,3) no tiene a B, mandamos A a (2,3), si no a (3,2)
   (if (and (= ?fb 2) (= ?cb 3))
      then (assert (objetivo-mov (pieza A) (destino-f 3) (destino-c 2)))
      else (assert (objetivo-mov (pieza A) (destino-f 2) (destino-c 3)))))

;;; Detectar si B está fuera de los centros y solicitar su colocación
(defrule JUEGO::1-B-fuera-recuperar
   (declare (salience 20))
   (control-fase (fase ORDENAR-A-B))
   (not (objetivo-mov)) ; Solo si no hay una orden en curso
   ;; B esta fuera de los centros
   (casilla (fila ?fb) (columna ?cb) (valor B))
   (test (or (neq ?fb 2) (neq ?cb 3)))
   (test (or (neq ?fb 3) (neq ?cb 2)))
   ;; Miramos donde esta B para no machacbrla
   (casilla (fila ?fa) (columna ?ca) (valor A))
   =>
   ;; Si (2,3) no tiene a B, mandamos A a (2,3), si no a (3,2)
   (if (and (= ?fa 2) (= ?ca 3))
      then (assert (objetivo-mov (pieza B) (destino-f 3) (destino-c 2)))
      else (assert (objetivo-mov (pieza B) (destino-f 2) (destino-c 3)))))

;;; Verificar que A y B están seguras y pasar a Fase 3
(defrule JUEGO::fase-2-ok-pasar-3
   (declare (salience 10))
   ?f <- (control-fase (fase ORDENAR-A-B))
   (casilla (fila 2) (columna 3) (valor A|B))
   (casilla (fila 3) (columna 2) (valor A|B))
   (not (objetivo-mov))
   =>
   (printout t ">> A y B seguras. Pasando a ordenar pieza n." crlf)
   (modify ?f (fase ORDENAR-PIEZA)))

;;;============================================================================
;;; FASE 3: ORDENAR-PIEZA
;;;============================================================================
;;; Objetivo: Llevar el número N actual al buffer (2,3) mediante rotaciones
;;; del anillo exterior, preparándolo para su colocación final

;;; Generar objetivo de movimiento: llevar N al buffer (2,3)
(defrule JUEGO::fase-3-iniciar-movimiento
   (declare (salience 20))
   (control-fase (fase ORDENAR-PIEZA))
   (ordenar-n ?n)
   (not (objetivo-mov))
   =>
   (printout t ">> Objetivo: Aparcar " ?n " en buffer (2,3)." crlf)
   (assert (objetivo-mov (pieza ?n) (destino-f 2) (destino-c 3))))

;;; Verificar que N llegó al buffer y pasar a Fase 4
(defrule JUEGO::fase-3-completada
   (declare (salience 21))
   ?f <- (control-fase (fase ORDENAR-PIEZA))
   (ordenar-n ?n)
   ;; Verificamos si N ya llegó al buffer (2,3)
   (casilla (fila 2) (columna 3) (valor ?n))
   (not (objetivo-mov))
   =>
   (printout t ">> Pieza " ?n " aparcada. Colocamos " ?n " en su orden." crlf)
   (modify ?f (fase COLOCAR-N)))

;;;============================================================================
;;; FASE 4: COLOCAR-N
;;;============================================================================
;;; Objetivo: Insertar el número N desde el buffer (2,3) a su posición
;;; final en la secuencia mediante rotaciones hasta configuración correcta

;;; Rotar el anillo (numeros en el exterior) mientras no se alcance la configuración de inserción
(defrule JUEGO::actuador-rotar-pieza-f4
   (control-fase (fase COLOCAR-N))
   ;; Contexto: Queremos meter la pieza ?p en el centro (2,3)
   

   ;; Estado actual del hueco
   (casilla (fila ?fh) (columna ?ch) (valor 0))

   ;; Seguridad: No rotar si el hueco se metió en el centro por error
   (test (or (neq ?fh 2) (neq ?ch 3)))

   =>

   ;; ACCIÓN: Rotar anillo en sentido horario (d -> b -> i -> a)
   (bind ?mov nil)
   (if (and (= ?fh 1) (< ?ch 4)) then (bind ?mov d)
    else (if (and (= ?ch 4) (< ?fh 4)) then (bind ?mov b)
     else (if (and (= ?fh 4) (> ?ch 1)) then (bind ?mov i)
      else (if (and (= ?ch 1) (> ?fh 1)) then (bind ?mov a)
       ;; Sacar hueco si está atrapado en (2,3) o (3,2)
       else (if (= ?fh 2) then (bind ?mov d) else (bind ?mov i))))))

   (if (neq ?mov nil) then
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;; Insertar N cuando hueco en (1,3) y n-1 en (1,2): ejecutar 'b'
(defrule JUEGO::actuador-colocar-pieza
   (declare (salience 10))
   (ordenar-n ?n)
   ;;  Control de Fase estricto
   (control-fase (fase COLOCAR-N))

   
   ;; Verificamos que el hueco 0 está específicamente en (1,3)
   (casilla (fila 1) (columna 3) (valor 0))

   ;; n-1 esta en posicion (1,2)
   (casilla (fila 1) (columna 2) (valor ?prev&=( - ?n 1)))
   
   =>
   
   
   ;; Input 'b' (Abajo): Mueve el hueco de (1,3) a (2,3)
   (assert (mover b 1 3))

   
   ;; Gestión de Foco para ejecutar los movimientos
   (pop-focus)
   (focus MOVIMIENTO)
)

;;; Sacar N del buffer ejecutando 'd' cuando hueco en (2,3)
(defrule JUEGO::actuador-colocar-pieza-sacar-hueco
   (declare (salience 10))
   
   ;; Control de Fase estricto
   ?f <- (control-fase (fase COLOCAR-N))

   
   ;; Verificamos que el hueco (0) está específicamente en (1,3)
   (casilla (fila 2) (columna 3) (valor 0))

   
   =>
   
   ;; ACCIONES: Mandar input 'b' y luego 'd' [1-8]
   
   ;; Input 'd' (Derecha) el hueco estará en (2,3) tras el paso anterior.
   ;; así que generamos la orden para moverlo de (2,3) a (2,4)
   (assert (mover d 2 3))
   
   ;; Gestión de Foco para ejecutar los movimientos
   (modify ?f (fase ORDENAR-N))
   (pop-focus)
   (focus MOVIMIENTO)
)

;;;============================================================================
;;; SECUENCIA ESPECIAL: COLOCACIÓN DE LOS NÚMEROS 10 Y 11
;;;============================================================================
;;; Esta secuencia maneja el caso especial del número 10, que requiere
;;; maniobras específicas de intercambio de letras para completar el puzzle

;;;----------------------------------------------------------------------------
;;; PREPARACIÓN: Asegurar letras A y B en centros
;;;----------------------------------------------------------------------------

;;; Detectar si A está fuera de los centros (fase especial 10)
(defrule JUEGO::10-paso-1-asegurar-centros-failA
   (declare (salience 20))
   (control-fase (fase ESPECIAL-10-PREPARAR))
   (not (objetivo-mov)) ; Solo si no hay una orden en curso
   ;; A esta fuera de los centros
   (casilla (fila ?fa) (columna ?ca) (valor A))
   (test (or (neq ?fa 2) (neq ?ca 3)))
   (test (or (neq ?fa 3) (neq ?ca 2)))
   ;; Miramos donde esta B para no machacarla
   (casilla (fila ?fb) (columna ?cb) (valor B))
   =>
   ;; Si (2,3) no tiene a B, mandamos A a (2,3), si no a (3,2)
   (if (and (= ?fb 2) (= ?cb 3))
      then (assert (objetivo-mov (pieza A) (destino-f 3) (destino-c 2)))
      else (assert (objetivo-mov (pieza A) (destino-f 2) (destino-c 3)))))

;;; Detectar si B está fuera de los centros (fase especial 10)
(defrule JUEGO::10-paso-1-asegurar-centros-failB
   (declare (salience 20))
   (control-fase (fase ESPECIAL-10-PREPARAR))
   (not (objetivo-mov)) ; Solo si no hay una orden en curso
   ;; B esta fuera de los centros
   (casilla (fila ?fb) (columna ?cb) (valor B))
   (test (or (neq ?fb 2) (neq ?cb 3)))
   (test (or (neq ?fb 3) (neq ?cb 2)))
   ;; Miramos donde esta B para no machacbrla
   (casilla (fila ?fa) (columna ?ca) (valor A))
   =>
   ;; Si (2,3) no tiene a B, mandamos A a (2,3), si no a (3,2)
   (if (and (= ?fa 2) (= ?ca 3))
      then (assert (objetivo-mov (pieza B) (destino-f 3) (destino-c 2)))
      else (assert (objetivo-mov (pieza B) (destino-f 2) (destino-c 3)))))

;;; Verificar que A y B están OK y pasar a meter el 10
(defrule JUEGO::10-paso-1-asegurar-centros-ok
   (declare (salience 10))
   ?f <- (control-fase (fase ESPECIAL-10-PREPARAR))
   (casilla (fila 2) (columna 3) (valor A|B))
   (casilla (fila 3) (columna 2) (valor A|B))
   (not (objetivo-mov))
   =>
   (printout t ">> Centros asegurados. Pasando a meter el 10." crlf)
   (modify ?f (fase ESPECIAL-10-METER)))

;;;----------------------------------------------------------------------------
;;; COLOCACIÓN DEL 10: Llevar número 10 al buffer
;;;----------------------------------------------------------------------------

;;; Comprobar si estan todos los numeros ordenados (con prioridad)
(defrule JUEGO::10-paso-2-orden-10y11
   (declare (salience 30))
   ?f <- (control-fase (fase ESPECIAL-10-METER))
   (not (objetivo-mov))

   (test (eq (calcular-sentido 11 11) "Horario")) ; Esto implica que tenemos 11 y 10 seguidos (he puesto 11 11 porque el segundo 11 se toma 11 - 1 = 10 como referencia del orden)
   =>
   (printout t ">> Secuencia ordenada" crlf)
   (modify ?f (fase ESPECIAL-10-FIN)))

;;; Solicitar llevar el 10 al buffer (2,3) si no está ahí
(defrule JUEGO::10-paso-2-meter-10
   (declare (salience 20))
   (control-fase (fase ESPECIAL-10-METER))
   (not (objetivo-mov))
   (casilla (fila ?f) (columna ?c) (valor 10))
   (test (or (neq ?f 2) (neq ?c 3)))
   =>
   (printout t ">> Llevando el 10 al buffer (2,3)..." crlf)
   (assert (objetivo-mov (pieza 10) (destino-f 2) (destino-c 3))))

;;; Verificar que 10 está en posición y pasar a maniobra 1
(defrule JUEGO::10-paso-2-meter-10-ok
   (declare (salience 20))
   ?f <- (control-fase (fase ESPECIAL-10-METER))
   (casilla (fila 2) (columna 3) (valor 10))
   (not (objetivo-mov))
   =>
   (printout t ">> 10 en posicion. Iniciando maniobra de rotacion 1." crlf)
   (modify ?f (fase ESPECIAL-10-MANIOBRA-1)))

;;;----------------------------------------------------------------------------
;;; MANIOBRA 1: Intercambiar letras mediante rotación
;;;----------------------------------------------------------------------------
;;; Objetivo: Rotar hasta que Hueco=(4,2) y Letra=(3,1), luego 'a' e 'i'

;;; Rotar hasta alcanzar configuración: Hueco(4,2) y Letra(3,1)
(defrule JUEGO::10-paso-3-rotar-maniobra-1
   (declare (salience 50))
   (control-fase (fase ESPECIAL-10-MANIOBRA-1))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   
   ;; Identificamos la letra que está en el anillo (la que no está en el centro fijo (3,2))
   (casilla (fila 3) (columna 2) (valor ?v_fijo)) 
   (casilla (fila ?fl) (columna ?cl) (valor ?letra&A|B&~?v_fijo))

   ;; CONDICION DE PARADA NEGADA: Si NO estamos en Hueco(4,2) y Letra(3,1) -> ROTAR
   (test (not (and (= ?fh 4) (= ?ch 2) (= ?fl 3) (= ?cl 1))))
   =>
   ;; Rotación Horaria Genérica
   (if (and (= ?fh 1) (< ?ch 4)) then (assert (mover d ?fh ?ch))
    else (if (and (= ?ch 4) (< ?fh 4)) then (assert (mover b ?fh ?ch))
     else (if (and (= ?fh 4) (> ?ch 1)) then (assert (mover i ?fh ?ch))
      else (assert (mover a ?fh ?ch)))))
   (pop-focus) (focus MOVIMIENTO))

;;; Ejecutar movimiento 'a': Hueco(4,2) -> (3,2)
(defrule JUEGO::10-paso-3-ejecutar-maniobra-1a
   (declare (salience 60))
   ?f <- (control-fase (fase ESPECIAL-10-MANIOBRA-1))
   ;; Hueco en (4,2) y Letra en (3,1)
   (casilla (fila 4) (columna 2) (valor 0))
   (casilla (fila 3) (columna 2) (valor ?v_fijo))
   (casilla (fila 3) (columna 1) (valor ?letra&A|B&~?v_fijo))
   =>
   (printout t ">> Ejecutando maniobra 1: inputs 'a' " crlf)
   ;; 'a': Hueco (4,2) -> (3,2). (Mete Letra(3,1)?? No, intercambia con centro abajo)
   (assert (mover a 4 2)) 
   (pop-focus) (focus MOVIMIENTO))

;;; Ejecutar movimiento 'i': Hueco(3,2) -> (3,1) y cambiar a maniobra 2
(defrule JUEGO::10-paso-3-ejecutar-maniobra-1i
   (declare (salience 60))
   ?f <- (control-fase (fase ESPECIAL-10-MANIOBRA-1))
   ;; Hueco en (3,2)
   (casilla (fila 3) (columna 2) (valor 0))

   =>
   (printout t ">> Ejecutando maniobra 1: inputs 'i'" crlf)

   ;; 'i': Hueco esperado en (3,2) -> (3,1). (Mete la letra que estaba en 3,1 al centro)
   (assert (mover i 3 2))
   
   (modify ?f (fase ESPECIAL-10-MANIOBRA-2))
   (pop-focus) (focus MOVIMIENTO))

;;;----------------------------------------------------------------------------
;;; MANIOBRA 2: Segunda rotación para finalizar intercambio
;;;----------------------------------------------------------------------------
;;; Objetivo: Rotar hasta Hueco=(1,3) y Letra=(2,4), luego 'b' y 'd'

;;; Rotar hasta alcanzar configuración: Hueco(1,3) y Letra(2,4)
(defrule JUEGO::10-paso-4-rotar-maniobra-2
   (declare (salience 50))
   (control-fase (fase ESPECIAL-10-MANIOBRA-2))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   ;; Buscamos cualquier letra en (2,4) o rotamos hasta que llegue
   (casilla (fila ?fl) (columna ?cl) (valor ?letra&A|B)) 

   ;; CONDICION DE PARADA: Hueco(1,3) y Letra(2,4)
   (test (not (and (= ?fh 1) (= ?ch 3) (= ?fl 2) (= ?cl 4))))
   =>
   ;; Rotación Horaria
   (if (and (= ?fh 1) (< ?ch 4)) then (assert (mover d ?fh ?ch))
    else (if (and (= ?ch 4) (< ?fh 4)) then (assert (mover b ?fh ?ch))
     else (if (and (= ?fh 4) (> ?ch 1)) then (assert (mover i ?fh ?ch))
      else (assert (mover a ?fh ?ch)))))
   (pop-focus) (focus MOVIMIENTO))

;;; Ejecutar movimiento 'b': Hueco(1,3) -> (2,3)
(defrule JUEGO::10-paso-4-ejecutar-maniobra-2b
   (declare (salience 60))
   ?f <- (control-fase (fase ESPECIAL-10-MANIOBRA-2))
   (casilla (fila 1) (columna 3) (valor 0))
   (casilla (fila 2) (columna 4) (valor ?letra&A|B))
   =>
   (printout t ">> Ejecutando maniobra 2: inputs 'b' " crlf)
   (assert (mover b 1 3)) ; Hueco baja a (2,3) (Saca el 10?)

   (pop-focus) (focus MOVIMIENTO))

;;; Ejecutar movimiento 'd': Hueco(2,3) -> (2,4) y cambiar a fase final
(defrule JUEGO::10-paso-4-ejecutar-maniobra-2d
   (declare (salience 60))
   ?f <- (control-fase (fase ESPECIAL-10-MANIOBRA-2))
   (casilla (fila 2) (columna 3) (valor 0))

   =>
   (printout t ">> Ejecutando maniobra 2: inputs  'd'" crlf)

   (assert (mover d 2 3)) ; Hueco va a (2,4) (Mete la letra?)
   
   (modify ?f (fase ESPECIAL-10-FIN))
   (pop-focus) (focus MOVIMIENTO))

;;;----------------------------------------------------------------------------
;;; FASE FINAL: Rotación continua hasta completar el puzzle
;;;----------------------------------------------------------------------------

;;; Rotar continuamente en sentido horario hasta alcanzar meta
(defrule JUEGO::10-paso-final-bucle
   (declare (salience 50))
   (control-fase (fase ESPECIAL-10-FIN))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   =>
   ;; Rotación perpetua horario
   (if (and (= ?fh 1) (< ?ch 4)) then (assert (mover d ?fh ?ch))
    else (if (and (= ?ch 4) (< ?fh 4)) then (assert (mover b ?fh ?ch))
     else (if (and (= ?fh 4) (> ?ch 1)) then (assert (mover i ?fh ?ch))
      else (assert (mover a ?fh ?ch)))))
   (pop-focus) (focus MOVIMIENTO))

;;;============================================================================
;;; ACTUADORES GENÉRICOS: Ejecución de objetivos de movimiento
;;;============================================================================

;;;----------------------------------------------------------------------------
;;; ACTUADOR 1: Rotación del anillo exterior (Fase normal)
;;;----------------------------------------------------------------------------
;;; Rota el hueco en sentido horario hasta alcanzar la configuración
;;; deseada según el sentido calculado (Horario o Antihorario)

;;; Regla para movimiento objetivo (2,3)
(defrule JUEGO::actuador-rotar-pieza-23
   (declare (salience 70))
   
   ;; Contexto: Queremos meter la pieza ?p en el centro (2,3)
   (objetivo-mov (pieza ?p) (destino-f 2) (destino-c 3))
   (ordenar-n ?n)
   (control-fase (fase ?fase))
   ;; Estado actual
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))

   ;; CONDICIÓN DE PARADA (Negada):
   ;; La regla se ejecutará (rotará) MIENTRAS NO se cumpla la configuración deseada.
   (test (not (or 
      
      ;; CASO A: Sentido HORARIO
      ;; Configuración deseada: Pieza en (1,3) y Hueco en (2,4)
      (and (eq (calcular-sentido ?p ?n) "Horario")
           (= ?f 1) (= ?c 3)
           (= ?fh 2) (= ?ch 4))
           
      ;; CASO B: Sentido ANTIHORARIO (o defecto)
      ;; Configuración deseada: Pieza en (2,4) y Hueco en (1,3)
      (and (neq (calcular-sentido ?p ?n) "Horario") ;; Cubre Antihorario y otros
           (= ?f 2) (= ?c 4)
           (= ?fh 1) (= ?ch 3))
   )))
   
   ;; Seguridad: No rotar si el hueco se metió en el centro por error
   (test (or (neq ?fh 2) (neq ?ch 3)))
   (test (neq ?fase ESPECIAL-10-PREPARAR))
   =>

   ;; ACCIÓN: Rotar anillo en sentido horario (d -> b -> i -> a)
   (bind ?mov nil)
   (if (and (= ?fh 1) (< ?ch 4)) then (bind ?mov d)
    else (if (and (= ?ch 4) (< ?fh 4)) then (bind ?mov b)
     else (if (and (= ?fh 4) (> ?ch 1)) then (bind ?mov i)
      else (if (and (= ?ch 1) (> ?fh 1)) then (bind ?mov a)
       ;; Sacar hueco si está atrapado en (2,3) o (3,2)
       else (if (= ?fh 2) then (bind ?mov d) else (bind ?mov i))))))

   (if (neq ?mov nil) then
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;; Regla para movimiento objetivo (3,2) [Con if se podría reducir a 1 regla, aunque por claridad lo divido]
(defrule JUEGO::actuador-rotar-pieza-32
   (declare (salience 70))
   
   ;; Contexto: Queremos meter la pieza ?p en el centro (3,2)
   (objetivo-mov (pieza ?p) (destino-f 3) (destino-c 2))
   (ordenar-n ?n)
   (control-fase (fase ?fase))
   ;; Estado actual
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))

   ;; CONDICIÓN DE PARADA (Negada):
   ;; La regla se ejecutará (rotará) MIENTRAS NO se cumpla la configuración deseada.
   (test (not (or 
      
      ;; CASO A: Sentido HORARIO
      ;; Configuración deseada: Pieza en (4,2) y Hueco en (3,1)
      (and (eq (calcular-sentido ?p ?n) "Horario")
           (= ?f 4) (= ?c 2)
           (= ?fh 3) (= ?ch 1))
           
      ;; CASO B: Sentido ANTIHORARIO (o defecto)
      ;; Configuración deseada: Pieza en (3,1) y Hueco en (4,2)
      (and (neq (calcular-sentido ?p ?n) "Horario") ;; Cubre Antihorario
           (= ?f 3) (= ?c 1)
           (= ?fh 4) (= ?ch 2))
   )))
   
   ;; Seguridad: No rotar si el hueco se metió en el centro por error
   (test (or (neq ?fh 3) (neq ?ch 2)))
   (test (neq ?fase ESPECIAL-10-PREPARAR))
   =>

   ;; ACCIÓN: Rotar anillo en sentido horario (d -> b -> i -> a)
   (bind ?mov nil)
   (if (and (= ?fh 1) (< ?ch 4)) then (bind ?mov d)
    else (if (and (= ?ch 4) (< ?fh 4)) then (bind ?mov b)
     else (if (and (= ?fh 4) (> ?ch 1)) then (bind ?mov i)
      else (if (and (= ?ch 1) (> ?fh 1)) then (bind ?mov a)
       ;; Sacar hueco si está atrapado en (2,3) o (3,2)
       else (if (= ?fh 2) then (bind ?mov d) else (bind ?mov i))))))

   (if (neq ?mov nil) then
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;;----------------------------------------------------------------------------
;;; ACTUADOR 2: Rotación del anillo exterior (Fase especial 10)
;;;----------------------------------------------------------------------------
;;; Versión específica para la fase ESPECIAL-10-PREPARAR con lógica
;;; simplificada (siempre antihorario: Pieza(2,4) y Hueco(1,3))

(defrule JUEGO::actuador-rotar-pieza10
   (declare (salience 71))
   (control-fase (fase ESPECIAL-10-PREPARAR))
   ;; Contexto: Queremos meter la pieza ?p en el centro (2,3)
   (objetivo-mov (pieza ?p) (destino-f 2) (destino-c 3))
   

   ;; Estado actual
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))

   ;; CONDICIÓN DE PARADA (Negada):
   ;; La regla se ejecutará (rotará) MIENTRAS NO se cumpla la configuración deseada.
   (test (not 
      ;; Configuración deseada: Pieza en (2,4) y Hueco en (1,3)
      (and 
           (= ?f 2) (= ?c 4)
           (= ?fh 1) (= ?ch 3))
   ))
   
   ;; Seguridad: No rotar si el hueco se metió en el centro por error
   (test (or (neq ?fh 2) (neq ?ch 3)))

   =>

   ;; ACCIÓN: Rotar anillo en sentido horario (d -> b -> i -> a)
   (bind ?mov nil)
   (if (and (= ?fh 1) (< ?ch 4)) then (bind ?mov d)
    else (if (and (= ?ch 4) (< ?fh 4)) then (bind ?mov b)
     else (if (and (= ?fh 4) (> ?ch 1)) then (bind ?mov i)
      else (if (and (= ?ch 1) (> ?fh 1)) then (bind ?mov a)
       ;; Sacar hueco si está atrapado en (2,3) o (3,2)
       else (if (= ?fh 2) then (bind ?mov d) else (bind ?mov i))))))

   (if (neq ?mov nil) then
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;;----------------------------------------------------------------------------
;;; ACTUADOR 3: Meter hueco al centro desde el anillo (Fase normal)
;;;----------------------------------------------------------------------------
;;; Cuando la configuración está lista, mueve el hueco del anillo hacia
;;; el centro (2,3) o (3,2) según el sentido calculado

(defrule JUEGO::actuador-meter-hueco
   (declare (salience 50))
   (objetivo-mov (pieza ?p) (destino-f ?df) (destino-c ?dc))
   (control-fase (fase ?fase))
   ;; Necesitamos saber qué número estamos ordenando para calcular el sentido
   (ordenar-n ?n)
   
   ;; Estado actual
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   
   (test (neq ?fase ESPECIAL-10-PREPARAR))
   =>
   
   (bind ?mov nil)
   (bind ?sentido (calcular-sentido ?p ?n))


   ;; Destino (2,3)
   (if (and (= ?df 2) (= ?dc 3)) then
      
      ;; Si es HORARIO: Esperamos hueco en (2,4). Input 'i' (Izquierda -> entra a 2,3)
      (if (and (eq ?sentido "Horario") (= ?fh 2) (= ?ch 4)) 
          then (bind ?mov i))
          
      ;; Si es ANTIHORARIO: Esperamos hueco en (1,3). Input 'b' (Abajo -> entra a 2,3)
      (if (and (neq ?sentido "Horario") (= ?fh 1) (= ?ch 3)) 
          then (bind ?mov b))
   )


   ;; Destino (3,2)
   (if (and (= ?df 3) (= ?dc 2)) then
      
      ;; Si es HORARIO: Esperamos hueco en (3,1). Input 'd' (Derecha -> entra a 3,2)
      (if (and (eq ?sentido "Horario") (= ?fh 3) (= ?ch 1)) 
          then (bind ?mov d))
          
      ;; Si es ANTIHORARIO: Esperamos hueco en (4,2). Input 'a' (Arriba -> entra a 3,2)
      (if (and (neq ?sentido "Horario") (= ?fh 4) (= ?ch 2)) 
          then (bind ?mov a))
   )

   (if (neq ?mov nil) then
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;;----------------------------------------------------------------------------
;;; ACTUADOR 4: Meter hueco al centro desde el anillo (Fase especial 10)
;;;----------------------------------------------------------------------------
;;; Versión simplificada para fase especial: siempre ejecuta 'b'

(defrule JUEGO::actuador-meter-hueco10
   (declare (salience 51))
   (objetivo-mov (pieza ?p) (destino-f ?df) (destino-c ?dc))
   (control-fase (fase ESPECIAL-10-PREPARAR))
   
   ;; Estado actual
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   
   =>
   
   (bind ?mov b)
   (assert (mover ?mov ?fh ?ch))
   (pop-focus)
   (focus MOVIMIENTO)
)

;;;----------------------------------------------------------------------------
;;; ACTUADOR 5: Meter pieza desde el anillo al centro (Fase normal)
;;;----------------------------------------------------------------------------
;;; Cuando el hueco ya está dentro del centro, ejecuta el movimiento final
;;; para intercambiar la pieza objetivo con el hueco

(defrule JUEGO::actuador-meter-pieza
   (declare (salience 60))
   ?obj <- (objetivo-mov (pieza ?p) (destino-f ?df) (destino-c ?dc))
   
   (ordenar-n ?n)
   (control-fase (fase ?fase))
   ;; Estado actual: Pieza fuera, Hueco dentro
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   
   ;; Verificamos que el hueco está en el destino
   (test (and (= ?fh ?df) (= ?ch ?dc)))

   (test (neq ?fase ESPECIAL-10-PREPARAR))
   =>

   (bind ?mov nil)
   (bind ?sentido (calcular-sentido ?p ?n))


   ;;  Destino (2,3)
   (if (and (= ?df 2) (= ?dc 3)) then
      
      ;; Si es HORARIO: Input 'a' (Arriba). 
      ;; Hueco sube a (1,3), Pieza baja a (2,3).
      (if (eq ?sentido "Horario") 
          then (bind ?mov a))
          
      ;; Si es ANTIHORARIO: Input 'd' (Derecha).
      ;; Hueco va a la derecha (2,4), Pieza entra a la izquierda a (2,3).
      (if (neq ?sentido "Horario") 
          then (bind ?mov d))
   )

   ;;  Destino (3,2)
   (if (and (= ?df 3) (= ?dc 2)) then
      
      ;; Si es HORARIO: Input 'b' (Baja). 
      (if (eq ?sentido "Horario") 
          then (bind ?mov b))
          
      ;; Si es ANTIHORARIO: Input 'i' (Izquierda).
      (if (neq ?sentido "Horario") 
          then (bind ?mov i))
   )

   (if (neq ?mov nil) then
      (retract ?obj) ; Objetivo completado
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)

;;;----------------------------------------------------------------------------
;;; ACTUADOR 6: Meter pieza desde el anillo al centro (Fase especial 10)
;;;----------------------------------------------------------------------------
;;; Versión simplificada para fase especial: siempre ejecuta 'd'

(defrule JUEGO::actuador-meter-pieza10
   (declare (salience 61))
   ?obj <- (objetivo-mov (pieza ?p) (destino-f ?df) (destino-c ?dc))
   (control-fase (fase ESPECIAL-10-PREPARAR))
   (ordenar-n ?n)
   
   ;; Estado actual: Pieza fuera, Hueco dentro
   (casilla (fila ?f) (columna ?c) (valor ?p))
   (casilla (fila ?fh) (columna ?ch) (valor 0))
   
   ;; Verificamos que el hueco está en el destino
   (test (and (= ?fh ?df) (= ?ch ?dc)))

   =>

   (bind ?mov nil)
   (bind ?sentido (calcular-sentido ?p ?n))

   ;; Destino (2,3)
   (if (and (= ?df 2) (= ?dc 3)) then
          
      (bind ?mov d)
   )

   ;; Lógica estándar para Destino (3,2)
   (if (and (= ?df 3) (= ?dc 2)) then
       (bind ?mov b)) ;; Por defecto hueco baja

   (if (neq ?mov nil) then
      (retract ?obj) ; Objetivo completado
      (assert (mover ?mov ?fh ?ch))
      (pop-focus)
      (focus MOVIMIENTO))
)


;;; ============================================================================
;;; MODO MANUAL: Solicitud de movimientos y comprobaciones de validez
;;; ============================================================================

;;; Solicitar movimiento 
(defrule JUEGO::pedir-movimiento
   (estado (modo manual) (fase jugando))
   (not (input))
   =>
   (printout t "Movimiento (a=arriba, b=abajo, i=izq, d=der): " )
   (assert (input (read))))

;;; Procesar input y llamar a MOVIMIENTO
(defrule JUEGO::procesar-movimiento
   ?i <- (input ?dir&a|b|i|d)
   (casilla (fila ?f) (columna ?c) (valor 0)) ; Localizar hueco
   =>
   (retract ?i)
   (assert (mover ?dir ?f ?c)) ; Solicitar mover hueco desde F,C en dirección DIR
   (pop-focus)
   (focus MOVIMIENTO))

(defrule JUEGO::input-invalido
   ?i <- (input ?x&~a&~b&~i&~d)
   =>
   (retract ?i)
   (printout t "Entrada incorrecta. Use 'a', 'b', 'i' o 'd'." crlf))

;;;============================================================================
;;; MODULO MOVIMIENTO: Ejecución lógica y validación de bordes
;;;============================================================================

(defmodule MOVIMIENTO (import MAIN ?ALL) (import DIBUJAR ?ALL) (import VALIDACION ?ALL) (import JUEGO ?ALL) (export ?ALL))

;;; Reglas para calcular coordenadas destino según input:
;;; 1) Si input 'a' (Arriba): hueco pasa a destino fila - 1 (si es posible) y el valor casilla superior se asigna a la posicion de hueco anterior
;;; 2) Si input 'b' (Arriba): hueco pasa a destino fila + 1 (si es posible) y el valor casilla inferior se asigna a la posicion de hueco anterior
;;; 3) Si input 'i' (Arriba): hueco pasa a destino columna - 1 (si es posible) y el valor casilla izquierda se asigna a la posicion de hueco anterior
;;; 4) Si input 'd' (Arriba): hueco pasa a destino columna + 1 (si es posible) y el valor casilla derecha se asigna a la posicion de hueco anterior

;;; Mover Arriba (a)
(defrule MOVIMIENTO::mover-arriba
   ?m <- (mover a ?f ?c)
   (test (> ?f 1)) ; Limite tablero
   (casilla (fila ?f) (columna ?c) (valor 0))
   ?hueco <- (casilla (fila ?f) (columna ?c))
   ?destino <- (casilla (fila =(- ?f 1)) (columna ?c) (valor ?v&~X)) ; No mover si es X
   ?st <- (estado (movimientos ?n))
   =>
   (retract ?m)
   (modify ?hueco (valor ?v))
   (modify ?destino (valor 0))
   (modify ?st (movimientos (+ ?n 1)))
   (pop-focus)
   (focus DIBUJAR JUEGO)) ; Redibujar tras mover

;;; Mover Abajo (b)
(defrule MOVIMIENTO::mover-abajo
   ?m <- (mover b ?f ?c)
   (test (< ?f 4))
   (casilla (fila ?f) (columna ?c) (valor 0))
   ?hueco <- (casilla (fila ?f) (columna ?c))
   ?destino <- (casilla (fila =(+ ?f 1)) (columna ?c) (valor ?v&~X))
   ?st <- (estado (movimientos ?n))
   =>
   (retract ?m)
   (modify ?hueco (valor ?v))
   (modify ?destino (valor 0))
   (modify ?st (movimientos (+ ?n 1)))
   (pop-focus)
   (focus DIBUJAR JUEGO))

;;; Mover Izquierda (i)
(defrule MOVIMIENTO::mover-izquierda
   ?m <- (mover i ?f ?c)
   (test (> ?c 1))
   (casilla (fila ?f) (columna ?c) (valor 0))
   ?hueco <- (casilla (fila ?f) (columna ?c))
   ?destino <- (casilla (fila ?f) (columna =(- ?c 1)) (valor ?v&~X))
   ?st <- (estado (movimientos ?n))
   =>
   (retract ?m)
   (modify ?hueco (valor ?v))
   (modify ?destino (valor 0))
   (modify ?st (movimientos (+ ?n 1)))
   (pop-focus)
   (focus DIBUJAR JUEGO))

;;; Mover Derecha (d)
(defrule MOVIMIENTO::mover-derecha
   ?m <- (mover d ?f ?c)
   (test (< ?c 4))
   (casilla (fila ?f) (columna ?c) (valor 0))
   ?hueco <- (casilla (fila ?f) (columna ?c))
   ?destino <- (casilla (fila ?f) (columna =(+ ?c 1)) (valor ?v&~X))
   ?st <- (estado (movimientos ?n))
   =>
   (retract ?m)
   (modify ?hueco (valor ?v))
   (modify ?destino (valor 0))
   (modify ?st (movimientos (+ ?n 1)))
   (pop-focus)
   (focus DIBUJAR JUEGO))

;;; Captura de movimiento ilegal (fuera de rango o sobre X)
(defrule MOVIMIENTO::movimiento-ilegal
   (declare (salience -10))
   ?m <- (mover ? ? ?)
   ?st <- (estado (movimientos ?n))
   =>
   (retract ?m)
   (printout t "Movimiento invalido (borde o pieza fija X)" crlf)
   (modify ?st (movimientos (+ ?n 1)))
   (pop-focus)
   (focus JUEGO))