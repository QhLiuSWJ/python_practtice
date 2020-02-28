# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P2.py
@time:2020/02/28
"""


def cal():
    profit = int(input("净利润："))
    if profit <= 0:
        print("请输入准确的净利润")
        profit = int(input("净利润："))

    arrange = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    return_m = 0
    for k in range(0, 6):
        if profit > arrange[k]:
            return_m += (profit - arrange[k]) * rat[k]
            print((profit - arrange[k]) * rat[k])
            profit = arrange[k]
    print('总奖金：%s' % return_m)


if __name__ == '__main__':
    cal()
