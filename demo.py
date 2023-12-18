import sys
import math
import numpy as np
from scipy.optimize import minimize
from PyQt5.QtWidgets import *
import random
import threading

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度

#  此处引入的是我们设计的界面的类，在first.py文件中
from first import Ui_Form


# 新建类来继承UiForm，这样我们再更改界面后，不用再去修改我们写的逻辑
class DemoUi(QWidget, Ui_Form):
    # 类的初始化
    def __init__(self):
        super(DemoUi, self).__init__()
        self.setupUi(self)

    # 实现定义的槽函数逻辑
    def on_calculateButton1_clicked(self):
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

        # 将输入框的值转换为float类型
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

    def calculate(self):
        pass

    def on_calculateButton2_clicked(self):
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

        # 将输入框的值转换为float类型
        def gaussian(x, y, q):
            z = 0
            distance = np.sqrt(x ** 2 + y ** 2)
            sigma_y = 0.22 * distance / np.sqrt(1 + 0.0001 * distance)
            sigma_z = 0.20 * x

            term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

            k = -0.5 * (y ** 2 / sigma_y ** 2)
            term2 = np.exp(k)

            term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

            gau_result = term1 * term2 * term3 * 100000
            # print(term1, term2, term3)
            return gau_result

        # 已知的热量点位
        known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                              (4, 7, gaussian(4, 7, Q_calculate))]

        # 初始猜测的泄漏源点坐标
        initial_guess = [random.uniform(-5, 5), random.uniform(-5, -5)]

        def calculate_error(xs, ys, qs):
            error = 0
            for (x, y, heat) in known_heat_sources:
                error += np.sqrt((heat - gaussian(x - xs, y - ys, qs)) ** 2)
            return error

        # 进行蒙特卡罗模拟
        num_samples = 500000
        num_threads = 5


        # 定义子循环的函数
        def worker(start, end):
            global min_error, best_xs, best_ys, best_q
            min_error = 1e-20
            best_xs, best_ys = None, None
            best_q = None
            for i in range(start, end):
                xs, ys = random.uniform(-10, 10), random.uniform(-10, 10)
                qs = random.uniform(0, 1)
                error = calculate_error(xs, ys, qs)
                if error < min_error:
                    min_error = error
                    best_xs, best_ys = xs, ys
                    best_q = qs


        # 开启多线程
        threads = []
        for i in range(num_threads):
            start = int(i * num_samples / num_threads)
            end = int((i + 1) * num_samples / num_threads)
            t = threading.Thread(target=worker, args=(start, end))
            threads.append(t)
            t.start()

        # 等待所有线程结束
        for t in threads:
            t.join()

        # 将计算得到的result值设置到result_x，result_y和result_q上
        self.result_out_x.setText(str(best_xs))
        self.result_out_y.setText(str(best_ys))
        self.result_out_q.setText(str(best_q))
        # 获取迭代次数
        iterations = 10000
        # 将迭代次数设置到result_interation上

        self.result_interation.setText(str(iterations))

    def update_progess(self, value):

        pass

# 此处是测试代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dm = DemoUi()
    dm.show()
    sys.exit(app.exec())
