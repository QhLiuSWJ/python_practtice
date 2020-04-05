# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:4imgfilter.py
@time:2020/03/29
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


def addnoise(imglocal):
    img = cv2.imread(imglocal, cv2.IMREAD_UNCHANGED)
    rows, cols, chn = img.shape
    imgsize = img.size
    print(imgsize)
    for i in range(int(imgsize / 100)):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y, :] = 255
    cv2.imshow("noise", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


# 均值滤波
def averagefilter():
    img = addnoise('test.jpg')
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 转换为RGB，应该是plt的默认读取方式是BGR
    result = cv2.blur(source, (5, 5))
    """
    result = cv2.blur(原始图像,核大小)
    其中，核大小是以（宽度，高度）表示的元祖形式。常见的形式包括：核大小（3，3）和（5，5）。"""
    title = ['source img', 'blur img']
    image = [source, result]
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(image[i])  # 设置背景颜色
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


# 方波滤波
def Boxfiltertest():
    """
    方框滤波和均值滤波核基本一致，区别是需不需要均一化处理。OpenCV调用boxFilter()函数实现方框滤波。函数如下：
    result = cv2.boxFilter(原始图像, 目标图像深度(-1与原始图像一致), 核大小, normalize属性)
    一般选择normalize=true，否则容易溢出
    其中，目标图像深度是int类型，通常用“-1”表示与原始图像一直；核大小主要包括（3，3）和（5，5），如下所示。:return:
    """
    img = addnoise('test.jpg')
    source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = cv2.boxFilter(source, -1, (1, 1), normalize=0)  # 为0容易导致溢出  图像多为白色，为1归一化
    title = ['source img', 'box img']
    image = [source, result]
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(image[i])  # 设置背景颜色
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    print(result[0:3, 0:3, 0])
    print(source[0:3, 0:3, 0])


# 高斯滤波
def Gaussfiltertest():
    """
   为了克服简单局部平均法的弊端(图像模糊)，目前已提出许多保持边缘、细节的局部平滑算法。它们的出发点都集中在如何选择邻域的大小、形状和方向、参数加平均及邻域各店的权重系数等。
图像高斯平滑也是邻域平均的思想对图像进行平滑的一种方法，在图像高斯平滑中，对图像进行平均时，不同位置的像素被赋予了不同的权重。高斯平滑与简单平滑不同，它在对邻域内像素进行平均时，给予不同位置的像素不同的权值，下图的所示的 3 * 3 和 5 * 5 领域的高斯模板

    """
    img = addnoise('test.jpg')
    source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = cv2.GaussianBlur(source, (3, 3), 0)  # 为0容易导致溢出  图像多为白色，为1归一化
    """
    dst = cv2.GaussianBlur(src, ksize, sigmaX)
其中，src表示原始图像，ksize表示核大小，sigmaX表示X方向方差。注意，核大小（N, N）必须是奇数，X方向方差主要控制权重。

    """
    title = ['source img', 'box img']
    image = [source, result]
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(image[i])  # 设置背景颜色
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    print(result[0:3, 0:3, 0])
    print(source[0:3, 0:3, 0])


# 中值滤波
def medianBlurtest():
    img = addnoise('test.jpg')
    result = cv2.medianBlur(img, 3)  # 核函数
    cv2.imshow("source", img)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # addnoise("test.jpg")
    # averagefilter()
    # Boxfiltertest()
    # Gaussfiltertest()
    medianBlurtest()

