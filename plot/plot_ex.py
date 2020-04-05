# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:plot_ex.py
@time:2020/03/23
"""

import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.axes([0.05, 0.05, 0.9, 0.9])  # 图片占图比例

plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)
# 再x的位置填充1-Y+1
# (Y-1) > -1 添加条件判断

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.25)

plt.xlim(-np.pi, np.pi)
plt.xticks([1,2])  # 标 注
plt.ylim(-2.5, 2.5)
# plt.yticks([])
# savefig('../figures/plot_ex.png',dpi=48)
plt.show()

if __name__ == '__main__':
    pass
