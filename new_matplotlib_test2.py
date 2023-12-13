import sys
from PyQt6 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pandas as pd

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        df = pd.DataFrame([
            [0, 10], [5, 15], [2, 20], [15, 25], [4, 10],
        ], columns=['A', 'B'])
        df.plot(ax=sc.axes)
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the main window and set it as the central widget of another widget
    main_window = MainWindow()
    
    # Create a placeholder widget to hold the main window
    container_widget = QtWidgets.QWidget()
    container_layout = QtWidgets.QVBoxLayout()
    container_layout.addWidget(main_window)
    container_widget.setLayout(container_layout)
    
    # Show the container widget
    container_widget.show()
    
    sys.exit(app.exec())
