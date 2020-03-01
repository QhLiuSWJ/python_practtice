# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P8.py
@time:2020/03/01
"""
"""

题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
# 添加end=‘’ 取消换行 注意range也是左闭右开，range（1，1）直接没有值

def cal():
    for i in range(1, 10):
        print()
        for j in range(1, i+1):
            print("%d*%d=%d" % (i, j, i*j), end=' ') # 添加end=‘’ 取消换行


if __name__ == '__main__':
    cal()