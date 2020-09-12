import numpy as np
import pandas as pd


# Exercise 15 (inverse series)
def inverse_series(s):
    indexes = np.array(s.index)
    values = np.array(s.values)
    indexes = np.flip(indexes)
    values = np.flip(values)
    inverse = pd.Series(data=values, index=indexes)
    return inverse
