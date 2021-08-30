class Perceptron:
    LEARNING_RATE = 0.001
    MAX_EPOCH = 100

    def __init__(self):
        self.x_ = []
        self.y_ = []
        self.learning_rate = self.LEARNING_RATE
        self.max_epoch = self.MAX_EPOCH

    ########  1.- Rúbrica Canvas para espacio R^2(Plano cartesiano) ########
    # 10 Pts
    # TODO receive dictionary with x,y coordinates and value 1 o 0 (1 o -1 if
    #  bipolar labels) and save it in the testing data

    ######## 2.- Rúbrica Hiperparámetros: learning rate , épocas máximas
    # ########
    # 10 Pts / 5 si no se cumple alguno
    # TODO receive new value for learning rate
    # TODO receive new value for max epoch

    ######## 3.- Rúbrica Inicialización de pesos ########
    # 10 Pts
    # TODO init xy size weights with random values

    ######## 4.- Rúbrica Algoritmo de entrenamiento y linea en cada actualización
    ########
    # 30 Pts
    # Una vez inicializado
    # TODO training function that call the training_epoch function
    # TODO training_epoch function

    ######## 5.- Rúbrica Convergencia final ########
    # 20 Pts
    # Al finalizar el entrenamiento
    # TODO have a epoch converged variable and set it on the iterations when
    #  the error = 0
    # TODO have a confusion matrix and set it at the end of the training
    #  function
    # TODO recive a dictionary with coordinates to test

