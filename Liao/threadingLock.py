# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:threadingLock.py
@time:2020/03/24
"""
import threading
import os
import time

balance = 0
lock = threading.Lock()


def change_it(n):
    n -= 1
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        lock.acquire()  # 到release的阶段中间的过程不可以缺少锁
        try:
            change_it(n)
        finally:
            lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
