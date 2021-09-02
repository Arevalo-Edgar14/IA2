import time

import numpy as np
from pubsub import pub


class Perceptron:
    # LEARNING_RATE = 0.001
    LEARNING_RATE = 0.5
    MAX_EPOCH = 50
    BOUND = 1

    def __init__(self):
        self.reset("init")

    def reset(self, event):
        self.x_ = []
        self.y_ = []
        self.learning_rate = self.LEARNING_RATE
        self.max_epoch = self.MAX_EPOCH
        self.converged_epoch = -1
        self.confusion_matrix = []
        self.bipolar = False
        self.bounds = [-self.BOUND, self.BOUND]
        self.is_fitted = False
        self.w = []
        self.x = []
        self.y = []

    def set_xy(self, xy):
        print(f'Setting xy: {xy} on perceptron')
        self.x_.append(xy["pos"])
        self.y_.append(xy["value"])
        # send to add the point on the canvas no need to take care of bipolar
        # because on the view do not care
        pub.sendMessage("point_added", point={"x": xy["pos"][0],
                                              "y": xy["pos"][1],
                                              "value":
                                                  0 if xy["value"] == 3 else 1})

    def set_learning_rate(self, learning_rate):
        print(f'Setting learning_rate: {learning_rate} on perceptron')
        self.learning_rate = learning_rate

    def set_max_epoch(self, max_epoch):
        print(f'Setting max_epoch: {max_epoch} on perceptron')
        self.max_epoch = max_epoch

    def set_bipolar(self, bipolar):
        print(f'Setting bipolar: {bipolar} on perceptron')
        self.bipolar = bipolar

    def set_bounds(self, bounds):
        print(f'Setting bounds: {bounds} on perceptron')
        # bounds come in negative values
        self.bounds = [bounds, -bounds]

    def init(self, event):
        print(f'Initializing Perceptron Weights')
        self.x = np.array(self.x_)
        self.y = np.array(self.y_)
        # -3 is the right click value, set corresponding valued as -1 if is
        # bipolar or 0 if not
        self.y[self.y == 3] = -1 if self.bipolar else 0
        # rand values from -bound to bound of x size for this example 2 + 1 (
        # +1 because W0)
        # x.shape(points number, coords) that's why we use x.shape[1] to just
        # set coords elements number as weights, example x, y, just 2 weights
        self.w = np.random.uniform(self.bounds[0], self.bounds[1],
                                   self.x.shape[1] + 1)
        pub.sendMessage('weights_changed', weights=self.w)
        self.calculate_points_to_draw_line()

    def calculate_points_to_draw_line(self):
        x1 = np.array([self.bounds[0] - 2, self.bounds[1] + 2])
        m = -self.w[1] / self.w[2]
        b = self.w[0] / self.w[2]
        x2 = m * x1 + b
        pub.sendMessage('draw_line', data={"x": x1, "y": x2})

    def activation(self, xw):
        if xw >= 0:
            return 1
        return -1 if self.bipolar else 0

    # test method
    def Pw(self, x):
        # x dot product weights
        xw = np.dot(x, self.w)
        # return self.activation(xw)
        return 1 if xw >= 0 else 0

    def error(self, x, i):
        return self.y[i] - self.Pw(x)

    def epoch(self, current_epoch):
        print(f'new epoch {current_epoch}')
        pub.sendMessage('current_epoch_change', epoch=current_epoch)
        done = True
        errors = 0
        for i, xi in enumerate(self.x):
            # x0 = -1 because w0 = Theta need it as input is place into the
            # for to avoid x.size > y.size
            xi = np.insert(xi, 0, -1.0)

            error = self.error(xi, i)
            # errors += abs(error)
            if error != 0:
                errors += 1
                done = False
                self.w = self.w + np.multiply((self.learning_rate * error), xi)
                pub.sendMessage('weights_changed', weights=self.w)
                self.calculate_points_to_draw_line()

        pub.sendMessage('errors',
                        data={"errors": errors,
                              "epoch": current_epoch})
        return done

    def train(self, event):
        print(f'Start Training on perceptron')
        done = False
        current_epoch = 0
        while not done and current_epoch < self.max_epoch:
            current_epoch += 1
            done = self.epoch(current_epoch)
        self.converged_epoch = current_epoch - 1
        pub.sendMessage('converge',
                        converge={"converge": done,
                                  "converged_epoch": self.converged_epoch})
        self.is_fitted = True if done else False
        # converge if done == TRUE else not converge

        ######## 5.- Rúbrica Convergencia final ########
        # 20 Pts
        # Al finalizar el entrenamiento
        # TODO have a confusion matrix and set it at the end of the training
        #  function

    def test(self, xy):
        # TO SEE if need
        # np.insert(test, 0, -1.0)
        pub.sendMessage("point_added", point={"x": xy["pos"][0],
                                              "y": xy["pos"][1],
                                              "value": self.Pw(xy)})
