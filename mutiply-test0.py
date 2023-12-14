import math
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
import random

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度


def gaussian(x, y, q):
    z = 0
    distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
    sigma_y = 0.22 * x / np.sqrt(1 + 0.0001 * x)  # y方向上的标准差
    sigma_z = 0.20 * x  # z方向上的标准差

    term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

    k = -0.5 * (y ** 2 / sigma_y ** 2)
    term2 = np.exp(k)

    term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

    gau_result = term1 * term2 * term3 * 500000
    # print(term1, term2, term3)
    # Use np.where to return gau_result where x >= 0, else return 0
    return np.where(x >= 0, gau_result, 0)


xo = random.uniform(-10, 10)
yo = random.uniform(-10, 10)

# 已知的热量点位
known_heat_sources = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                      (2, -3, gaussian(7 - xo, 5 - yo, Q_calculate)),
                      (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                      (4, -7, gaussian(3 - xo, 5 - yo, Q_calculate)),
                      (7, 0, gaussian(10 - xo, 7 - yo, Q_calculate))]  # Initialize with zero heat


def objective(params):
    xs, ys, q = params
    error = 0
    wx, wy, wq = 0.3, 0.3, 0.4  # Set the weights for x, y, and q
    for (x, y, heat) in known_heat_sources:
        weight = heat
        error_x = wx * (x - xs) ** 2
        error_y = wy * (y - ys) ** 2
        error_q = wq * (heat - gaussian(x, y, q)) ** 2
        error += weight * (error_x + error_y + error_q)
    return error


# Define the bounds for the parameters
bounds = [(-1, 0.5), (-0.5, 1), (0, 2)]

# Use optimization algorithm to find the source coordinates
result = differential_evolution(objective, bounds, maxiter=50000, tol=1e-10, atol=1e-10)

initial_guess = [1.0, 1.0]

# Known heat strength from the result of the heat source strength optimization
known_heat_strength = result.x[2]


def objective_1(params):
    xs, ys = params
    error = 0
    for (x, y, heat) in known_heat_sources:
        error_x = (x - xs) ** 2
        error_y = (y - ys) ** 2
        error_heat = (heat - gaussian(x, y, known_heat_strength)) ** 2
        error += np.sqrt(error_x + error_y + error_heat)
    return error


# Use optimization algorithm to find the source coordinates
result_1 = minimize(objective_1, initial_guess, method='L-BFGS-B')
# 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

# 获取迭代次数
iterations = result.nit
iterations_1 = result_1.nit

# 输出泄露点坐标和迭代次数
print(f"初始的泄漏源点坐标：({ '%.6f' % xo}, { '%.6f' % yo})")
print(f"反解_1的泄漏源点坐标：({ '%.4f' % result_1.x[0]}, { '%.4f' % result_1.x[1]})")
print(f"反解的泄漏源点坐标：({ '%.4f' % result.x[0]}, { '%.4f' % result.x[1]})")
print("泄漏源强度：", '%.10f' % result.x[2])
print("迭代次数：", iterations, iterations_1)

# Get the coordinates of the origin
origin_x = result.x[0]
origin_y = result.x[1]

# # Create a meshgrid covering the 500x500 range
# x = np.linspace(origin_x - 250, origin_x + 250, 500)
# y = np.linspace(origin_y - 250, origin_y + 250, 500)
# X, Y = np.meshgrid(x, y)
#
# # Calculate the Gaussian concentration for each grid point
# Z = gaussian(X, Y, result.x[2])
#
# # 绘制热图
# plt.imshow(Z, extent=[-20.0, 20.0, -20.0, 20.0], origin='lower', cmap='hot', vmin=0, vmax=70)
#
# # Add a colorbar
# plt.colorbar()
#
# # Add labels and title
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Gaussian Concentration Heatmap')
#
# # Add known heat sources to the plot
# for (x, y, heat) in known_heat_sources:
#     plt.scatter(x, y, color='green', marker='o')
#
# # Show the plot
# plt.show()
