import sys
import math
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from scipy.optimize import minimize
from PyQt5.QtWidgets import *
import random
import matplotlib.pyplot as plt

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度

from first import Ui_Form
#全局变量声明
global con1_x, con1_y, con1_q, con2_x, con2_y, con2_q, con3_x, con3_y, con3_q, xs_r, ys_r, qs_r

class DemoUi(QWidget, Ui_Form):
    # 类的初始化
    def __init__(self):
        super(DemoUi, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('毒气泄漏源定位')
        self.setWindowIcon(QIcon('logo.ico'))
        self.calculateButton1.clicked.connect(self.on_calculateButton1_clicked)
        self.calculateButton2.clicked.connect(self.on_calculateButton2_clicked)
        self.plotButton.clicked.connect(self.on_plotButton_clicked)  # 假设你有一个名为plotButton的按钮
        # self.progress_bar.setValue(0)
        self.xs_r = None
        self.ys_r = None
        self.qs_r = None

        # self.plot_widget = pg.PlotWidget()

    # 实现定义的槽函数逻辑
    def on_calculateButton1_clicked(self):
        # 获取输入框的值
        con1_x = self.con1_x.text()
        con1_y = self.con1_y.text()
        con1_q = self.con1_q.text()
        con2_x = self.con2_x.text()
        con2_y = self.con2_y.text()
        con2_q = self.con2_q.text()
        con3_x = self.con3_x.text()
        con3_y = self.con3_y.text()
        con3_q = self.con3_q.text()

        # 将输入框的值转换为float类型

        # 已知的热量点位
        self.known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                              (4, 7, gaussian(4, 7, Q_calculate))]  # Initialize with zero heat

        def objective(params):
            xs, ys, q = params
            error = 0
            for (x, y, heat) in self.known_heat_sources:
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
        # Update the plot with simulation results
        # self.on_plotButton_clicked([result.x[0]], [result.x[1]], [result.x[2]])
        self.xs_r = result.x[0]
        self.ys_r = result.x[1]
        self.qs_r = result.x[2]

    def calculate(self):
        pass

    # 实现定义的槽函数逻辑

    def on_plotButton_clicked(self):
        # Close all old figures
        plt.close('all')
        # Get the coordinates of the origin
        origin_x = self.xs_r
        origin_y = self.ys_r

        # Create a meshgrid covering the 500x500 range
        x = np.linspace(origin_x - 50, origin_x + 450, 500)
        y = np.linspace(origin_y - 250, origin_y + 250, 500)
        X, Y = np.meshgrid(x, y)

        # Calculate the Gaussian concentration for each grid point
        Z = gaussian(X, Y, self.qs_r)

        # 绘制热图
        plt.imshow(Z, extent=[-5.0, 45.0, -25.0, 25.0], origin='lower', cmap='hot', vmin=0, vmax=70)

        # Add a colorbar
        plt.colorbar()

        # Add labels and title
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Gaussian Concentration Heatmap')

        # Add known heat sources to the plot
        for (x, y, heat) in self.known_heat_sources:
            plt.scatter(x, y, color='green', marker='o', s=50, label='Known Heat Source')  # Plot the known heat sources

        # Show the plot
        plt.show()
        plt.close()
        
        
    def on_calculateButton2_clicked(self):
        # 获取输入框的值
        con1_x = self.con1_x.text()
        con1_y = self.con1_y.text()
        con1_q = self.con1_q.text()
        con2_x = self.con2_x.text()
        con2_y = self.con2_y.text()
        con2_q = self.con2_q.text()
        con3_x = self.con3_x.text()
        con3_y = self.con3_y.text()
        con3_q = self.con3_q.text()

        # 已知的热量点位
        known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                              (4, 7, gaussian(4, 7, Q_calculate))]

        def calculate_error(xs, ys, qs):
            error = 0
            for (x, y, heat) in known_heat_sources:
                error += (heat - gaussian(x - xs, y - ys, qs))**2
            return error

        # 进行蒙特卡罗模拟
        num_samples = 5000

        for i in range(num_samples):
            # 初始化最小误差为正无穷
            min_error = float('inf')
            best_xs, best_ys, best_q = None, None, None
            xs, ys = random.uniform(-10, 10), random.uniform(-10, 10)
            qs = random.uniform(0, 1)
            error = calculate_error(xs, ys, qs)

            # 如果当前误差更小，则更新最小误差和对应的坐标和强度值
            if error < min_error:
                min_error = error
                best_xs, best_ys, best_q = xs, ys, qs

            # # 计算进度
            # progress = int(round((i / num_samples) * 100))
            # self.progress_bar.setValue(progress)

        # 将计算得到的result值设置到result_x，result_y和result_q上
        self.result_out_x.setText(str(best_xs) if best_xs is not None else '')
        self.result_out_y.setText(str(best_ys) if best_ys is not None else '')
        self.result_out_q.setText(str(best_q) if best_q is not None else '')
        # 获取迭代次数
        iterations = num_samples
        # 将迭代次数设置到result_interation上
        self.result_interation.setText(str(iterations))
        # Update the plot with simulation results
        # self.on_plotButton_clicked([best_xs], [best_ys], [best_q])
        self.xs_r = best_xs
        self.ys_r = best_ys
        self.qs_r = best_q

    # def update_plot(self, xs, ys, qs):
    #     # Clear previous plot data
    #     self.plot_widget.clear()
    #
    #     # Plot the new data
    #     self.plot_widget.plot(xs, ys, pen=None, symbol='o', symbolBrush=(255, 0, 0), symbolSize=10)
    #
    #     # Set labels and title
    #     self.plot_widget.setLabel('left', 'Y Axis')
    #     self.plot_widget.setLabel('bottom', 'X Axis')
    #     self.plot_widget.setTitle('Simulation Results')

    def calculate(self):
        pass


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


# 此处是测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DemoUi()
    demo.show()
    sys.exit(app.exec_())
