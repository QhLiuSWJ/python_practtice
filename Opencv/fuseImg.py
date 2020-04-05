# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:fuseImg.py
@time:2020/03/29
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


def Opencv_Numpy_fuse():
    """"
    1.Numpy库加法
    其运算方法是：目标图像 = 图像1 + 图像2，运算结果进行取模运算。

    当像素值<=255时，结果为“图像1+图像2”，例如：120+48=168
    当像素值>255时，结果为对255取模的结果，例如：(255+64)%255=64
    2.OpenCV加法运算
    另一种方法是直接调用OpenCV库实现图像加法运算，方法如下：
    目标图像 = cv2.add(图像1, 图像2)
    此时结果是饱和运算，即：

    当像素值<=255时，结果为“图像1+图像2”，例如：120+48=168
    当像素值>255时，结果为255，例如：(255+64) = 255

    """
    img = cv2.imread('test.jpg')
    test = img
    result1 = img + test  # numpy 直接叠加
    result2 = cv2.add(img, test)  # opencv叠加
    Image = [result1, result2]
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(Image[i])
        plt.title("test" + str(i))
    plt.show()

def addWeighttest():
    img = cv2.imread('test1.jpg')
    print(img.shape)
    img1 = cv2.imread('test.jpg')
    print(img1.shape)
    result = cv2.addWeighted(img[0:255, 0:255], 0.8, img1[0:255, 0:255], 0.8, 0)
    cv2.imshow('fuse', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def testimgconvert():
    img = cv2.imread('test.jpg')
    result1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('rgb',result1)
    cv2.imshow('gray',result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Opencv_Numpy_fuse()
    # addWeighttest()
    testimgconvert()
