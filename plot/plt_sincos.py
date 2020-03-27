# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:plt_sincos.py
@time:2020/03/23
"""
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5), dpi=80)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')# tick 标记
ax.spines['bottom'].set_position(('data', 0))# spines 移动原本底部的 坐标到0位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min() * 1.1, C.max() * 1.1)
# plt.yticks([-1, 0, +1])
plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

plt.show()

if __name__ == '__main__':
    pass
