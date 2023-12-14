import math
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

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


known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                      (4, 7, gaussian(4, 7, Q_calculate)), (3, 5, gaussian(3, 5, Q_calculate)),
                      (10, 7, gaussian(10, 7, Q_calculate))]  # Initialize with zero heat


def objective(params):
    xs, ys, q = params
    error = 0
    wx, wy, wq = 0.4, 0.4, 0.2  # Set the weights for x, y, and q
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

bounds_1 = [(-1, 0.5), (-0.5, 1)]

# Known heat strength from the result of the heat source strength optimization
known_heat_strength = result.x[2]


def objective_1(params):
    xs, ys = params
    error = 0
    for (x, y, heat) in known_heat_sources:
        weight = np.sqrt(x ** 2 + y ** 2)  # Set the weight as the distance to the origin
        error += weight * np.abs(heat - gaussian(x - xs, y - ys, known_heat_strength))  # Use absolute error
    error += 0.01 * (xs ** 2 + ys ** 2)  # Add regularization term
    return error


# Use optimization algorithm to find the source coordinates
result_1 = differential_evolution(objective_1, bounds_1, maxiter=50000, tol=1e-10, atol=1e-10)
# 最小化objection，初值条件是initial_guess，采用的算法是TNC

# 获取迭代次数
iterations = result.nit
iterations_1 = result_1.nit

# 输出泄露点坐标和迭代次数
print(f"反解的泄漏源点坐标：({result_1.x[0]}, {result_1.x[1]})")
print("泄漏源强度：", result.x[2])
print("迭代次数：", iterations, iterations_1)

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
