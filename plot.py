from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

file = ''
data = pd.read_csv(sep=',', skiprows=20).values.tolist()
x, y = data[0], data[1]

plt.grid(True)
plt.plot(x, y, label='input')
plt.legend(True)