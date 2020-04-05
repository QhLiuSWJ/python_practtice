# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:testshuffle.py
@time:2020/04/02
"""

import paddle.fluid as fluid


def reader():
    for i in range(5):
        yield i


shuffled_reader = fluid.io.shuffle(reader, buf_size=7)
for e in shuffled_reader():
    print(e)

if __name__ == '__main__':
    pass
