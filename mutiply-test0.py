import math
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
from scipy.optimize import basinhopping
# from scipy.optimize import dual_annealing
# from scipy.optimize import least_squares
import random

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
# 对于风速u进行方向上的判定
u_x = 3
u_y = 4
u = 1.05  # 实时风速，x方向上的风速
ang_u = math.atan(u_y / u_x)  # 风向与x轴的夹角
print(ang_u)
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = random.uniform(0.01, 0.6)  # 毒气源强度
print("Q_calculate:", Q_calculate)
xo = random.uniform(2, 15)
yo = random.uniform(-5, 5)
print(f"初始的泄漏源点坐标：({'%.6f' % xo}, {'%.6f' % yo})")


def gaussian(x, y, q):

    z = 0
    distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
    sigma_y = 0.22 * distance / np.sqrt(1 + 0.0001 * distance)  # y方向上的标准差
    sigma_z = 0.20 * x  # z方向上的标准差

    term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

    k = -0.5 * (y ** 2 / sigma_y ** 2)
    term2 = np.exp(k)

    term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

    gau_result = term1 * term2 * term3 * 50000
    # print(term1, term2, term3)
    # 使用np.where函数返回当x>=0时的gau_result，否则返回0
    return gau_result


# 已知的热量点位
known_heat_sources_0 = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                        (2, -3, gaussian(2 - xo, -3 - yo, Q_calculate)),
                        (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                        (4, -7, gaussian(4 - xo, -7 - yo, Q_calculate)),
                        (15, 10, gaussian(15 - xo, 10 - yo, Q_calculate)),
                        (15, -10, gaussian(15 - xo, -10 - yo, Q_calculate))]  # 已知泄漏点位

# 在每个已知的热源周围±2范围内生成一个0.5x0.5的网格
additional_heat_sources = []
for (x, y, heat) in known_heat_sources_0:
    for x_new in np.arange(x - 1.5, x + 1.5, 0.5):
        for y_new in np.arange(y - 2, y + 2, 0.5):
            heat_new = gaussian(x_new - xo, y_new - yo, Q_calculate)
            additional_heat_sources.append((x_new, y_new, heat_new))

# 将新生成的热源添加到已知的热源列表中
known_heat_sources = []
known_heat_sources.extend(additional_heat_sources)


# 对于原始数据进行处理，使其绕原点逆时针旋转ang_u角度
def cw_rotate(x, y, ang):
    # 定义旋转矩阵
    rotation_matrix = np.array([[math.cos(math.radians(ang)), -math.sin(math.radians(ang))],
                                [math.sin(math.radians(ang)), math.cos(math.radians(ang))]])
    # 进行坐标变换
    rotated_x, rotated_y = np.dot(rotation_matrix, np.array([x, y]))
    # 用round()保留5位小数
    new_x = round(rotated_x, 5)
    new_y = round(rotated_y, 5)
    return new_x, new_y


# 逆时针旋转
def ccw_rotate(x, y, ang):
    ang = math.radians(ang)     # 将角度转换成弧度
    # 用round()保留5位小数
    new_x = round(x * math.cos(ang) - y * math.sin(ang), 5)
    new_y = round(x * math.sin(ang) + y * math.cos(ang), 5)
    return new_x, new_y


# 对已知的热量点位进行坐标变换
rotated_known_heat_sources = []
for (x, y, heat) in known_heat_sources:
    rotated_x, rotated_y = cw_rotate(x, y, ang_u)
    rotated_known_heat_sources.append((rotated_x, rotated_y, heat))


def objective(params):
    xs, ys, q = params  # 这里的xs, ys, q会导入初始值，即initial_guess
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += (heat - gaussian(x - xs, y - ys, q)) ** 2
    return error


# 定义参数的边界
bounds = [(-20.0, 20.0), (-20.0, 20.0), (0, 2.0)]

# 使用优化算法找到源的坐标
result = differential_evolution(
    objective, bounds, tol=1e-15, atol=1e-15, maxiter=10000)

# 获取迭代次数
iterations = result.nit

print(f"反解的泄漏源点坐标：({'%.5f' % result.x[0]}, {'%.5f' % result.x[1]})")
print("目标函数值：", result.fun)
print("迭代次数：", iterations)

# 优化算法实现的初始猜测泄漏源点浓度
initial_guess_1 = 0.5


def objective_1(params):
    qs = params
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += (heat - gaussian(x - result.x[0], y - result.x[1], qs)) ** 2
    return error


# 使用优化算法找到源的坐标
result_1 = minimize(objective_1, initial_guess_1, method='L-BFGS-B')
# 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

# 获取迭代次数
iterations_1 = result_1.nit

# 打印反解的泄漏源点浓度，保留8位数字
print("反解的泄漏源点浓度：", round(result_1.x[0], 8))
# 打印目标函数值
print("迭代次数：", iterations_1)
##################################

print("绘图检查", gaussian(result.x[0] + 30, result.x[1] + 10, result_1.x[0]))
###################################

# 绘图部分代码。绘制热图
# 获取坐标原点
origin_x = result.x[0]
origin_y = result.x[1]
origin_q = result_1.x[0]

# 创建一个500x500范围的网格点
x = np.linspace(origin_x - 50, origin_x + 450, 500)
y = np.linspace(origin_y - 250, origin_y + 250, 500)
X, Y = np.meshgrid(x, y)


# 计算每个网格点上的高斯浓度
Z = gaussian(X, Y, origin_q)

# 绘制热图
plt.imshow(Z, extent=[-5.0, 45.0, -25.0, 25.0],
           origin='lower', cmap='hot', vmin=0, vmax=20)

# 添加颜色条
plt.colorbar()

# 添加标签和标题
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gaussian Concentration Heatmap')

# 添加已知的热源点
for (x, y, heat) in known_heat_sources_0:
    plt.scatter(x, y, color='green', marker='o', s=50,
                label='Known Heat Source')  # 绘制已知的热源点

# 显示图像
plt.show()