# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:豆瓣爬虫.py
@time:2020/03/15
"""
import sys
import time
from bs4 import BeautifulSoup
import re
from urllib import request, error
import openpyxl


def askURL(url):
    request1 = request.Request(url)
    try:
        response = request.urlopen(request1)
        html = response.read()
    except error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def getData(baseurl):
    findLink = re.compile(r'<a href = "(.*?)">')


if __name__ == '__main__':
    print("开始爬取......")
    baseurl = 'https://movie.douban.com/top250?start='
