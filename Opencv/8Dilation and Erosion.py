# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:8Dilation and Erosion.py
@time:2020/03/31
"""
# 卷积后的图像的最小值作为图像的值
import cv2
import numpy as np


def DilationFunc():
    src = cv2.imread('Dilation.JPG', cv2.IMREAD_UNCHANGED)
    kernal1 = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(src,kernal1,iterations=2)
    dilatepic = cv2.dilate(erosion,kernal1,iterations=1)
    cv2.imshow('ero',erosion)
    cv2.imshow('src', src)
    cv2.imshow('dilate',dilatepic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    DilationFunc()
