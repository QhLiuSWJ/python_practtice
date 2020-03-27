# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:plotquiver.py
@time:2020/03/23
"""
import numpy as np
import matplotlib.pyplot as plt

n = 8
X, Y = np.mgrid[0:n, 0:n]# XY分别是8*8的数组
T = np.arctan2(Y - n / 2.0, X - n / 2.0)
R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
U, V = R * np.cos(T), R * np.sin(T)# 得到箭头的长度，且顺着T角度的方向，T也为xy此时的arctan角度

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.quiver(X, Y, U, V, R, alpha=.5)# R为颜色
plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)# 添加边的颜色

plt.xlim(-1, n), plt.xticks([])
plt.ylim(-1, n), plt.yticks([])

# savefig('../figures/quiver_ex.png',dpi=48)
plt.show()
