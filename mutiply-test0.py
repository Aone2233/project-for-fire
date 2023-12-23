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
u = 1.05  # 实时风速，x方向上的风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = random.uniform(0.01, 0.6)  # 毒气源强度
print("Q_calculate:", Q_calculate)
xo = random.uniform(2, 15)
yo = random.uniform(-5, 5)
print(f"初始的泄漏源点坐标：({'%.6f' % xo}, {'%.6f' % yo})")


def gaussian(x, y, q):
    if np.any(x < 0):
        return np.zeros_like(x)
    
    z = 0
    distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
    sigma_y = 0.22 * x / np.sqrt(1 + 0.0001 * x)# y方向上的标准差
    sigma_z = 0.20 * x  # z方向上的标准差

    term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

    k = -0.5 * (y ** 2 / sigma_y ** 2)
    term2 = np.exp(k)

    term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

    gau_result = term1 * term2 * term3 * 500000
    # print(term1, term2, term3)
    # Use np.where to return gau_result where x >= 0, else return 0
    return gau_result


# 已知的热量点位
known_heat_sources = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                      (2, -3, gaussian(2 - xo, -3 - yo, Q_calculate)),
                      (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                      (4, -7, gaussian(4 - xo, -7 - yo, Q_calculate)),
                      (15, 10, gaussian(15 - xo, 10 - yo, Q_calculate)),
                      (15, -10, gaussian(15 - xo, -10 - yo, Q_calculate))]  # 已知泄漏点位

# 在每个已知的热源周围的±2范围内生成一个0.5x0.5的网格
additional_heat_sources = []
for (x, y, heat) in known_heat_sources:
    for x_new in np.arange(x - 2, x + 2, 0.2):
        for y_new in np.arange(y - 2, y + 2, 0.2):
            heat_new = gaussian(x_new - xo, y_new - yo, Q_calculate)
            additional_heat_sources.append((x_new, y_new, heat_new))

# 将新生成的热源添加到已知的热源列表中
known_heat_sources.extend(additional_heat_sources)

def objective(params):
    xs, ys, q = params  # 这里的xs, ys, q会导入初始值，即initial_guess
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += (heat - gaussian(x - xs, y - ys, q)) ** 2
    return error


# Define the bounds for the parameters
bounds = [(-20.0, 20.0), (-20.0, 20.0), (0, 2.0)]

# Use optimization algorithm to find the source coordinates
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
        error += (heat - gaussian(x-result.x[0], y - result.x[1], qs)) ** 2
    return error


# Use optimization algorithm to find the source coordinates
result_1 = minimize(objective_1, initial_guess_1, method='L-BFGS-B')
# 最小化objection，初值条件是initial_guess，采用的算法是L-BFGS-B

# 获取迭代次数
iterations_1 = result_1.nit


print("反解的泄漏源点浓度：", {'%.7f' % result_1.x[0]})
print("迭代次数：", iterations_1)

###################################
# 优化算法实现的初始猜测泄漏源点坐标
# initial_guess = [result.x[0], result.x[1], result_1.x[0]]

# # 使用模式搜索算法找到最优解
# result_pattern_search = basinhopping(objective, initial_guess, niter=10000, stepsize=0.1)


# # 输出最优解和对应的目标函数值
# print("Pattern search solution: ", result_pattern_search.x)
# print("With fitness: ", result_pattern_search.fun)




# #绘图部分代码。绘制热图

# # Get the coordinates of the origin
# origin_x = result.x[0]
# origin_y = result.x[1]

# # Create a meshgrid covering the 500x500 range
# x = np.linspace(origin_x - 50, origin_x + 450, 500)
# y = np.linspace(origin_y - 250, origin_y + 250, 500)
# X, Y = np.meshgrid(x, y)

# # # Calculate the Gaussian concentration for each grid point
# Z = gaussian(X, Y, result_1.x[0])


# # 绘制热图
# plt.imshow(Z, extent=[-5.0, 45.0, -25.0, 25.0],
#            origin='lower', cmap='hot', vmin=0, vmax=70)

# # Add a colorbar
# plt.colorbar()

# # Add labels and title
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Gaussian Concentration Heatmap')

# # Add known heat sources to the plot
# for (x, y, heat) in known_heat_sources:
#     plt.scatter(x, y, color='green', marker='o', s=50,
#                 label='Known Heat Source')  # Plot the known heat sources

# # Show the plot
# plt.show()
# plt.close()

