# Grid module

import numpy as np

from scipy.spatial.distance import cdist

def init(rows, cols, states):
    grid = np.random.rand(rows, cols) * states
    return grid.round()

def coordinates_array(rows, cols):
    list = []
    for row in range(0, rows):
        for column in range(0, cols):
            list.append((row, column))
    return list

def manhattan_distance_matrix(coordinates_array, target):
    distance = cdist(coordinates_array, target, 'cityblock')
    distance = np.asarray(distance)
    distance = np.reshape(distance, (10, 10))
    return distance