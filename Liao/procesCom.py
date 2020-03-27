# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:procesCom.py
@time:2020/03/24
"""
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ["A", "B", "C"]:
        print('Put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read:%s ' % os.getpid())
    while True:
        value = q.get()
        print('get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # 强行终止死循环
