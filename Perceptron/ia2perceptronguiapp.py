import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "IA2_perceptron_gui.ui")

class Ia2PerceptronGuiApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel = tk.Toplevel(master, container='false')
        self.top_frame = ttk.Frame(self.toplevel)
        self.hyper_parameters_frame = ttk.Frame(self.top_frame)
        self.hyper_parameters_label = ttk.Label(self.hyper_parameters_frame)
        self.hyper_parameters_label.configure(font='{Times New Roman} 24 {}', text='Hyper Parameters')
        self.hyper_parameters_label.pack(padx='20', pady='20', side='top')
        self.frame7 = ttk.Frame(self.hyper_parameters_frame)
        self.bipolar_checkbutton = ttk.Checkbutton(self.frame7)
        self.bipolar = tk.BooleanVar(value='')
        self.bipolar_checkbutton.configure(text='Bipolar', variable=self.bipolar)
        self.bipolar_checkbutton.pack(expand='true', fill='x', side='left')
        self.bipolar_checkbutton.configure(command=self._onchange)
        self.frame7.pack(expand='true', fill='x', pady='5', side='top')
        self.bounds_frame = ttk.Frame(self.hyper_parameters_frame)
        self.bounds_label = ttk.Label(self.bounds_frame)
        self.bounds_label.configure(text='Bounds')
        self.bounds_label.pack(side='left')
        self.bound_max_label = ttk.Label(self.bounds_frame)
        self.bound_max_label.configure(text='-3   ')
        self.bound_max_label.pack(side='right')
        self.bounds_scale = ttk.Scale(self.bounds_frame)
        self.bounds = tk.DoubleVar(value=-5)
        self.bounds_scale.configure(from_='-20', length='180', orient='horizontal', to='-3')
        self.bounds_scale.configure(value='-5', variable=self.bounds)
        self.bounds_scale.pack(side='right')
        self.bounds_scale.bind('<FocusOut>', self._on_change, add='')
        self.bounds_scale.bind('<Return>', self._on_change, add='')
        self.bounds_scale.bind('<Unmap>', self._on_change, add='')
        self.bound_min_label = ttk.Label(self.bounds_frame)
        self.bound_min_label.configure(text='-23')
        self.bound_min_label.pack(side='right')
        self.bounds_frame.pack(expand='true', fill='x', pady='5', side='top')
        self.learning_rate_frame = ttk.Frame(self.hyper_parameters_frame)
        self.learning_rate_label = ttk.Label(self.learning_rate_frame)
        self.learning_rate_label.configure(text='Learning Rate')
        self.learning_rate_label.pack(side='left')
        self.learning_rate_max_label = ttk.Label(self.learning_rate_frame)
        self.learning_rate_max_label.configure(text='0.01')
        self.learning_rate_max_label.pack(side='right')
        self.learning_rate_scale = ttk.Scale(self.learning_rate_frame)
        self.learning_rate = tk.DoubleVar(value=0.001)
        self.learning_rate_scale.configure(from_='0.001', length='180', orient='horizontal', to='0.01')
        self.learning_rate_scale.configure(value='0.001', variable=self.learning_rate)
        self.learning_rate_scale.pack(side='right')
        self.learning_rate_scale.bind('<FocusOut>', self._on_change, add='')
        self.learning_rate_scale.bind('<Return>', self._on_change, add='')
        self.learning_rate_scale.bind('<Unmap>', self._on_change, add='')
        self.learning_rate_min_label = ttk.Label(self.learning_rate_frame)
        self.learning_rate_min_label.configure(text='0.001')
        self.learning_rate_min_label.pack(side='right')
        self.learning_rate_frame.configure(height='300', width='300')
        self.learning_rate_frame.pack(expand='true', fill='x', pady='5', side='top')
        self.max_epoch_frame = ttk.Frame(self.hyper_parameters_frame)
        self.max_epoch_label = ttk.Label(self.max_epoch_frame)
        self.max_epoch_label.configure(text='Max Epoch')
        self.max_epoch_label.pack(side='left')
        self.max_epoch_max_label = ttk.Label(self.max_epoch_frame)
        self.max_epoch_max_label.configure(text='500 ')
        self.max_epoch_max_label.pack(side='right')
        self.max_epoch_scale = ttk.Scale(self.max_epoch_frame)
        self.max_epoch = tk.IntVar(value=100)
        self.max_epoch_scale.configure(from_='50', length='180', orient='horizontal', to='500')
        self.max_epoch_scale.configure(value='100', variable=self.max_epoch)
        self.max_epoch_scale.pack(side='right')
        self.max_epoch_scale.bind('<FocusOut>', self._on_change, add='')
        self.max_epoch_scale.bind('<Return>', self._on_change, add='')
        self.max_epoch_scale.bind('<Unmap>', self._on_change, add='')
        self.max_epoch_min_label = ttk.Label(self.max_epoch_frame)
        self.max_epoch_min_label.configure(text='50')
        self.max_epoch_min_label.pack(side='right')
        self.max_epoch_frame.pack(expand='true', fill='x', pady='5', side='top')
        self.frame9 = ttk.Frame(self.hyper_parameters_frame)
        self.initialize_button = ttk.Button(self.frame9)
        self.initializeButton90x30_png = tk.PhotoImage(file='initializeButton90x30.png')
        self.initialize_button.configure(image=self.initializeButton90x30_png, style='Toolbutton', text='Initialize')
        self.initialize_button.pack(side='left')
        self.initialize_button.configure(command=self.initialize)
        self.perceptron_button = ttk.Button(self.frame9)
        self.perceptronButton100x30_png = tk.PhotoImage(file='perceptronButton100x30.png')
        self.perceptron_button.configure(image=self.perceptronButton100x30_png, state='disabled', text='Perceptron', width='15')
        self.perceptron_button.pack(side='right')
        self.perceptron_button.configure(command=self.train)
        self.frame9.configure(height='200', width='200')
        self.frame9.pack(expand='true', fill='x', pady='5', side='top')
        self.hyper_parameters_frame.configure(width='500')
        self.hyper_parameters_frame.pack(anchor='nw', expand='false', side='left')
        self.plot_frame = ttk.Frame(self.top_frame)
        self.plot_canvas = tk.Canvas(self.plot_frame)
        self.plot_canvas.configure(background='#e9e9e9', relief='flat')
        self.plot_canvas.pack(expand='true', fill='both', padx='50', side='top')
        self.plot_frame.pack(anchor='e', expand='true', fill='both', pady='20', side='right')
        self.top_frame.configure(height='200', width='300')
        self.top_frame.pack(anchor='center', expand='true', fill='both', padx='20', pady='20', side='top')
        self.frame11 = ttk.Frame(self.toplevel)
        self.frame12 = ttk.Frame(self.frame11)
        self.confision_matrix_label = ttk.Label(self.frame12)
        self.confision_matrix_label.configure(font='{Times New Roman} 24 {}', text='Confision Matrix')
        self.confision_matrix_label.pack(padx='20', pady='20', side='top')
        self.canvas2 = tk.Canvas(self.frame12)
        self.canvas2.configure(background='#e9e9e9', confine='true', takefocus=False)
        self.canvas2.pack(side='top')
        self.frame12.pack(expand='true', fill='x', padx='20', pady='20', side='left')
        self.frame13 = ttk.Frame(self.frame11)
        self.graph_error_label = ttk.Label(self.frame13)
        self.graph_error_label.configure(font='{Times New Roman} 24 {}', text='Graph Error')
        self.graph_error_label.pack(padx='20', pady='20', side='top')
        self.canvas3 = tk.Canvas(self.frame13)
        self.canvas3.configure(background='#e9e9e9')
        self.canvas3.pack(expand='true', side='top')
        self.frame13.configure(height='200', width='200')
        self.frame13.pack(expand='true', fill='x', padx='20', pady='20', side='right')
        self.frame11.configure(height='200', width='200')
        self.frame11.pack(fill='x', padx='20', pady='20', side='top')
        self.toplevel.configure(height='200', takefocus=False, width='200')
        self.toplevel.geometry('1440x900')
        self.toplevel.bind('', self., add='')

        # Main widget
        self.mainwindow = self.toplevel
    
    def _onchange(self):
        pass

    def _on_change(self, event=None):
        pass

    def initialize(self):
        pass

    def train(self):
        pass

    def (self, event=None):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = Ia2PerceptronGuiApp()
    app.run()

