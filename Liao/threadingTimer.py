# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:threadingTimer.py
@time:2020/03/27
"""

# 定时器，指定n秒后执行某个操作
from threading import Timer
import time


def funccc():
    print("执行时间同步")


if __name__ == "__main__":

    while True:
        Timer(5, funccc).start()  # 注意这个线程是异步的，先执行这句，然后马上就执行time.sleep()，
        # timer在等待5秒后执行func,而time.sleep()此时也等待了5秒，再次执行timer()
        time.sleep(5)
