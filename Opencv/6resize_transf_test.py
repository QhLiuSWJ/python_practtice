# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:6resize_transf_test.py
@time:2020/03/29
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


def resizeTest():
    """
    图像缩放主要调用resize()函数实现，具体如下：
result = cv2.resize(src, dsize[, result[. fx[, fy[, interpolation]]]])
其中src表示原始图像，dsize表示缩放大小，fx和fy也可以表示缩放大小倍数，他们两个（dsize或fx\fy）设置一个即可实现图像缩放。例如：

result = cv2.resize(src, (160,160))
result = cv2.resize(src, None, fx=0.5, fy=0.5)
    :return:
    """
    img = cv2.imread('test.jpg')
    result1 = cv2.resize(img, (200, 100))
    result2 = cv2.resize(img, None, fx=0.5, fy=0.5)  # 必须设定fx =
    print(result1.shape)
    print(result2.shape)
    cv2.imshow('src', img)
    cv2.imshow('res1', result1)
    cv2.imshow('res2', result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotationfun():
    img = cv2.imread('test.jpg')
    rows, cols, chn = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
    print(M)
    rotated = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('src', img)
    cv2.imshow('rotated', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rotated


def fliptest():
    img = cv2.imread('test.jpg')
    src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 使用plt需转换

    # 图像翻转
    # 0以X轴为对称轴翻转 >0以Y轴为对称轴翻转 <0X轴Y轴翻转
    img1 = cv2.flip(src, 0)  # x轴翻转
    img2 = cv2.flip(src, 1)  # y轴翻转
    img3 = cv2.flip(src, -1)  # xy翻转 中心旋转180°

    # 显示图形
    titles = ['Source', 'Image1', 'Image2', 'Image3']
    images = [src, img1, img2, img3]
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def transfTest():
    img = cv2.imread('test.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    M = np.float32([[1, 0, 100], [0, 1, 0]])
    print(M)
    transfr = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    M = np.float32([[1, 0, 0], [0, 1, 100]])
    transfup = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    M = np.float32([[1, 0, 0], [0, 1, -100]])
    transfdown = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    image = [img, transfr, transfup, transfdown]
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(image[i])
        plt.title(str(i+1))
    plt.show()


if __name__ == '__main__':
    # resizeTest()
    rotationfun()
    # fliptest()
    # transfTest()
