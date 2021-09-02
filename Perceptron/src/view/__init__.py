import tkinter as tk
import tkinter.ttk as ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

from perceptron.src.view.plot import Plot


class PerceptronView:
    # GUI Constants
    GUI_TITLE = 'Implementación perceptrón'

    FONT_TITLE = '{Times New Roman} 24 {}'

    BACKGROUND = '#e9e9e9'

    PERCEPTRON_BUTTON_PATH = '../../assets/perceptronButton100x30.png'
    INIT_BUTTON_IMAGE_PATH = '../../assets/initializeButton90x30.png'

    CANVAS_PADDING = 50
    BIG_PADDING = 20
    PADDING = 10
    SMALL_PADDING = 5

    IMAGE_BUTTON_STYLE = 'Toolbutton'
    BUTTON_DISABLED = 'disabled'
    BUTTON_ENABLED = 'normal'

    SCALE_LENGTH = 180
    SCALE_ORIENTATION = 'horizontal'

    BIPOLAR = False

    BOUNDS_MIN = -5
    BOUNDS_MAX = -1
    BOUNDS = -5

    LEARNING_RATE_MIN = 0.001
    LEARNING_RATE_MAX = 0.1
    LEARNING_RATE = LEARNING_RATE_MAX

    MAX_EPOCH_MAX = 500
    MAX_EPOCH_MIN = 50
    MAX_EPOCH = 100

    DEFAULT_LANGUAGE = "en"

    def __init__(self, master=None):
        # Hack to set DISPLAY env variable if not set in linux, this is need for
        # tk, if can't create or connect the computer don't have a display
        if os.environ.get('DISPLAY', '') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        # get absolute path for images import
        absolute_path = os.path.dirname(os.path.realpath(__file__))

        # build ui
        # top level container (new window)
        self.toplevel = tk.Tk(screenName=self.GUI_TITLE) if master is None \
            else tk.Toplevel(master, title=self.GUI_TITLE)

        # hyper params and canvas 2D frame
        self.top_frame = ttk.Frame(self.toplevel)

        # hyper params frame
        self.hyper_parameters_frame = ttk.Frame(self.top_frame)
        # TODO add to _i18n internationalization
        self.hyper_parameters_label = ttk.Label(self.hyper_parameters_frame,
                                                font=self.FONT_TITLE,
                                                text='Hyper Parameters')
        self.hyper_parameters_label.pack(padx=self.BIG_PADDING,
                                         pady=self.BIG_PADDING, side='top')

        # bipolar element
        self.bipolar_frame = ttk.Frame(self.hyper_parameters_frame)
        self.bipolar = tk.BooleanVar(value=self.BIPOLAR)
        # TODO add to _i18n internationalization
        self.bipolar_checkbutton = ttk.Checkbutton(self.bipolar_frame,
                                                   text='Bipolar',
                                                   variable=self.bipolar)
        self.bipolar_checkbutton.pack(expand='true', fill='x', side='left')
        self.bipolar_frame.pack(expand='true', fill='x',
                                pady=self.SMALL_PADDING, side='top')
        # bounds elements
        self.bounds_frame = ttk.Frame(self.hyper_parameters_frame)
        # TODO add to _i18n internationalization
        self.bounds_label = ttk.Label(self.bounds_frame, text='Bounds')
        self.bounds_label.pack(side='left')
        self.bound_max_label = ttk.Label(self.bounds_frame,
                                         text=f'{self.BOUNDS_MAX}   ')
        self.bound_max_label.pack(side='right')
        self.bounds = tk.IntVar(value=self.BOUNDS)
        self.bounds_scale = ttk.Scale(self.bounds_frame,
                                      from_=self.BOUNDS_MIN,
                                      length=self.SCALE_LENGTH,
                                      orient=self.SCALE_ORIENTATION,
                                      to=self.BOUNDS_MAX,
                                      value=self.BOUNDS, variable=self.bounds)
        self.bounds_scale.pack(side='right')
        self.bound_min_label = ttk.Label(self.bounds_frame,
                                         text=f'{self.BOUNDS_MIN}')
        self.bound_min_label.pack(side='right')
        self.bounds_frame.pack(expand='true', fill='x',
                               pady=self.SMALL_PADDING, side='top')

        # learning rate elementes
        self.learning_rate_frame = ttk.Frame(self.hyper_parameters_frame)
        # TODO add to _i18n internationalization
        self.learning_rate_label = ttk.Label(self.learning_rate_frame,
                                             text='Learning Rate')
        self.learning_rate_label.pack(side='left')
        self.learning_rate_max_label = ttk.Label(self.learning_rate_frame,
                                                 text=self.LEARNING_RATE_MAX)
        self.learning_rate_max_label.pack(side='right')
        self.learning_rate = tk.DoubleVar(value=self.LEARNING_RATE)
        self.learning_rate_scale = ttk.Scale(self.learning_rate_frame,
                                             from_=self.LEARNING_RATE_MIN,
                                             length=self.SCALE_LENGTH,
                                             orient=self.SCALE_ORIENTATION,
                                             to=self.LEARNING_RATE_MAX,
                                             value=self.LEARNING_RATE,
                                             variable=self.learning_rate)
        self.learning_rate_scale.pack(side='right')

        self.learning_rate_min_label = ttk.Label(self.learning_rate_frame,
                                                 text=self.LEARNING_RATE_MIN)
        self.learning_rate_min_label.pack(side='right')
        self.learning_rate_frame.pack(expand='true', fill='x',
                                      pady=self.SMALL_PADDING,
                                      side='top')

        # max epoch elements
        self.max_epoch_frame = ttk.Frame(self.hyper_parameters_frame)
        # TODO add to _i18n internationalization
        self.max_epoch_label = ttk.Label(self.max_epoch_frame,
                                         text='Max Epoch')
        self.max_epoch_label.pack(side='left')

        self.max_epoch_max_label = ttk.Label(self.max_epoch_frame)
        self.max_epoch_max_label.configure(text=f'{self.MAX_EPOCH_MAX} ')
        self.max_epoch_max_label.pack(side='right')
        self.max_epoch = tk.IntVar(value=self.MAX_EPOCH)
        self.max_epoch_scale = ttk.Scale(self.max_epoch_frame,
                                         from_=self.MAX_EPOCH_MIN,
                                         length=self.SCALE_LENGTH,
                                         orient=self.SCALE_ORIENTATION,
                                         to=self.MAX_EPOCH_MAX,
                                         value=self.MAX_EPOCH,
                                         variable=self.max_epoch)
        self.max_epoch_scale.pack(side='right')

        self.max_epoch_min_label = ttk.Label(self.max_epoch_frame,
                                             text=self.MAX_EPOCH_MIN)
        self.max_epoch_min_label.pack(side='right')
        self.max_epoch_frame.pack(expand='true', fill='x',
                                  pady=self.SMALL_PADDING, side='top')
        self.buttons_frame = ttk.Frame(self.hyper_parameters_frame)

        self.initializeButtonImage = tk.PhotoImage(
            file=os.path.join(absolute_path, self.INIT_BUTTON_IMAGE_PATH))
        # TODO add to _i18n internationalization
        self.initialize_button = ttk.Button(self.buttons_frame,
                                            image=self.initializeButtonImage,
                                            style=self.IMAGE_BUTTON_STYLE,
                                            state=self.BUTTON_DISABLED,
                                            text='Initialize')
        self.initialize_button.pack(side='left')
        self.perceptronButtonImage = tk.PhotoImage(
            file=os.path.join(absolute_path, self.PERCEPTRON_BUTTON_PATH))
        # TODO add to _i18n internationalization
        self.perceptron_button = ttk.Button(self.buttons_frame,
                                            image=self.perceptronButtonImage,
                                            style=self.IMAGE_BUTTON_STYLE,
                                            state=self.BUTTON_DISABLED,
                                            text='Perceptron')
        self.perceptron_button.pack(side='right')
        self.buttons_frame.pack(expand='true', fill='x',
                                pady=self.SMALL_PADDING, side='top')

        ###
        self.parameters_labelframe = ttk.Labelframe(
            self.hyper_parameters_frame, text='Selected Parameters')

        self.bipolar_selected = tk.StringVar(
            value=f'Bipolar: {self.bipolar.get()}')
        self.bipolar_selected_label = ttk.Label(
            self.parameters_labelframe,
            text=f'Bipolar: {self.bipolar.get()}',
            textvariable=self.bipolar_selected)
        self.bipolar_selected_label.pack(side='top')

        self.bounds_selected = tk.StringVar(
            value=f'Bounds: {self.bounds.get()} , {-1 * self.bounds.get()}')
        self.bounds_selected_label = ttk.Label(
            self.parameters_labelframe,
            text=f'Bounds: {self.bounds.get()} , {-1 * self.bounds.get()}',
            textvariable=self.bounds_selected)
        self.bounds_selected_label.pack(side='top')

        self.learning_rate_select = tk.StringVar(
            value=f'Learning Rate: {self.learning_rate.get()}')
        self.learning_rate_select_label = ttk.Label(
            self.parameters_labelframe,
            text=f'Learning Rate: {self.learning_rate.get()}',
            textvariable=self.learning_rate_select)
        self.learning_rate_select_label.pack(side='top')

        self.max_epoch_select = tk.StringVar(
            value=f'Max Epoch: {self.max_epoch.get()}')
        self.max_epoch_select_label = ttk.Label(
            self.parameters_labelframe,
            text=f'Max Epoch: {self.max_epoch.get()}',
            textvariable=self.max_epoch_select)
        self.max_epoch_select_label.pack(side='top')

        self.parameters_labelframe.pack(side='top')

        self.hyper_parameters_frame.pack(anchor='nw', expand='false',
                                         side='left')

        # main plot canvas2D frame
        self.plot_frame = ttk.Frame(self.top_frame)
        # Create a figure
        self.fig = Figure(facecolor=self.BACKGROUND)

        # create a subplot to plot
        self.ax = self.fig.add_subplot(111,
                                       xlim=[-1 * self.bounds.get(),
                                             self.bounds.get()],
                                       ylim=[-1 * self.bounds.get(),
                                             self.bounds.get()],
                                       facecolor=f'tab:gray')

        # Create a figure canvas to can connect the widget and connect it to
        # the press event
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)

        self.canvas.get_tk_widget().pack(expand='true', fill='both',
                                         padx=self.CANVAS_PADDING, side='top')

        self.plot_frame.pack(anchor='e', expand='true', fill='both',
                             pady=self.BIG_PADDING, side='right')
        self.top_frame.pack(anchor='center', expand='true', fill='both',
                            padx=self.BIG_PADDING, pady=self.BIG_PADDING,
                            side='top')

        # bottom frame with the confusion matrix and the graph bar error
        self.bottom_frame = ttk.Frame(self.toplevel)
        # confusion matrix frame
        self.confusion_matrix_frame = ttk.Frame(self.bottom_frame)
        # TODO add to _i18n internationalization
        self.confusion_matrix_label = ttk.Label(self.confusion_matrix_frame,
                                                font=self.FONT_TITLE,
                                                text='Confusion Matrix')
        self.confusion_matrix_label.pack(padx=self.BIG_PADDING,
                                         pady=self.BIG_PADDING, side='top')
        # TODO see how to plot confusion matrix
        # Create a figure
        self.confusion_matrix_fig = Figure(facecolor=self.BACKGROUND)

        # create a subplot to plot
        self.confusion_matrix_ax = self.confusion_matrix_fig \
            .add_subplot(111,
                         xlim=[-1 * self.bounds.get(),
                               self.bounds.get()],
                         ylim=[-1 * self.bounds.get(),
                               self.bounds.get()],
                         facecolor=f'tab:gray')

        # Create a figure canvas to can connect the widget and connect it to
        # the press event
        self.confusion_matrix_canvas = FigureCanvasTkAgg(
            self.confusion_matrix_fig, master=self.confusion_matrix_frame)

        self.confusion_matrix_canvas.get_tk_widget().pack(side='top')

        self.confusion_matrix_frame.pack(expand='true', fill='x',
                                         padx=self.BIG_PADDING,
                                         pady=self.BIG_PADDING, side='left')

        # Graph Bar Error frame
        self.graph_error_frame = ttk.Frame(self.bottom_frame)
        # TODO add to _i18n internationalization
        self.graph_error_label = ttk.Label(self.graph_error_frame,
                                           font=self.FONT_TITLE,
                                           text='Graph Error')
        self.graph_error_label.pack(padx=self.BIG_PADDING,
                                    pady=self.BIG_PADDING, side='top')
        # TODO check how to set correct bounds
        # Create a figure
        self.graph_error_fig = Figure(facecolor=self.BACKGROUND)

        # create a subplot to plot
        self.graph_error_ax = self.graph_error_fig.add_axes(
            [0, 0, 1, 1], facecolor=f'tab:gray')
        # .add_subplot(111,
        #              xlim=[0, 1],
        #              ylim=[0, 1],
        #              facecolor=f'tab:gray')

        # Create a figure canvas to can connect the widget and connect it to
        # the press event
        self.graph_error_canvas = FigureCanvasTkAgg(
            self.graph_error_fig, master=self.graph_error_frame)
        self.graph_error_canvas.get_tk_widget().pack(side='top')
        ################
        self.graph_error_frame.pack(expand='true', fill='x',
                                    padx=self.BIG_PADDING,
                                    pady=self.BIG_PADDING, side='right')
        self.bottom_frame.pack(fill='x', padx=self.BIG_PADDING,
                               pady=self.BIG_PADDING, side='top')

        # get screen width and height if not, set it to 1440x1080 resolution
        screen_width = self.toplevel.winfo_screenwidth()
        screen_height = self.toplevel.winfo_screenheight()
        self.WINDOW_WIDTH = screen_width if screen_width is not None else 1440
        self.WINDOW_HEIGHT = screen_height if screen_height is not None \
            else 900

        # set screen size
        self.toplevel.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        # # set screen title
        # self.toplevel.title = self.GUI_TITLE

        # Main widget
        self.main_window = self.toplevel

    def bipolar_changed(self, bipolar):
        print(f'Bipolar change on view to {self.bipolar.get()}')
        self.bipolar_selected.set(f'Bipolar: {self.bipolar.get()}')

    def bounds_changed(self, bounds):
        print(f'Bounds change on view to {self.bounds.get()}')
        self.bounds_selected.set(
            f'Bounds: {self.bounds.get()} , {-1 * self.bounds.get()}')
        self.ax.set_xlim([self.bounds.get(), -1 * self.bounds.get()])
        self.ax.set_ylim([self.bounds.get(), -1 * self.bounds.get()])
        self.canvas.draw()

    def learning_rate_changed(self, learning_rate):
        print(f'Learning Rate change on view to '
              f'{"{:.5f}".format(float(self.learning_rate.get()))}')
        self.learning_rate_select.set(
            f'Learning Rate: '
            f'{"{:.5f}".format(float(self.learning_rate.get()))}')

    def max_epoch_changed(self, max_epoch):
        print(f'Max Epoch change on view to {self.max_epoch.get()}')
        self.max_epoch_select.set(f'Max Epoch: {self.max_epoch.get()}')

    def data_registered(self):
        print(f'Any data test is registered')
        self.initialize_button.configure(state=self.BUTTON_ENABLED)

    def perceptron_initialized(self, event):
        print(f'Perceptron already initialized activating Perceptron Button')
        self.perceptron_button.configure(state=self.BUTTON_ENABLED)

    def draw_point(self, point):
        print(f'Drawing point')
        text = ['x', 'o']
        class_color = ['r', 'b']
        self.ax.plot(point["x"],
                     point["y"],
                     text[point["value"]] + str(class_color[point["value"]]))
        self.canvas.draw()

    def draw_line(self, data):
        print(f'Drawing line')
        self.ax.plot(data["x"], data["y"])
        self.canvas.draw()

    def draw_bar(self, data):
        print(f'Drawing bar')
        self.graph_error_ax.bar(f'{data["epoch"]}: '
                                f'{data["accumulative_error"]}',
                                data["accumulative_error"])
        self.graph_error_canvas.draw()

    # TODO update epoch

    def run(self):
        self.main_window.deiconify()
        print('---- Starting main event loop ----')
        self.main_window.mainloop()
        print('---- Exited main event loop ----')

        ######## 5.- Rúbrica Convergencia final ########
        # 20 Pts
        # Al finalizar el entrenamiento
        # TODO create converge label with the converges end value

        # TODO create a confusion matrix with the result values.

        # TODO receive the converge epoch number and display in the converge
        #  label

        # TODO receive an array with the confusion matrix values to display

        # TODO reuse the same function for draw a circle
