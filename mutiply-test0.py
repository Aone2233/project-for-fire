import math
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import random

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05  # 毒气源强度


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


known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                      (4, 7, gaussian(4, 7, Q_calculate))]  # Initialize with zero heat


def objective(params):
    xs, ys, q = params
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += np.sqrt((heat - gaussian(x - xs, y - ys, q)) ** 2)
    return error  # Minimize the negative of the Gaussian function


# Initial guess
initial_guess = [0.5, 0.5, 0.5]

# Use optimization algorithm to find the source coordinates
result = minimize(objective, initial_guess, method='L-BFGS-B', options={'maxiter': 10000})
# 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

# 获取迭代次数
iterations = result.nit

# 输出泄露点坐标和迭代次数
print(f"反解的泄漏源点坐标：({result.x[0]}, {result.x[1]})")
print("泄漏源强度：", result.x[2])
print("迭代次数：", iterations)

# Get the coordinates of the origin
origin_x = result.x[0]
origin_y = result.x[1]

# Create a meshgrid covering the 500x500 range
x = np.linspace(origin_x - 250, origin_x + 250, 500)
y = np.linspace(origin_y - 250, origin_y + 250, 500)
X, Y = np.meshgrid(x, y)

# Calculate the Gaussian concentration for each grid point
Z = gaussian(X, Y, result.x[2])

# 绘制热图
plt.imshow(Z, extent=[-5.0, 5.0, -5.0, 5.0], origin='lower', cmap='hot', vmin=0, vmax=70)

# Add a colorbar
plt.colorbar()

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gaussian Concentration Heatmap')

# Show the plot
plt.show()
