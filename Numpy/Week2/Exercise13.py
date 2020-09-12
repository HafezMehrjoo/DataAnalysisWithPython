import numpy as np


# Exercise 13 (diamond)
def diamond(size):
    row = size * 2 - 1
    column = size * 2 - 1
    zero_array = np.zeros(row * column, dtype=int).reshape(row, column)
    parts = np.split(zero_array, row)
    mean = int(row / 2)
    diamond_array = []
    j = 1
    for i, ar in enumerate(parts):
        if i > mean:
            ar[0, j] = 1
            ar[0, (row - 1) - j] = 1
            j += 1
        else:
            ar[0, mean + i] = 1
            ar[0, mean - i] = 1
        diamond_array.append(ar[0])
    return np.array(diamond_array)



