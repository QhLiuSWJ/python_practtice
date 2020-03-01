# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P9.py
@time:2020/03/01
"""

import time

"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""


def cal():
    myD = {1: 'a', 2: 'b'}
    for k, v in myD.items():
        print(k, v)
        time.sleep(1)


if __name__ == '__main__':
    cal()