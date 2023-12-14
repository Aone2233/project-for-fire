import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# 定义二维热传导方程模型
def heat_conduction_model(position, intensity, grid_size=(50, 50), alpha=0.01, time=1.0):
    x, y = np.meshgrid(np.linspace(0, 1, grid_size[0]), np.linspace(0, 1, grid_size[1]))
    distance = np.sqrt((x - position[0]) ** 2 + (y - position[1]) ** 2)
    source_term = intensity * np.exp(-distance ** 2 / (4 * alpha * time))
    return source_term


# 生成模拟观测数据
def generate_observation_data(true_position, true_intensity, noise_level=0.1):
    model_data = heat_conduction_model(true_position, true_intensity)
    noise = np.random.normal(0, noise_level, model_data.shape)
    observation_data = model_data + noise
    return observation_data


# 定义误差函数
def error_function(params, observation_data):
    position, intensity = params[:2], params[2]
    model_data = heat_conduction_model(position, intensity)
    error = np.sum((model_data - observation_data) ** 2)
    return error


# 最小二乘法求解
def inverse_heat_source_solver(observation_data, initial_guess):
    result = minimize(error_function, initial_guess, args=(observation_data,), method='L-BFGS-B')
    return result.x[:2], result.x[2]


# 主程序
true_position = [0.7, 0.7]
true_intensity = 5.0
observation_data = generate_observation_data(true_position, true_intensity)

initial_guess = [0.5, 0.5, 2.0]  # initial guess for position (x, y) and intensity

estimated_position, estimated_intensity = inverse_heat_source_solver(observation_data, initial_guess)

print("True Position:", true_position)
print("Estimated Position:", estimated_position)
print("True Intensity:", true_intensity)
print("Estimated Intensity:", estimated_intensity)

# 可视化
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.imshow(heat_conduction_model(true_position, true_intensity), cmap='hot', origin='lower')
plt.title("True Heat Distribution")

plt.subplot(1, 3, 2)
plt.imshow(observation_data, cmap='hot', origin='lower')
plt.title("Observed Temperature Distribution")

plt.subplot(1, 3, 3)
plt.imshow(heat_conduction_model(estimated_position, estimated_intensity), cmap='hot', origin='lower')
plt.title("Estimated Heat Distribution")

plt.show()
