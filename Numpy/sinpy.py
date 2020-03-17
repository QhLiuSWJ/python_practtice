# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:sinpy.py
@time:2020/03/17
"""
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * x)
plt.scatter(x, s)
plt.show()
plt.plot(x, s, label='y=x*x')
plt.xlabel('x')
plt.legend()
plt.show()

plt.plot(x, np.sin(x), 'r--', x, x * 2, 'b+')
plt.show()