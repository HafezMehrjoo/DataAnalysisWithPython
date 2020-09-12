import numpy as np


# Exercise 16 (multiplication table revisited)
def multiplication_table(n):
    return np.array(np.arange(n).reshape(-1, 1) * np.arange(n).reshape(1, -1))


print(multiplication_table(9))
