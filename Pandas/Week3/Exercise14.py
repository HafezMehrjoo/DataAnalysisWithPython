import numpy as np
import pandas as pd


# Exercise 14 (operations on series)

def create_series(a, b):
    s1 = pd.Series(data=a, index=['a', 'b', 'c'])
    s2 = pd.Series(data=b, index=['a', 'b', 'c'])
    return s1, s2


def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return s1, s2



