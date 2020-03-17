#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'Michael Liao'

import sys


def test():
    sys.argv.append('M')
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    # 这种方式用于测试本模块的可用性
    # 注：name两边各有2个下划线__name__有2个取值：当模块是被调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为：__main__
    test()
