from tkinter import *


class PerceptronView:
    # GUI Constants
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

    def __init__(self, master):
        self.container = master
        self.frame = Frame(self.container)
