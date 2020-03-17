# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:broadcast.py
@time:2020/03/01
"""
import numpy as np


def test():
    a = np.array([1, 2, 3, 4])
    b = np.array([4, 5, 6, 7])
    if a.shape == b.shape:
        print(a*b)


def test1():
    a = np.array([[0, 0, 0],
                  (3, 3, 3)])
    b = np.array([1, 2, 3])
    print(a + b)


if __name__ == '__main__':
    test()
    test1()