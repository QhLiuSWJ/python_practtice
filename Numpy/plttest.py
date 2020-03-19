# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:plttest.py
@time:2020/03/17
"""
import numpy as np
from matplotlib import pyplot as plt

np.random.seed(11)
N = 100
x = np.random.rand(N)
print(x)
y = 10 * x ** 2 + np.random.rand(N)
colors = np.random.rand(N)
area = (20 * x) ** 2
plt.scatter(x, y, s=area, alpha=0.5)
plt.show()


# if __name__ == '__main__':
#    pass
