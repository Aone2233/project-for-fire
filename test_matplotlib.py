import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QToolBar, QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import SpanSelector
import numpy as np

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        self.setLayout(layout)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("My Plot Title")
        self.ax.set_xlabel("X-axis Label")
        self.ax.set_ylabel("Y-axis Label")

        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.line, = self.ax.plot(x, y, linestyle='-', color='b', label='My Data')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-1, 1)
        self.ax.grid(True)
        self.ax.legend()

        self.selector = SpanSelector(self.ax, self.on_select, 'horizontal', useblit=True)

        self.slider = QSlider()
        self.slider.setOrientation(1)  # Qt.Horizontal
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSliderPosition(50)
        self.slider.valueChanged.connect(self.on_slider_change)
        layout.addWidget(self.slider)

    def on_select(self, xmin, xmax):
        self.ax.set_xlim(xmin, xmax)
        self.canvas.draw()

    def on_slider_change(self, value):
        zoom_factor = value / 50.0
        self.ax.set_xlim(0, 10 * zoom_factor)
        self.canvas.draw()

class NavigationToolbar(QToolBar):
    def __init__(self, canvas, parent):
        super(NavigationToolbar, self).__init__("Navigation Toolbar", parent)
        self.canvas = canvas
        self.addAction(QAction("Home", self, triggered=self.home))
        self.addAction(QAction("Back", self, triggered=self.back))
        self.addAction(QAction("Forward", self, triggered=self.forward))

    def home(self):
        self.canvas.ax.set_xlim(0, 10)
        self.canvas.ax.set_ylim(-1, 1)
        self.canvas.draw()

    def back(self):
        # Add logic for 'Back' button
        pass

    def forward(self):
        # Add logic for 'Forward' button
        pass

def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    central_widget = MatplotlibWidget(main_window)
    main_window.setCentralWidget(central_widget)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
