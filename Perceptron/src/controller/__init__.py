######## 6.- Rúbrica Entregables ########
# 20 Pts
# reporte de práctica
# TODO breve explicación de lo que es el perceptrón
# TODO el código de las funciones de ajuste de pesos
# TODO la función de transferencia del perceptrón
# TODO la función de graficado de la línea
from pubsub import pub

from perceptron.src.model import Perceptron
from perceptron.src.view import PerceptronView


class PerceptronController:
    def __init__(self):
        self.model = Perceptron()
        self.view = PerceptronView()
        self.create_publishers()
        self.create_subscribers()

    def create_publishers(self):
        # bipolar
        self.view.bipolar_checkbutton.configure(command=self._on_change_bipolar)

        # bounds
        self.view.bounds_scale.configure(command=self._on_change_bounds)

        # max epoch
        self.view.max_epoch_scale.configure(command=self._on_change_max_epoch)

        # learning rate
        self.view.learning_rate_scale.configure(
            command=self._on_change_learning_rate)

        # canvas clicks
        self.view.canvas.mpl_connect('button_press_event',
                                     self._on_press_canvas)
        self.cid = self.view.canvas.mpl_connect('button_press_event',
                                                self._on_first_press_canvas)

        # init button
        self.view.initialize_button.configure(command=self._initialize)

        # perceptron button
        self.view.perceptron_button.configure(command=self._train)

    def create_subscribers(self):
        pub.subscribe(self.model.set_bipolar, 'bipolar_changed')
        pub.subscribe(self.view.bipolar_changed, 'bipolar_changed')

        pub.subscribe(self.view.bounds_changed, 'bounds_changed')
        pub.subscribe(self.model.set_bounds, 'bounds_changed')

        pub.subscribe(self.model.set_max_epoch, 'max_epoch_changed')
        pub.subscribe(self.view.max_epoch_changed, 'max_epoch_changed')

        pub.subscribe(self.model.set_learning_rate, 'learning_rate_changed')
        pub.subscribe(self.view.learning_rate_changed, 'learning_rate_changed')

        pub.subscribe(self.model.set_xy, 'canvas_pressed')
        pub.subscribe(self.view.draw_point, 'point_added')

        pub.subscribe(self.view.draw_bar, 'accumulative_error')

        pub.subscribe(self.view.draw_line, 'draw_line')

        pub.subscribe(self.model.init, 'initialize_perceptron')
        pub.subscribe(self.view.perceptron_initialized, 'initialize_perceptron')

        pub.subscribe(self.model.train, 'train_perceptron')


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
        #  class type

    def _on_change_bipolar(self, _event=None):
        print(f'Checkbutton bipolar with: {self.view.bipolar.get()} value')
        pub.sendMessage('bipolar_changed', bipolar=self.view.bipolar.get())

    def _on_change_bounds(self, _event=None):
        print(f'Scale bounds with: {self.view.bounds.get()} value')
        pub.sendMessage('bounds_changed', bounds=self.view.bounds.get())

    def _on_change_max_epoch(self, _event=None):
        print(f'Scale max_epoch with: {self.view.max_epoch.get()} value')
        pub.sendMessage('max_epoch_changed',
                        max_epoch=self.view.max_epoch.get())

    def _on_change_learning_rate(self, _event=None):
        print(f'Scale learning_rate with: '
              f'{"{:.5f}".format(float(self.view.learning_rate.get()))} value')
        pub.sendMessage('learning_rate_changed',
                        learning_rate="{:.5f}".format(float(
                            self.view.learning_rate.get())))

    @staticmethod
    def _on_press_canvas(event):
        # left click event.button == 1, right click event.button == 3
        print(f'Canvas on pressed with: {event}')
        # event button is a enum so is saved like Button Object need explicit
        # cast to int
        pub.sendMessage('canvas_pressed',
                        xy={"pos": [event.xdata, event.ydata],
                            "value": int(event.button)})

    def _on_first_press_canvas(self, event):
        print(f'Canvas on pressed for fist time')
        self.view.canvas.mpl_disconnect(self.cid)
        self.view.data_registered()

    @staticmethod
    def _initialize(_event=None):
        print(f'Initialize perceptron')
        pub.sendMessage('initialize_perceptron', event='Initialize')

    @staticmethod
    def _train(_event=None):
        print(f'Start Training perceptron')
        pub.sendMessage('train_perceptron', event='Start Training')

    def run(self):
        self.view.run()
