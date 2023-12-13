import sys
import math
import numpy as np
from PyQt5.QtGui import QPixmap
from scipy.optimize import minimize
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度

#  此处引入的是我们设计的界面的类，在first.py文件中
from first import Ui_Form

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

# 新建类来继承UiForm，这样我们再更改界面后，不用再去修改我们写的逻辑
class DemoUi(QWidget, Ui_Form):
    # 类的初始化
    def __init__(self):
        super(DemoUi, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("毒气泄漏源反演与重绘制")
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.matplotlib.setLayout(layout)
    # 实现定义的槽函数逻辑
    def on_calculateButton_clicked(self):
        # 获取输入框的值
        global con1_x, con1_y, con1_q, con2_x, con2_y, con2_q, con3_x, con3_y, con3_q
        con1_x = self.con1_x.text()
        con1_y = self.con1_y.text()
        con1_q = self.con1_q.text()
        con2_x = self.con2_x.text()
        con2_y = self.con2_y.text()
        con2_q = self.con2_q.text()
        con3_x = self.con3_x.text()
        con3_y = self.con3_y.text()
        con3_q = self.con3_q.text()

        # 定义高斯函数计算
        def gaussian(x, y, q):
            z = 0
            distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
            sigma_y = 0.22 * distance / np.sqrt(1 + 0.0001 * distance)  # y方向上的标准差
            sigma_z = 0.20 * x  # z方向上的标准差

            term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

            k = -0.5 * (y ** 2 / sigma_y ** 2)
            term2 = np.exp(k)

            term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

            gau_result = term1 * term2 * term3 * 100000
            # print(term1, term2, term3)
            return gau_result

        # 已知的热量点位
        known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                              (4, 7, gaussian(4, 7, Q_calculate))]  # Initialize with zero heat

        def objective(params):
            xs, ys, q = params
            error = 0
            for (x, y, heat) in known_heat_sources:
                error += np.sqrt((heat - gaussian(x - xs, y - ys, q)) ** 2)
            return error  # Minimize the negative of the Gaussian function

        # 初值估计
        initial_guess = [0.5, 0.5, 0.5]

        result = minimize(objective, initial_guess, method='L-BFGS-B', options={'maxiter': 10000})
        # 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

        # 将计算得到的result值设置到result_x，result_y和result_q上
        self.result_out_x.setText(str(result.x[0]))
        self.result_out_y.setText(str(result.x[1]))
        self.result_out_q.setText(str(result.x[2]))
        # 获取迭代次数
        iterations = result.nit
        # 将迭代次数设置到result_interation上
        self.result_interation.setText(str(iterations))

        # 创建热力图
        x = np.linspace(-10, 10, 500)
        y = np.linspace(-10, 10, 500)
        X, Y = np.meshgrid(x, y)
        Z = gaussian(X - result.x[0], Y - result.x[1], result.x[2])
        self.canvas.axes.imshow(Z, extent=[-10, 10, -10, 10], origin='lower', cmap='hot', alpha=0.5)
        self.canvas.axes.set_title('Heatmap')
        self.canvas.draw()
        # 将画布上的图像捕获为QPixmap，并设置为matplotlib标签的图像
        pixmap = QPixmap.grabWidget(self.canvas)
        self.matplotlib.setPixmap(pixmap)

    def calculate(self):
        pass


# 此处是测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dm = DemoUi()
    dm.show()
    sys.exit(app.exec())
