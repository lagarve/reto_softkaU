# reto_softkaU
Este es un programa de preguntas aleatorias con varios niveles 


## Requisitos
Para ejecutar el programa es necesario tener instalado Python en la versión 3.9

## Ejecutar
En una ventana de comandos de Windows, ubicado en la ruta del archivo RandomDare.py, ejecute el siguiente comando:
* python RandomDare.py

## Botones 
La interfaz grafica cuenta con 4 botones a la izquierda.
*	LonGin: Permite desplegar una ventana para el logueo del jugador; Si no está logueado no puede jugar.
*	Registrarse: Permite realizar el registro de un jugador.
*	Historial: Permite ver una tabla con los jugadores y sus puntajes.
*	Jugar: Mientras no este logueado el botón permanece inactivo, cuando está actico permite regresar a la ventana del juego.


### Ventana del juego 
*  Información del jugador: Esta en la parte superior de la ventana, permite ver el nombre a la izquierda, el acumulado de puntos, el premio por responder bien y el nivel de la pregunta se encuentra a la derecha.
* Pregunta: Debajo de la información de usuario esta la pregunta, la cual es aleatoria dentro del mismo nivel y aumenta la dificultad según el nivel.
* Opciones: Debajo de la pregunta están las opciones, solo puedes elegir una.
* Botón rendirse: Si quieres salir de la partida y conservar los puntos puedes pulsar este botón, al hacerlo se despliega una ventana emergente que te preguntará si realmente deseas salir de la partida.
 * Botón responder: Cuando selecciones tu respuesta presiona sobre Responder para confirmarla.

 #### Al ganar 
Cuando seleccionas una respuesta y aciertas subirás de nivel, al llegar al nivel 5 y acertar habrá ganado y el juego terminará, pero puedes escoger en la ventana emergente la opción de volver a jugar, esto reinicia el juego, de lo contrario los botones de Responder y Retirarse se bloquearán y se establecerá tu puntaje en el historial. 
#### Al perder 
Salta una ventana emergente anunciando que perdiste, te permite escoger entre jugar una nueva o no, en cualquier caso, tus puntos estarán en cero.
#### Al rendirse
Se guardará tu puntaje actual en esta partida en el historial de jugadores. 



