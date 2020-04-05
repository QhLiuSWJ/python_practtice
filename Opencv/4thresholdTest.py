# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:4thresholdTest.py
@time:2020/03/29
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def testthreshold():
    src = cv2.imread('test.jpg')
    Grayimage = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    r, b = cv2.threshold(Grayimage, 127, 255, cv2.THRESH_BINARY)
    print(r)
    cv2.imshow('src', src)
    cv2.imshow('result', b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test5():
    src = cv2.imread('test.jpg')
    # src1 = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    GrayImage = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imshow('test',GrayImage)
    print(GrayImage[100,100])
    ret, thresh1 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh',thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ret, thresh2 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO_INV)
    thresh6 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh7 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    title = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV','MEAN_C','GAUSSIAN_C']
    images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5,thresh6, thresh7]
    for i in range(8):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images[i],'gray') # 只有加了gray才能是灰度图像？？？
        plt.title(title[i])
    plt.show()

    # cv2.imshow('src', src)
    # cv2.imshow('result', b)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    test5()
    # testthreshold()
