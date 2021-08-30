class Perceptron:
    LEARNING_RATE = 0.001
    MAX_EPOCH = 100

    def __init__(self):
        self.x_ = []
        self.y_ = []
        self.learning_rate = self.LEARNING_RATE
        self.max_epoch = self.MAX_EPOCH