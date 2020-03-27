# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:ProcessTest.py
@time:2020/03/24
"""

import multiprocessing
import os


def run_proc(name):
    print('Run child process %s(%s)...' %(name, os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid()) # os.getpid()获取当前的线程id
    p = multiprocessing.Process(target=run_proc, args=('test',))  # 元组只有一个参数的话要加上逗号
    print("child will start")
    p.start()# 启动进程
    p.join()  # 主线程等待 进程间的同步
    print('child process end')
