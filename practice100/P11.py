# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P11.py
@time:2020/03/01
"""


def rabbit(num):
    f1 = 1
    # 第一个月为1
    f2 = 1
    # 第二个月为1
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num - 1):
            f1, f2 = f2, f1 + f2
    return f1


if __name__ == '__main__':
    print(rabbit(36))