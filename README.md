PAV - P3: detección de pitch
============================

Esta práctica se distribuye a través del repositorio GitHub [Práctica 3](https://github.com/albino-pav/P3).
Siga las instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para realizar un `fork` de la
misma y distribuir copias locales (*clones*) del mismo a los distintos integrantes del grupo de prácticas.

Recuerde realizar el *pull request* al repositorio original una vez completada la práctica.

Ejercicios básicos
------------------

- Complete el código de los ficheros necesarios para realizar la detección de pitch usando el programa
  `get_pitch`.

   * Complete el cálculo de la autocorrelación e inserte a continuación el código correspondiente.

A continuación mostramos el código correspondiente:

<img width="741" alt="Captura de Pantalla 2021-11-21 a les 18 05 59" src="https://user-images.githubusercontent.com/91251152/142771857-d7c8ba22-d566-46d8-9e86-b9748fda69d6.png">


   * Inserte una gŕafica donde, en un *subplot*, se vea con claridad la señal temporal de un segmento de
     unos 30 ms de un fonema sonoro y su periodo de pitch; y, en otro *subplot*, se vea con claridad la
	 autocorrelación de la señal y la posición del primer máximo secundario.

	 NOTA: es más que probable que tenga que usar Python, Octave/MATLAB u otro programa semejante para
	 hacerlo. Se valorará la utilización de la librería matplotlib de Python.
	 
	 *****Captura 2*****
	 
	 *****Captura 3*****
	 
	 Para poder observar el primer máximo secundario de forma nítida hacemos zoom en la primera parte:
	 
	  *****Captura 4*****
	  
	  *****Captura 5*****
	  

   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.
     
       *****Captura 6*****
     

   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.

   Para el caso de las tramas sonoras detectadas como sordas (UV), consideramos que la mejor opción es diferenciarlas aplicando autocorrelaciones. Con tal de poder descartar la mayoría de las tramas sonoras que detectamos como sordas (VU), creeemos que una buena opción es usando la potencia.
   
          *****Captura 7*****
	  

- Una vez completados los puntos anteriores, dispondrá de una primera versión del detector de pitch. El 
  resto del trabajo consiste, básicamente, en obtener las mejores prestaciones posibles con él.

  * Utilice el programa `wavesurfer` para analizar las condiciones apropiadas para determinar si un
    segmento es sonoro o sordo. 
	
	  - Inserte una gráfica con la detección de pitch incorporada a `wavesurfer` y, junto a ella, los 
	    principales candidatos para determinar la sonoridad de la voz: el nivel de potencia de la señal
		(r[0]), la autocorrelación normalizada de uno (r1norm = r[1] / r[0]) y el valor de la
		autocorrelación en su máximo secundario (rmaxnorm = r[lag] / r[0]).

		Puede considerar, también, la conveniencia de usar la tasa de cruces por cero.

	    Recuerde configurar los paneles de datos para que el desplazamiento de ventana sea el adecuado, que
		en esta práctica es de 15 ms.
		
	Si nos fijamos en la potencia, podemos apreciar de forma bastante clara la diferencia de potencia entre los intervalos silenciosos y sonoros.
	*****falta comentar mas cosas******
	
	Utilizamos la libreria de entrada/salida de C++ con tal de poder conseguir los valores de la autocorrelacion, ademas, empleamos la funcion cout que nos permite mostrar por consola la informacion para cada trama.
	
	*****Captura 8*****
	
	A continuacion, mediante la terminal conseguimos que la salida se escriba en un fichero .out en vez de mostrarla en la terminal. Mas adelante, para poder observar la funcion r(lag)/r(0) y r(1)/r(0), mediante el comando cut reducimos las columnas en cuestion y lo colocamos en otros dos archivos que finalmente los añadiremos en el wavesurfer
	
	*****Captura 9*****
	
	En la primera grafica observamos la potencia, en la segunda vemos r1norm, en la tercera rmaxnorm y la ultima la señal rl001.wav:
	
	*****Captura 10*****
	
	Obervamos que donde tenemos segmentos sonoros, tanto la autocorrelacion normalizadas de 1 como la normalizada en el pitch tienen un valor cercano a 1. Esto tiene todo el sentido del mundo, ya que las muestras cercanas de las tramas de voz son muy parecidas entre ellas. Para nuestro audio en particular podemos decir que para la autocorrelacion normalizada en de 1 por encima de 0,8 es una trama de voz. En cambio, para la autocorrelacion normalizada en el pitch hemos decidido que para valores mayores a 0,38 decidimos que se trata de una trama de voz.
	

      - Use el detector de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos detectores.
		
	A continuacion vemos la estimacion del pitch de wavesurfer, la estimacion de pitch de nuestra mejor version y por ultimo la señal rl006.wav:
		
	*****Captura 11*****	
  
  * Optimice los parámetros de su sistema de detección de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..
	
	
	Ahora para optimizar los parámetros de nuestro sistema de detección pescindiremos de la variables estáticas como comentamos en el laboratorio. Además, nos hemos dado cuenta que la potencia es alta cuando el locutor habla aunque tambien lo es en tramas ruidosas. Como las potencias y las autocorrelaciones no encajan de forma óptima para decidir si una trama es sonora o sorda, entonces hemos convenido en usar puertas OR y definir de forma inversa las inecuaciones. Por lo tanto nos queda de la siguiente manera:
	
	*****Captura 12*****
	
	


   * Inserte una gráfica en la que se vea con claridad el resultado de su detector de pitch junto al del
     detector de Wavesurfer. Aunque puede usarse Wavesurfer para obtener la representación, se valorará
	 el uso de alternativas de mayor calidad (particularmente Python).
   

Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  detector a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del detector. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la detección de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.

- Implemente las técnicas que considere oportunas para optimizar las prestaciones del sistema de detección
  de pitch.

  Entre las posibles mejoras, puede escoger una o más de las siguientes:

  * Técnicas de preprocesado: filtrado paso bajo, *center clipping*, etc.
  * Técnicas de postprocesado: filtro de mediana, *dynamic time warping*, etc.
  * Métodos alternativos a la autocorrelación: procesado cepstral, *average magnitude difference function*
    (AMDF), etc.
  * Optimización **demostrable** de los parámetros que gobiernan el detector, en concreto, de los que
    gobiernan la decisión sonoro/sordo.
  * Cualquier otra técnica que se le pueda ocurrir o encuentre en la literatura.

  Encontrará más información acerca de estas técnicas en las [Transparencias del Curso](https://atenea.upc.edu/pluginfile.php/2908770/mod_resource/content/3/2b_PS%20Techniques.pdf)
  y en [Spoken Language Processing](https://discovery.upc.edu/iii/encore/record/C__Rb1233593?lang=cat).
  También encontrará más información en los anexos del enunciado de esta práctica.

  Incluya, a continuación, una explicación de las técnicas incorporadas al detector. Se valorará la
  inclusión de gráficas, tablas, código o cualquier otra cosa que ayude a comprender el trabajo realizado.

  También se valorará la realización de un estudio de los parámetros involucrados. Por ejemplo, si se opta
  por implementar el filtro de mediana, se valorará el análisis de los resultados obtenidos en función de
  la longitud del filtro.
   

Evaluación *ciega* del detector
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
detector con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
