import random
import math
import numpy as np
from scipy.optimize import minimize
import threading
import matplotlib.pyplot as plt

# q = 0.05  # 毒气源强度
H = 0.5  # 毒气源高度
u = 0.05  # 实时风速
# sigma_x = 0.105  # x方向上的标准差
Q_calculate = 0.05


# z = 0
#高斯函数的定义和相关实现
def gaussian(x, y, q):
    z = 0
    distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
    sigma_y = 0.22 * x / (np.sqrt(1 + 0.0001 * x) + 1e-20)  # y方向上的标准差
    sigma_z = 0.20 * x + 1e-20  # z方向上的标准差

    # 确保sigma_y和sigma_z的值不会小于1e-8
    sigma_y = np.where(sigma_y < 1e-20, 1e-20, sigma_y)
    sigma_z = np.where(sigma_z < 1e-20, 1e-20, sigma_z)

    term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

    k = -0.5 * (y ** 2 / sigma_y ** 2)
    term2 = np.exp(k)

    term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

    gau_result = term1 * term2 * term3 * 500000
    # print(term1, term2, term3)
    # Use np.where to return gau_result where x >= 0, else return 0
    return np.where(x >= 0, gau_result, 0)


# print(gaussian(2, 3))

# 已知的热量点位
known_heat_sources = [(2, 3, gaussian(2, 3, Q_calculate)), (7, 5, gaussian(7, 5, Q_calculate)),
                      (4, 7, gaussian(4, 7, Q_calculate))]


# # 初始猜测的泄漏源点坐标
# initial_guess = [random.uniform(-5, 5), random.uniform(-5, -5)]

def calculate_error(xs, ys, qs):
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += np.sqrt((heat ** 2 - gaussian(x - xs, y - ys, qs)) ** 2) ** 2
    return error


# 定义子循环的函数
def worker(start, end):
    global min_error, best_xs, best_ys, best_q
    for i in range(start, end):
        xs, ys = random.uniform(-10, 10), random.uniform(-10, 10)
        qs = random.uniform(0, 1)
        error = calculate_error(xs, ys, qs)
        if error < min_error:
            min_error = error
            best_xs, best_ys = xs, ys
            best_q = qs


# 进行蒙特卡罗模拟
num_samples = 50000
num_threads = 5
min_error = float('inf')
best_xs, best_ys = None, None
best_q = None

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

# 输出反解结果
print(f"反解的泄漏源点坐标：({best_xs}, {best_ys})")
print(f"反解的泄漏源强度：{best_q}")

# 画图代码
# Get the coordinates of the origin
origin_x = best_xs
origin_y = best_ys

# Create a meshgrid covering the 500x500 range
x = np.linspace(origin_x - 250, origin_x + 250, 500)
y = np.linspace(origin_y - 250, origin_y + 250, 500)
X, Y = np.meshgrid(x, y)

# Calculate the Gaussian concentration for each grid point
Z = gaussian(X, Y, best_q)

# 绘制热图
plt.imshow(Z, extent=[-5, 5, -5, 5], origin='lower', cmap='hot', vmin=0, vmax=70)

# 设置颜色轴刻度间隔
cbar = plt.colorbar()

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gaussian Concentration Heatmap')

# Show the plot
plt.show()
