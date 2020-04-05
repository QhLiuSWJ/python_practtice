# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:11calcHHist.py
@time:2020/04/03
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('test.jpg')
"""
hist = cv2.calcHist(images, channels, mask, histSize, ranges, accumulate)

"""
histb = cv2.calcHist([src], [0], None, [256], [0, 255])
histg = cv2.calcHist([src], [1], None, [256], [0, 255])
histr = cv2.calcHist([src], [2], None, [256], [0, 255])

plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.show()

if __name__ == '__main__':
    pass
