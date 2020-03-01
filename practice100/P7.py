# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P7.py
@time:2020/03/01
"""
"""
将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。
"""


def cal(a):
    b = a[:]  # all element
    print(b)


if __name__ == '__main__':
    cal([1, 2, 3])
