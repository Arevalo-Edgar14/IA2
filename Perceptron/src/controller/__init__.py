########  Rúbrica Canvas para espacio R^2(Plano cartesiano) ########
# 10 Pts
# TODO canvas para introducir los datos de entrenamiento en un plano
#  cartesiano (2D) acotado entre valores -5 a 5

# TODO click derecho se guardarán las coordenadas del punto en el conjunto de
#  datos de entrenamiento y la clase deseada como 1

# TODO click izquierdo se guardarán las coordenadas del punto en el conjunto
#  de datos de entrenamiento y la clase deseada será 0 (o -1 para los que
#  deseen trabajar con etiquetas bipolares)


########  Rúbrica Hiperparámetros: learning rate , épocas máximas ########
# 10 Pts / 5 si no se cumple alguno
# TODO textbox learning rate

# TODO épocas máximas

# TODO gráfica del error acumulado por época

########  Rúbrica Inicialización de pesos ########
# 10 Pts
# TODO botón que permita inicializar el vector de pesos
# TODO cuando estos se inicialicen deberán mostrar la línea recta que definen
#  esos pesos en el canvas del plano cartesiano

########  Rúbrica Algoritmo de entrenamiento y linea en cada actualización
########
# 30 Pts
# Una vez inicializado
# TODO botón de entrenamiento del perceptrón
# TODO cada que el algoritmo entre a modificar los pesos, se mostrará en
#  tiempo real la recta modificada en el canvas 2D.

########  Rúbrica Convergencia final ########
# 20 Pts
# Al finalizar el entrenamiento
# TODO desplegarán el número de épocas en el que convergió el algoritmo
# TODO matriz de confusión resultante.
# TODO introducir datos de prueba en el canvas para que los evalúen de
#  acuerdo a la línea ajustada y encontrada por el perceptrón determinar la
#  clase en la que el perceptrón ha aprendido a posicionar el punto


########  Rúbrica Entregables ########
# 20 Pts
# reporte de práctica
# TODO breve explicación de lo que es el perceptrón
# TODO el código de las funciones de ajuste de pesos
# TODO la función de transferencia del perceptrón
# TODO la función de graficado de la línea
import tkinter as tk

from perceptron.src.model import Perceptron
from perceptron.src.view import PerceptronView

class PerceptronController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Perceptron()
        self.view = PerceptronView(self.root)