# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:threadingtest.py
@time:2020/03/24
"""
import time, threading


def loop():
    print('thread %s is running..' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('threading %s >>>%s' % (threading.current_thread().name, n))
        time.sleep(2)
    print('threading%s is ended ' % threading.current_thread().name)


if __name__ == '__main__':
    print('threading%s is running ' % threading.current_thread().name)# 任何进程默认会启动一个线程，名称为主线程，主线程又可以启动新的线程
    t = threading.Thread(target=loop, name='loopThread')
    t.start()
    t.join()
    print('threading%s is ended ' % threading.current_thread().name)# 返回当前线程
