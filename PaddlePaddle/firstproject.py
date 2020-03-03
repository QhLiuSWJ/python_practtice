# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:firstproject.py
@time:2020/03/02
"""

import paddle.fluid as fluid
import numpy as np


def cal1():
    # 定义张量
    x1 = fluid.layers.fill_constant(shape=[2, 2], value=1, dtype='int64')
    x2 = fluid.layers.fill_constant(shape=[2, 2], value=1, dtype='int64')
    # 张量求和
    y1 = fluid.layers.sum(x=[x1, x2])

    # 创定使用GPU的解释器

    place = fluid.CPUPlace()
    exe = fluid.executor.Executor(place)

    exe.run(fluid.default_startup_program())
    result = exe.run(program=fluid.default_main_program(),
                     fetch_list=[y1])
    print(result)


def cal2():
    a = fluid.layers.create_tensor(dtype='int64', name='a')
    b = fluid.layers.create_tensor(dtype='int64', name='b')
    y = fluid.layers.sum(x=[a, b])
    place1 = fluid.CUDAPlace(0)
    exe = fluid.executor.Executor(place1)
    a1 = np.array([3, 2]).astype('int64')
    b1 = np.array([1, 2]).astype('int64')
    out_a, out_b, result = exe.run(program=fluid.default_main_program(), feed={'a': a1, 'b': b1}
                                   , fetch_list=[a, b, y])
    print(out_a, "+", out_b, "+", result)


if __name__ == '__main__':
    cal2()
