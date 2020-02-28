# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:P4.py
@time:2020/02/28
"""
"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""


def cal_days():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)  # 对于不变化的东西可以写成元组
    if year % 4 != 0 and year % 100 != 0:
        sundays = int(months[month - 1]) + day
    else:
        if month >= 3:
            sundays = int(months[month - 1]) + day
            sundays = sundays + 1
    print(sundays)


if __name__ == '__main__':
    cal_days()
