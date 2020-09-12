import numpy as np
import pandas as pd


# Exercise 13 (read series)

def read_series(input_):
    return pd.Series(data=input_, index=range(0, len(input_)))


input_lines = []
while True:
    line = input('please tell me:')
    if line:
        input_lines.append(line)
    else:
        break
print(read_series(input_lines))
