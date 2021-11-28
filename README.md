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
	 
	 Fonema sonoro de 30ms grabado por nosotros:
	 
	 <img width="694" alt="Captura de Pantalla 2021-11-26 a les 21 52 40" src="https://user-images.githubusercontent.com/91251152/143638758-cc4573db-b76a-4f9f-ab70-689ba3123c66.png">
	 
	 Para poder observar el primer máximo secundario de forma nítida hacemos zoom en la primera parte:

	 <img width="768" alt="Captura de Pantalla 2021-11-26 a les 21 53 06" src="https://user-images.githubusercontent.com/91251152/143639092-4945d567-0844-42b8-a781-5e612c4f6b65.png">
	 
	 Como vemos, por culpa de la baja calidad del micrófono con el que grabamos, obtenemos una señal un tanto ruidosa, por ello decidimos utilizar una señal más limpia.
	 
	  <img width="674" alt="Captura de Pantalla 2021-11-26 a les 21 57 26" src="https://user-images.githubusercontent.com/91251152/143642303-0f69f9ee-1436-4aef-a50b-5669a6f86e41.png">

	  <img width="659" alt="Captura de Pantalla 2021-11-26 a les 21 57 45" src="https://user-images.githubusercontent.com/91251152/143642535-cf7769ad-72e4-4957-aa31-48579af6bc65.png">

	  
   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.
       
     <img width="748" alt="Captura de Pantalla 2021-11-26 a les 21 58 38" src="https://user-images.githubusercontent.com/91251152/143643222-dceca88e-080b-4fda-946a-6f9bc99b2c58.png">


   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.

   Para el caso de las tramas sonoras detectadas como sordas (UV), consideramos que la mejor opción es diferenciarlas aplicando autocorrelaciones. Con tal de poder descartar la mayoría de las tramas sonoras que detectamos como sordas (VU), consideramos que una buena opción es usando la potencia.
   
  <img width="750" alt="Captura de Pantalla 2021-11-26 a les 22 00 25" src="https://user-images.githubusercontent.com/91251152/143644514-c15756a1-1d68-4233-8128-7985e3a5bf28.png">


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
	
	Utilizamos la libreria de entrada/salida de C++ con tal de poder conseguir los valores de la autocorrelacion, ademas, empleamos la funcion cout que nos permite mostrar por consola la informacion para cada trama.
	
	<img width="749" alt="Captura de Pantalla 2021-11-26 a les 22 07 52" src="https://user-images.githubusercontent.com/91251152/143649854-ade38979-5556-4d3d-9cd8-b0f5e451e90f.png">
	
	El if que tenemos asignado a 0 con tal de ver los valores por la terminal lo asignamos a 1.

	A continuacion, mediante la terminal conseguimos que la salida se escriba en un fichero .out en vez de mostrarla en la terminal. Mas adelante, para poder observar la funcion r(lag)/r(0) y r(1)/r(0), mediante el comando cut reducimos las columnas en cuestion y lo colocamos en otros dos archivos que finalmente los añadiremos en el wavesurfer.
	
	<img width="750" alt="Captura de Pantalla 2021-11-26 a les 22 11 14" src="https://user-images.githubusercontent.com/91251152/143652262-48215f84-7f3b-4e6d-9723-a950f74a8fda.png">
	
	En la primera grafica observamos la potencia, en la segunda vemos r1norm, en la tercera rmaxnorm y la ultima la señal rl006.wav:
	
	<img width="753" alt="Captura de Pantalla 2021-11-26 a les 22 12 26" src="https://user-images.githubusercontent.com/91251152/143653072-dc6b86ea-13d5-4998-aa36-11200dff2240.png">

	Obervamos que donde tenemos segmentos sonoros, tanto la autocorrelacion normalizada de 1 como la normalizada en el pitch tienen un valor cercano a 1. Esto tiene todo el sentido del mundo, ya que las muestras cercanas de las tramas de voz son muy parecidas entre ellas. Para nuestro audio en particular podemos decir que para la autocorrelacion normalizada en de 1 por encima de 0,9 es una trama de voz. En cambio, para la autocorrelacion normalizada en el pitch hemos decidido que para valores mayores a 0,5 entonces se trata de una trama de voz.
	

      - Use el detector de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos detectores.
		
	A continuacion vemos la estimacion del pitch de wavesurfer, la estimacion de pitch de nuestra mejor version y por ultimo la señal rl006.wav:
		
	En una primera versión obtuvimos un resultado del 83%, con el cual obtuvimos la siguiente información de pitch:
	
	<img width="755" alt="Captura de Pantalla 2021-11-26 a les 22 19 33" src="https://user-images.githubusercontent.com/91251152/143655713-3705594c-a1c6-4606-8d3e-d655a67e0f58.png">
	
	Como vemos, el resultado no es del todo bueno, por ello decidimos implementar una segunda version del programa para optimazarlo obteniendo los siguientes resultados:
	
	<img width="756" alt="Captura de Pantalla 2021-11-26 a les 22 21 54" src="https://user-images.githubusercontent.com/91251152/143655872-fc048462-7303-436f-b40f-339faa082668.png">
  
  * Optimice los parámetros de su sistema de detección de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..
	
	
	Con el objetivo optimizar los parámetros de nuestro sistema de detección prescindiremos de las variables estáticas como comentamos en el laboratorio. Además, nos hemos dado cuenta que la potencia es alta cuando el locutor habla aunque tambien lo es en tramas ruidosas. Como las potencias y las autocorrelaciones no encajan de forma óptima para decidir si una trama es sonora o sorda, a causa de esto hemos decido utilizar puertas OR al ser mas convenientes y definir de forma inversa las inecuaciones al ser en los casos donde surgen mas dudas. Por lo tanto nos queda de la siguiente manera:
	
	<img width="751" alt="Captura de Pantalla 2021-11-26 a les 22 28 56" src="https://user-images.githubusercontent.com/91251152/143656192-4869d7ea-cc00-4c31-9ead-327cbe00ce74.png">

	Implementando Ventana de Hamming, Center Clipping y Filtro de Mediana obtenemos on el sistema de decisión mejorado un resultado de un 90,41%. Con los parametros de decision optimizados de: Potencia = -20dBs, Autocorrelacion en 1 = 0,8 y la Autocorrelacion en el pitch = 0,38.
	
	<img width="748" alt="Captura de Pantalla 2021-11-26 a les 22 38 17" src="https://user-images.githubusercontent.com/91251152/143656623-1c8ade17-208f-4843-87b9-6e8cdb984dbb.png">

   * Inserte una gráfica en la que se vea con claridad el resultado de su detector de pitch junto al del
     detector de Wavesurfer. Aunque puede usarse Wavesurfer para obtener la representación, se valorará
	 el uso de alternativas de mayor calidad (particularmente Python).
	 
	 A continuación se puede apreciar una gráfica con la implementación del filtro de mediana.
	 
	 <img width="604" alt="Captura de Pantalla 2021-11-26 a les 22 41 13" src="https://user-images.githubusercontent.com/91251152/143656765-04bcf3f0-89d8-4653-808c-62022614e87e.png">

	 
	 Como vemos obtuvimos una primera versión con resultados no del todo buenos para la deteccion del pitch, por ello decidimos mejorarlo obteniendo los siguientes resultados:
	 
	 
        <img width="555" alt="Captura de Pantalla 2021-11-26 a les 22 42 34" src="https://user-images.githubusercontent.com/91251152/143656824-3c929923-6c87-4a9b-acf3-15096ef745c8.png">
	
	Apreciamos en esta ultima version la mejora de la deteccion del pitch, en la primera parte del reconocimiento de pitch no se aprecia mucho la mejora, pero en la segunda mitad obtenemos una mejora muy importante detectando de forma muy acurada la señal del pitch.


Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  detector a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del detector. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la detección de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.
    
    Ahora utilizamos la libreria  docopt para pasar por la terminal los thresholds para los diferentes parámetros que definen si una señal es sorda o sonora. Lo primero que hacemos es cambiar eL USAGE en get_pitch:
    
    <img width="753" alt="Captura de Pantalla 2021-11-26 a les 22 48 53" src="https://user-images.githubusercontent.com/91251152/143657174-bba9243b-e8d9-4cf8-a2cc-8736b4948929.png">

    A continuación recuperamos los valores especificados en la terminal como hicimos con el threshold 1 en el laboratorio:
    
    <img width="692" alt="Captura de Pantalla 2021-11-26 a les 22 51 30" src="https://user-images.githubusercontent.com/91251152/143657328-a9d9e24f-5021-4373-810f-e3c0a1c0820e.png">
 
    Para finalizar, cambiamos el pitch_analyzer.h para poder utilizar los nuevos thresholds y modificamos los valores que tenemos por defecto del mensaje de ayuda por los mas optimos que hemos encontrado:
    
    <img width="749" alt="Captura de Pantalla 2021-11-26 a les 22 59 59" src="https://user-images.githubusercontent.com/91251152/143657742-c180ce08-97c5-4d28-93d9-b44844f1f028.png">

    Hacemos comparaciones con f0ref y vemos que no cambia el resultado respecto a hacerlo por consola o en el propio codigo.
    

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
  
  
  **Implementación del Center Clipping**
  
  El principal objetivo de aplicar esta técnica de preprocesado es la de conseguir mejores resultados frente al ruido. Con este objetivo, lo que hacemos es poner 0 los instantes de tiempo en que la amplitud del audio es baja, y elevar la intensidad de los armónicos de orden alto. Hemos implementado el clipping con offset primero y después sin offset:
  
  <img width="749" alt="Captura de Pantalla 2021-11-26 a les 23 07 31" src="https://user-images.githubusercontent.com/91251152/143658090-76691330-39da-4930-b3f5-a8f9a86cdb3e.png">

  Hemos detectado que obtenemos mejores resultados implementando el clipping sin offset.
  
  **Implementación de la ventana de Hamming**
  
  A partir de la fórmula de la ventana de Hamming hemos hecho el siguiente código:

  <img width="744" alt="Captura de Pantalla 2021-11-26 a les 23 09 53" src="https://user-images.githubusercontent.com/91251152/143658174-e07671e1-2789-4efb-ae16-136d3431718f.png">

   **Implementación del filtro de Mediana**
   
   Esta tecnica de postprocesado se trata de coger un entorno de cada una de las muestras y mirar cual es el valor mediano. Es decir, cogemos la muestra anterior, la actual y la siguiente y de estas 3 muestras nos quedamos con el valor intermedio (filtro de mediana de longitud 3). Lo hacemos asi porque sabemos que la evolucion del pitch es una evolucion suave, con este filtrado de mediana eliminamos los saltos bruscos. A continuacion vemos el codigo que hemos implementado:
   
   <img width="747" alt="Captura de Pantalla 2021-11-26 a les 23 11 00" src="https://user-images.githubusercontent.com/91251152/143658217-a59d7766-f8e5-4ef6-b794-c9f928ff89a4.png">

   
   Mostramos la grafica final implementando el filtro:
  
    <img width="568" alt="Captura de Pantalla 2021-11-26 a les 23 13 19" src="https://user-images.githubusercontent.com/91251152/143658314-8049ccf5-1e76-4a55-810a-9e5317a442a8.png">

    
   

Evaluación *ciega* del detector
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
detector con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
