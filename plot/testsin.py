# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:testsin.py
@time:2020/03/23
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
ys = np.sin(x)
yc = np.cos(x)

plt.title("sine wave form")

# plt.plot(x, ys,'r')
# plt.plot(x, yc,'b')
plt.plot(x, ys, color="green", linewidth=10, linestyle="-", label='cosine') #以键值的形式添加内容
plt.plot(x, yc, color="red", linewidth=1, linestyle="--", label='sine')
plt.legend(loc="lower left")

""""
	best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center
"""
# 设置横轴的上下限
plt.xlim(0, 3 * np.pi)

# 设置横轴记号
plt.xticks(np.linspace(0, 10, 10, endpoint=True))

# 设置纵轴的上下限
plt.ylim(-1.0, 1.0)

# 设置纵轴记号
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.show()

if __name__ == '__main__':
    pass
