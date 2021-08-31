######## 6.- Rúbrica Entregables ########
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
        self.model = Perceptron()
        self.view = PerceptronView()

        # For publisher/Subscriber Pattern
        # send a message pub.sendMessage(message, data)
        # subscribe to a message pub.subscribe(function to process the message,
        # message)

        # Events Info
        # left click = 1, right click = 2

        # bind a event to a method
        # view element.bind('event', function)
        # canvas.callbacks.connect('event', function)

        ########  1.- Rúbrica Canvas para espacio R^2(Plano cartesiano) ########
        # 10 Pts
        # TODO bind the canvas2D to send a message to send a dictionary with
        #  coordinates and 1 if right click or 0 if left click (1 o -1 if
        #  bipolar labels) if not fitted Front-to-back

        ######## 2.- Rúbrica Hiperparámetros: learning rate , épocas máximas
        # ########
        # 10 Pts / 5 si no se cumple alguno
        # TODO bind <Return>, <Unmap>, <FocusOut> on spinbox to send a
        #  message with the new learning rate Front-to-back

        # TODO bind <Return>, <Unmap>, <FocusOut> on spinbox to send a
        #  message with the new max epoch Front-to-back

        # TODO bind calculate error per epoch to send a message with the new
        #  accumulative error Back-to-Front

        ######## 3.- Rúbrica Inicialización de pesos ########
        # 10 Pts
        # TODO bind the init button to send a message to init weights
        #  Front-to-Back

        # TODO bind init weights to send a message to draw a line with the
        #  values to draw Back-to-Front

        ######## 4.- Rúbrica Algoritmo de entrenamiento y linea en cada actualización
        ########
        # 30 Pts
        # Una vez inicializado
        # TODO bind train method for every epoch send a message to draw a
        #  line with the values to draw Back-to-Front

        ######## 5.- Rúbrica Convergencia final ########
        # 20 Pts
        # Al finalizar el entrenamiento
        # TODO bind the end of the train function to send a message to set
        #  the epoch converge value to display Back-to-Front
        # TODO bind the end of the train function to send a message to set
        #  the confusion matrix Back-to-Front
        # TODO bind the canvas2D to send a message to send the coordinates if
        #  fitted Front-to-Back
        # TODO bind the test function to send a boolean with the returned
        #  class type and test the following code ref
        #  https://stackoverflow.com/questions/58319693/how-to-disconnect-matplotlibs-event-handler
        #  Back-to-Front
        # def de_activate(self):
        #     print('checkbutton: ' + str(self.var1.get()))
        #     if self.var1.get() == 1:
        #         self.cidpress = self.fig.canvas.mpl_connect(
        #             'button_press_event', self.on_press)
        #         print('on_press connected (cid=' + str(self.cidpress) + ')')
        #     else:
        #         self.fig.canvas.mpl_disconnect(self.cidpress)
        #         self.cidpress = 0  # <<<<<<<<<<<<<<<<<<<<
        #         print('on_press disconnected (cid=' + str(self.cidpress) + ')')


    def run(self):
        self.view.run()
