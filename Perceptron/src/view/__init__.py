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
