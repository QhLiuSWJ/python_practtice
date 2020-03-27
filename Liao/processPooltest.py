# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:processPooltest.py
@time:2020/03/24
"""
import multiprocessing
import os, time, random


def long_time_task(name):
    print('run task %s(%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.4f seconds' % (name, (end - start)))


if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print('waiting for all subprocess done...')
    p.close()  # 关闭该进程池，但是池内已经启动的子进程还是会继续进行
    # p.apply_async(long_time_task, args=(10,))不可再进入，否则ValueError
    p.join()
    print('All subprocesses done')
