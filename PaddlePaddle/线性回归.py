# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:线性回归.py
@time:2020/03/02
"""

import paddle.fluid as fluid
import paddle
import numpy as np


# 线性回归demo
def cal():
    # 输入层-隐藏层-输出层
    # 定义输入层的数据
    x = fluid.layers.data(name='x', shape=[13], dtype='float32')
    # 定义了激活函数，激活函数就是一个非线性函数
    hidden = fluid.layers.fc(input=x, size=100, act='relu')
    net = fluid.layers.fc(input=hidden, size=1, act=None)
    # 定义损失函数
    y = fluid.layers.data(name='y', shape=[1], dtype='float32')
    cost = fluid.layers.square_error_cost(input=net, label=y)
    avg_cost = fluid.layers.mean(cost)
    # 克隆一个测试方法
    test_program = fluid.default_main_program().clone(for_test=True)
    # 定义优化方法
    optimizer = fluid.optimizer.SGDOptimizer(learning_rate=0.01)
    opts = optimizer.minimize(avg_cost)

    # 创建一个使用CPU的解释器
    place = fluid.CPUPlace()
    exe = fluid.Executor(place)
    # 进行参数初始化
    exe.run(fluid.default_startup_program())
    # 定义训练和测试数据
    x_data = np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]).astype('float32')
    y_data = np.array([[3.0], [5.0], [7.0], [9.0], [11.0]]).astype('float32')
    test_data = np.array([[6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]).astype('float32')

    # 开始训练100个pass
    for pass_id in range(10):
        train_cost = exe.run(program=fluid.default_main_program(),
                             feed={'x': x_data, 'y': y_data},
                             fetch_list=[avg_cost])
        print("Pass:%d, Cost:%0.5f" % (pass_id, train_cost[0]))
    # 开始预测
    result = exe.run(program=test_program,
                     feed={'x': test_data, 'y': np.array([[0.0]]).astype('float32')},
                     fetch_list=[net])
    print("当x为6.0时，y为：%0.5f" % result[0])


if __name__ == '__main__':
    cal()
