# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:basic.py
@time:2020/02/29
"""

import numpy as np

"""numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)"""
"""
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
"""


def practice():
    a = np.array([1, 2, 3])
    print(a)
    b = np.array([[1, 2], [3, 4]])
    print("b=", b)
    c = np.array([1, 2, 3, 4, 5], ndmin=2)
    print(c)
    d = np.array([1, 2, 3, 4, 5], dtype=complex)
    print(d)


def practice1():
    dt = np.dtype(np.int32)
    print(dt)
    # int8 int16 int32可以使用字符串 ‘i1’‘i2’‘i3’‘i4’等表示
    dy = np.dtype('i1')
    print(dy)
    # < > + ‘i1，2，3，4’表示在地址得大小端开始存储
    dp = np.dtype('<i4')
    print(dp)
    #  创建结构化数据类型
    ds = np.dtype([('age', np.int8)])
    print(ds)
    dk = np.array([(10,), (20,), (30,)], dtype=ds)
    print(dk)
    a = np.array([(10,), (20,), (30,)], dtype=ds)
    print(a['age'])

    # 结构化数据类型
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50), ('xyz', 21, 70)], dtype=student)
    print(a)


def practice2():
    a = np.array(24)
    print(a.ndim)  # 维度
    b = np.array([1, 2, 3, 4])
    print(b)
    print(b.ndim)
    b = b.reshape(2, 2)
    print(b.ndim)
    b.shape = (4, 1)
    print(b)
    print("b:itemsize:", b.itemsize)  # 占内存大小
    c = np.array([1, 2, 3, 4], dtype=np.int8)
    print(c.itemsize)
    print(c.flags)  # 获取数组得具体属性


def practice3():
    # 数组得创建  空数组和ones
    x = np.empty([2, 3], dtype=int)  # 出现随机值
    print(x)
    y = np.zeros([3, 3], dtype=float, order='C')  # 初始化全是零得数组，且存储顺序为先行后列，‘F’反之
    print(y)
    z = np.ones([3, 2], dtype=int)
    print(z)
    k = (1, 1, 3, 4)
    print(k)
    m = np.asarray(k)
    print(m)
    n = np.asarray(k, dtype=float)
    print(n)

    s = b'hello world'
    ss = np.frombuffer(s, dtype='S1')  # S1应该是占用一个byte的字节，b 表示以byte形式输出
    print(ss)


def practice4():
    x = np.arange(5, dtype=float)
    print(x)
    y = tuple(range(10, 20, 2))
    print(y)
    z = np.arange(10, 20, 2)
    print(z)
    k = np.linspace(10, 20, 2)  # 2为等差数列 数列个数 等比数列logspace
    print(k)
    k = np.linspace(10, 20, 10, endpoint=False)  # 去除最终点
    print(k)
    k = np.linspace(10, 20, 10, endpoint=False).reshape([10, 1])  # 去除最终点
    print(k)
    m = np.logspace(1, 2, 10).reshape(10, 1)  # 等比数列的生成，默认base是10  10**1  到  10**2中产生10个数
    print(m)
    # 这样生成的方式很好
    # 这样生成的方式很好
    # 这样生成的方式很好
    m = np.logspace(0, 9, num=10, base=2)  # 等比数列的生成，默认base是10  10**1  到  10**2中产生10个数
    print(m)


def practice5():
    a = np.arange(10)
    print(a[2:5])
    a = a.reshape(2, 5)
    print(a)
    print(a[1:])  # 选择第二行
    print(a[1:5])  # 左开右闭
    print(a[..., 1:])  # 取列
    print(a[..., 1:3])  # 取列
    print(a[1:, ...])  # 取行


if __name__ == '__main__':
    practice()
    practice1()
    practice2()
    practice3()
    practice4()
    practice5()
