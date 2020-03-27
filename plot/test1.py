# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:test1.py
@time:2020/03/23
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.plot(x,y,"ob")
plt.show()

if __name__ == '__main__':
    pass
