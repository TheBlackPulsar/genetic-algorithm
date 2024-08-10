import numpy as np
import math

def get_shift_values(x_range, y_range, random_number):
    np.random.seed(random_number)
    x_shift = np.random.uniform(x_range[0], x_range[1])
    y_shift = np.random.uniform(y_range[0], y_range[1])
    return x_shift, y_shift

def dynamic2(candidate, random_number):
    x_shift, y_shift = get_shift_values([-50, 50], [-50, 50], random_number)
    x, y = candidate[0] + x_shift, candidate[1] + y_shift
    return -2 * np.exp(-1/20 * math.pow(x/5, 2) - 1/20 * math.pow(y/5, 2)) \
           * math.pow(np.cos(x/5), 1) * math.pow(np.cos(y/5), 1) + 2
