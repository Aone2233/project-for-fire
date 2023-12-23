import sys
import math
import numpy as np
import pyqtgraph as pg
import self
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from scipy.optimize import minimize, differential_evolution
from PyQt5.QtWidgets import *
import random
import matplotlib.pyplot as plt

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
global u, u_x, u_y, ang_u
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度
# 已知的热量点位
xo = random.uniform(2, 15)
yo = random.uniform(-5, 5)
# 全局变量声明
global con1_x, con1_y, con1_q, con2_x, con2_y, con2_q, con3_x, con3_y, con3_q, con4_x, con4_y, con4_q, con5_x, con5_y, con5_q, con6_x, con6_y, con6_q, con7_x, con7_y, con7_q, con8_x, con8_y, con8_q, con9_x, con9_y, con9_q, con10_x, con10_y, con10_q, xs_r, ys_r, qs_r
from first import Ui_Form


class DemoUi(QWidget, Ui_Form):
    # 类的初始化
    def __init__(self):
        super(DemoUi, self).__init__()
        self.known_heat_sources_0 = None
        self.known_heat_sources = []
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

        # 获取输入框的值

    # 实现定义的槽函数逻辑
    def on_calculateButton1_clicked(self):
        # self.con1_x = self.con1_x.text()
        # self.con1_y = self.con1_y.text()
        # self.con1_q = self.con1_q.text()
        # self.con2_x = self.con2_x.text()
        # self.con2_y = self.con2_y.text()
        # self.con2_q = self.con2_q.text()
        # self.con3_x = self.con3_x.text()
        self.known_heat_sources_0 = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                                     (2, -3, gaussian(2 - xo, -3 - yo, Q_calculate)),
                                     (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                                     (4, -7, gaussian(4 - xo, -7 - yo, Q_calculate)),
                                     (15, 10, gaussian(15 - xo, 10 - yo, Q_calculate)),
                                     (15, -10, gaussian(15 - xo, -10 - yo, Q_calculate))]  # 已知泄漏点位

        # # 将输入的内容加入到已知的热量点位中
        # if con1_x != '' and con1_y != '' and con1_q != '':
        #     self.known_heat_sources.append((float(con1_x), float(con1_y), float(con1_q)))
        # if con2_x != '' and con2_y != '' and con2_q != '':
        #     self.known_heat_sources.append((float(con2_x), float(con2_y), float(con2_q)))
        # if con3_x != '' and con3_y != '' and con3_q != '':
        #     self.known_heat_sources.append((float(con3_x), float(con3_y), float(con3_q)))
        # if con4_x != '' and con4_y != '' and con4_q != '':
        #     self.known_heat_sources.append((float(con4_x), float(con4_y), float(con4_q)))
        # if con5_x != '' and con5_y != '' and con5_q != '':
        #     self.known_heat_sources.append((float(con5_x), float(con5_y), float(con5_q)))
        # if con6_x != '' and con6_y != '' and con6_q != '':
        #     self.known_heat_sources.append((float(con6_x), float(con6_y), float(con6_q)))
        # if con7_x != '' and con7_y != '' and con7_q != '':
        #     self.known_heat_sources.append((float(con7_x), float(con7_y), float(con7_q)))
        # if con8_x != '' and con8_y != '' and con8_q != '':
        #     self.known_heat_sources.append((float(con8_x), float(con8_y), float(con8_q)))
        # if con9_x != '' and con9_y != '' and con9_q != '':
        #     self.known_heat_sources.append((float(con9_x), float(con9_y), float(con9_q)))
        # if con10_x != '' and con10_y != '' and con10_q != '':
        #     self.known_heat_sources.append((float(con10_x), float(con10_y), float(con10_q)))

        additional_heat_sources = []
        for (x, y, heat) in self.known_heat_sources_0:
            for x_new in np.arange(x - 1.5, x + 1.5, 0.5):
                for y_new in np.arange(y - 2, y + 2, 0.5):
                    heat_new = gaussian(x_new - xo, y_new - yo, Q_calculate)
                    additional_heat_sources.append((x_new, y_new, heat_new))

        # 将新生成的热源添加到已知的热源列表中
        self.known_heat_sources.extend(additional_heat_sources)

        def objective(params):
            xs, ys, q = params
            error = 0
            for (x, y, heat) in self.known_heat_sources:
                error += np.sqrt((heat - gaussian(x - xs, y - ys, q)) ** 2)
            return error  # Minimize the negative of the Gaussian function

        # 定义参数的边界
        bounds = [(-20.0, 20.0), (-20.0, 20.0), (0, 2.0)]

        # 使用优化算法找到源的坐标
        result = differential_evolution(
            objective, bounds, tol=1e-15, atol=1e-15, maxiter=10000)

        # 获取迭代次数
        iterations = result.nit

        # 优化算法实现的初始猜测泄漏源点浓度
        initial_guess_1 = 0.5

        def objective_1(params):
            qs = params
            error = 0
            for (x, y, heat) in self.known_heat_sources:
                error += (heat - gaussian(x - result.x[0], y - result.x[1], qs)) ** 2
            return error

        # 使用优化算法找到源的坐标
        result_1 = minimize(objective_1, initial_guess_1, method='L-BFGS-B')
        # 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

        # 将计算得到的result值设置到result_x，result_y和result_q上
        self.result_out_x.setText(str(result.x[0]))
        self.result_out_y.setText(str(result.x[1]))
        self.result_out_q.setText(str(result_1.x[0]))
        # 将迭代次数设置到result_interation上
        self.result_interation.setText(str(iterations))
        # Update the plot with simulation results
        # self.on_plotButton_clicked([result.x[0]], [result.x[1]], [result.x[2]])
        self.xs_r = result.x[0]
        self.ys_r = result.x[1]
        self.qs_r = result_1.x[0]

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
        for (x, y, heat) in self.known_heat_sources_0:
            plt.scatter(x, y, color='green', marker='o', s=50, label='Known Heat Source')  # Plot the known heat sources

        # Show the plot
        plt.show()
        plt.close()

    # 对于蒙卡方法的求解过程
    def on_calculateButton2_clicked(self):

        self.known_heat_sources_0 = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                                     (2, -3, gaussian(2 - xo, -3 - yo, Q_calculate)),
                                     (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                                     (4, -7, gaussian(4 - xo, -7 - yo, Q_calculate)),
                                     (15, 10, gaussian(15 - xo, 10 - yo, Q_calculate)),
                                     (15, -10, gaussian(15 - xo, -10 - yo, Q_calculate))]  # 已知泄漏点位

        additional_heat_sources = []
        for (x, y, heat) in self.known_heat_sources_0:
            for x_new in np.arange(x - 1.5, x + 1.5, 0.5):
                for y_new in np.arange(y - 2, y + 2, 0.5):
                    heat_new = gaussian(x_new - xo, y_new - yo, Q_calculate)
                    additional_heat_sources.append((x_new, y_new, heat_new))

        # 将新生成的热源添加到已知的热源列表中
        known_heat_sources = []
        known_heat_sources.extend(additional_heat_sources)

        def calculate_error(xs, ys, qs):
            error = 0
            for (x, y, heat) in known_heat_sources:
                error += (heat - gaussian(x - xs, y - ys, qs)) ** 2
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
