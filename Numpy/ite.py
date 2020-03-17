# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:ite.py
@time:2020/03/02
"""
import numpy as np


def test():
    a = np.arange(6).reshape(2, 3)
    print(a)
    print(a.T)
    for x in np.nditer(a):
        print(x, end=',')
    print('')
    for x in np.nditer(a.T):
        print(x, end=',')
    for x in np.nditer(a.T.copy(order='C')):
        print(x, end=',')


if __name__ == '__main__':
    test()