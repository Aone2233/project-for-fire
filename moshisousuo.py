from deap import base, creator, tools
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
from scipy.optimize import dual_annealing
from scipy.optimize import least_squares
import random
import numpy as np
from deap import algorithms
import matplotlib.pyplot as plt
import time
import math

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
    z = 0
    distance = np.sqrt(x ** 2 + y ** 2)  # 距原点距离
    sigma_y = 0.22 * x / (np.sqrt(1 + 0.0001 * x) + 1e-20)  # y方向上的标准差
    sigma_z = 0.20 * x + 1e-20  # z方向上的标准差

    # Replace values in sigma_y and sigma_z that are less than 1e-8 with 1e-8
    sigma_y = np.where(sigma_y < 1e-20, 1e-20, sigma_y)
    sigma_z = np.where(sigma_z < 1e-20, 1e-20, sigma_z)

    term1 = q / (2 * math.pi * u * sigma_y * sigma_z)

    k = -0.5 * (y ** 2 / sigma_y ** 2)
    term2 = np.exp(k)

    term3 = np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2)) + \
        np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))

    gau_result = term1 * term2 * term3 * 500000
    # print(term1, term2, term3)
    # Use np.where to return gau_result where x >= 0, else return 0
    return np.where(x >= 0, gau_result, 0)

# 创建一个最小化问题
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -20, 20)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
    return objective(individual),

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)

    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)

    return pop, logbook, hof

known_heat_sources = [(2, 3, gaussian(2 - yo, 3 - yo, Q_calculate)),
                      (2, -3, gaussian(2 - xo, -3 - yo, Q_calculate)),
                      (4, 7, gaussian(4 - xo, 7 - yo, Q_calculate)),
                      (4, -7, gaussian(4 - xo, -7 - yo, Q_calculate)),
                      (15, 10, gaussian(15 - xo, 10 - yo, Q_calculate)),
                      (15, -10, gaussian(15 - xo, -10 - yo, Q_calculate))]  # 已知泄漏点位


def objective(params):
    xs, ys, qs = params  # 这里的xs, ys, q会导入初始值，即initial_guess
    error = 0
    for (x, y, heat) in known_heat_sources:
        error += (heat - gaussian(x - xs, y - ys, qs)) ** 2
    return error

if __name__ == "__main__":
    pop, log, hof = main()
    print("Best individual is: %s\nwith fitness: %s" % (hof[0], hof[0].fitness))

    # Use pattern search to fine-tune the solution
    res = minimize(objective, hof[0], method='L-BFGS-B')
    print("Refined solution: ", res.x)