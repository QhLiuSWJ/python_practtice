# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:threadinglocal.py
@time:2020/03/24
"""
import threading

local_school = threading.local()# 全局创建threadLocal变量，但是局部可以随意使用


def process_student():
    std = local_school.student
    print('hello %s(in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('alice',), name='thread-1')

    t2 = threading.Thread(target=process_thread, args=('ccc',), name='thread-2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
