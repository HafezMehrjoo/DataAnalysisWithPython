import numpy as np


# Exercise 15 (vector angles)
def vector_angles(x, y):
    inner_product = (x * y).sum(1)
    norms = np.linalg.norm(x, axis=1) * np.linalg.norm(y, axis=1)
    return np.arccos(np.clip(inner_product / norms, -1, 1))


a = np.array([[50, 50, 50, 50], [1, 2, 3, 4]])
b = np.array([[1, 1, 3, 5], [1, 2, 3, 4]])
print(vector_angles(a, b))
