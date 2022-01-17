import numpy as np

def calc_best_fuel(d, fuel_price):
    fuels = []
    for dest in range(max(d) + 1):
        fuels.append(sum([fuel_price[abs(x - dest)] for x in d]))
    return min(fuels)

d = list(map(int, open('input.txt').read().split(',')))
print(calc_best_fuel(d, list(range(max(d) + 1))))
print(calc_best_fuel(d, np.cumsum(range(max(d) + 1))))
