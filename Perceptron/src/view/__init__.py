from tkinter import *
import os


class PerceptronView:
    # GUI Constants
    GUI_TITLE = 'Implementación perceptrón'

    CANVAS_PADDING_Y = 20

    CANVAS_BG_COLOR = "white"

    CANVAS_HEIGHT = 200

    CANVAS_WIDTH = 300

    LEARNING_RATE_MAX = 1.0
    LEARNING_RATE_MIN = 0.0
    LEARNING_RATE = 0.001
    LEARNING_RATE_INCREMENT = LEARNING_RATE

    MAX_EPOCH_MAX = 99999999
    MAX_EPOCH_MIN = 0
    MAX_EPOCH = 50
    MAX_EPOCH_INCREMENT = 100

    DEFAULT_LANGUAGE = "en"

    def __init__(self, master: Tk):
        # Hack to set DISPLAY env variable if not set, this is need for tk,
        # if can't create or connect the computer don't have a display
        if os.environ.get('DISPLAY', '') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        master.title = self.GUI_TITLE

        self.WINDOW_WIDTH = master.winfo_screenwidth() or 1440
        self.WINDOW_HEIGHT = master.winfo_screenheight() or 1024

        master.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        master.resizable(1, 1)

        self.container = master
        self.frame = Frame(self.container)

        ######## 1.- Rúbrica Canvas para espacio R^2(Plano cartesiano) ########
        # 10 Pts
        # TODO create a canvas to introduce train data with default bounds
        #  -5, 5
        # TODO receive a dictionary with a boolean and the coordinates to
        #  draw a circle of color blue if true or red if false

        ######## 2.- Rúbrica Hiperparámetros: learning rate , épocas máximas
        # ########
        # 10 Pts / 5 si no se cumple alguno
        # TODO create learning rate spinbox
        # TODO create max epoch spinbox
        # TODO create an empty error graph bar
        # TODO receive a new accumulative error from a new epoch and draw it
        #  on a new bar

        ######## 3.- Rúbrica Inicialización de pesos ########
        # 10 Pts
        # TODO create a init weights button
        # TODO create a function to receive a dictionary with the data for
        #  drawing a line (perceptron description) in the canvas

        ######## 4.- Rúbrica Algoritmo de entrenamiento y linea en cada actualización
        ########
        # 30 Pts
        # Una vez inicializado
        # TODO create a perceptron training button
        # TODO reuse the same function for draw a line

        ######## 5.- Rúbrica Convergencia final ########
        # 20 Pts
        # Al finalizar el entrenamiento
        # TODO create converge label with the converges end value

        # TODO create a confusion matrix with the result values.

        # TODO receive the converge epoch number and display in the converge
        #  label

        # TODO receive an array with the confusion matrix values to display

        # TODO reuse the same function for draw a circle
