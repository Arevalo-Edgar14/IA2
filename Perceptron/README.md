# Perceptron requirements

Implementarán el algoritmo del perceptrón en un lenguaje de su elección (no matlab). La implementación deberá cuboid los siguientes requerimientos

1. Al dar click derecho o izquierdo se guardarán las coordenadas del punto en el conjunto de datos de entrenamiento (o pueden manejarlo con radio-buttons) y la clase deseada será 1 ó 0 (o 1,-1 para los que deseen trabajar con etiquetas bipolares).

2. Así mismo, la interfaz permitir cambiar el valor del "learning rate" y número de épocas máximas.

3. Incluirán un botón que permita inicializar "random" el vector de pesos y cuando estos se inicialicen deberán mostrar la línea recta que definen esos pesos en el canvas del plano cartesiano.

4. Una vez inicializado, se podrá dar click en el botón de entrenamiento del perceptrón, cada que el algoritmo entre a modificar los pesos, se mostrará en tiempo real la recta modificada en el canvas 2D.

5. Al finalizar el entrenamiento, se desplegarán el número de épocas en el que convergió el algoritmo (o si no convergió) . Además se incluirá un botón "evaluar" que realice un barrido en el canvas 2D evaluando cada uno de los pares de puntos de dicho canvas y "coloréandolos" según la clase obtenida (no olviden volver a dibujar los puntos iniciales de entrenamiento después de colorear todo el canvas)

6. Subirán un reporte de práctica que tendrá las siguientes secciones:

   1. una breve (5-15 líneas) descripción del algoritmo que está implementándose en la práctica, así como del lenguaje en que lo implementaron 
   
   2. una sección de código en el que incluyan las principales funciones de entrenamiento codificadas,  
   
   3. un análisis comparativo entre el perceptrón y un método clásico (no inteligente) de clasificación, por ejemplo bases de datos, en el que incluirán ventajas y desventajas de uno vs. otro y 
   
   4. una liga a un repositorio github o almacenamiento en la nube en el que se encuentre el proyecto completo y funcional de su práctica (no olviden darme derechos para poder consultarlo!)
