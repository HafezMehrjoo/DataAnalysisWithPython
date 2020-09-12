import numpy as np


# Exercise 14 (vector lengths)
def vector_lengths(array):
    return np.array(np.sqrt(np.sum(array, axis=1)))


array = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 22],
                  [2, 2, 1, -2],
                  [2, 0, 0, 2],
                  [0, 0, 0, 0]])
print(array.shape)
print(vector_lengths(array))
