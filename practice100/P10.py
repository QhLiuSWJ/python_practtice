# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P10.py
@time:2020/03/01
"""
import time, datetime

"""
题目：暂停一秒输出，并格式化当前时间。

程序分析：无。
"""


def cal():
    last = datetime.datetime.now()
    print(last.strftime("%Y.%m.%d %H-%M-%S"))
    time.sleep(1)
    ss = datetime.datetime.now()
    print(ss.strftime("%Y.%m.%d %H-%M-%S"))
    

if __name__ == '__main__':
    cal()