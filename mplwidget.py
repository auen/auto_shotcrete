from PyQt5 import QtWidgets,QtCore
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import pyplot, font_manager

matplotlib.use('QT5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self):
        pyplot.style.use('dark_background')
        pyplot.rcParams['grid.color'] = '#555555'
        self.fig = Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111, projection='3d')

        label_font = 15

        font = {'family': 'normal',
                'size': label_font}

        matplotlib.rc('font', **font)

        matplotlib.rcParams['figure.dpi'] = 236

        # Styling
        self.fig.set_facecolor('#31363B')
        self.fig.subplots_adjust(left=0.0, right=1, top=1, bottom=0)
        self.ax.set_facecolor('#31363B')
        self.ax.w_xaxis.set_pane_color((49/255, 54/255, 59/255, 1))
        self.ax.w_yaxis.set_pane_color((49/255, 54/255, 59/255, 1))
        self.ax.w_zaxis.set_pane_color((49/255, 54/255, 59/255, 1))

        self.ax.set_xlabel('X [m]', fontsize=label_font)
        self.ax.set_ylabel('Y [m]', fontsize=label_font)
        self.ax.set_zlabel('Z [m]', fontsize=label_font)

        self.ax.view_init(10, 210)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

