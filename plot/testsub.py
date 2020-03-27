# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:testsub.py
@time:2020/03/23
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2, 1, 1)
plt.xlim(0, 10)
plt.plot(x, y_sin)
plt.title('Sine')
plt.subplot(2, 1, 2)

plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()

if __name__ == '__main__':
    pass
