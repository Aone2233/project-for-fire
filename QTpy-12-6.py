import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leakage Calculation")
        self.setGeometry(100, 100, 400, 300)

        self.label1 = QLabel("Point 1 (x, y):")
        self.input1 = QLineEdit()
        self.label2 = QLabel("Point 2 (x, y):")
        self.input2 = QLineEdit()
        self.label3 = QLabel("Point 3 (x, y):")
        self.input3 = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        
        self.result_label = QLabel()
        self.figure_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.label3)
        layout.addWidget(self.input3)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.figure_label)

        self.setLayout(layout)

    def calculate(self):
        x1, y1 = map(float, self.input1.text().split(','))
        x2, y2 = map(float, self.input2.text().split(','))
        x3, y3 = map(float, self.input3.text().split(','))

        # 调用当前代码进行计算
        # 这里只是一个示例，您需要根据您的代码进行相应的计算
        result_x, result_y, result_intensity = calculate_leakage(x1, y1, x2, y2, x3, y3)

        self.result_label.setText(f"Leakage Point: ({result_x}, {result_y}), Intensity: {result_intensity}")

        # 生成可交互图像
        fig, ax = plt.subplots()
        ax.scatter([x1, x2, x3], [y1, y2, y3], color='red', label='Input Points')
        ax.scatter(result_x, result_y, color='blue', label='Leakage Point')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Leakage Calculation')
        self.figure_label.setPixmap(self.plot_to_pixmap(fig))

    def plot_to_pixmap(self, fig):
        fig.canvas.draw()
        width, height = fig.canvas.get_width_height()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
        qimage = QImage(image, width, height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

def calculate_leakage(x1, y1, x2, y2, x3, y3):
    # 在这里进行泄漏点计算的具体逻辑
    # 这里只是一个示例，您需要根据您的代码进行相应的计算
    result_x = (x1 + x2 + x3) / 3
    result_y = (y1 + y2 + y3) / 3
    result_intensity = 0.5

    return result_x, result_y, result_intensity

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())