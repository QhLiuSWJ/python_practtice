# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P1.py
@time:2020/02/28
"""


def cal():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (j != k) and (i != k):
                    print(i, j, k)


def cal2():
    list_num = [1, 2, 3, 4]
    list_print = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if
                  (j != i and j != k and i != k)]
    print(list_print)
    print(len(list_print))


if __name__ == '__main__':
    cal2()
