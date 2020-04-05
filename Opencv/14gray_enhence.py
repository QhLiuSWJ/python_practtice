# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:14gray_enhence.py
@time:2020/04/05
"""
#  线性变换

"""
图像的灰度线性变换是通过建立灰度映射来调整原始图像的灰度，从而改善图像的质量，凸显图像的细节，提高图像的对比度。灰度线性变换的计算公式如下所示：


该公式中DB表示灰度线性变换后的灰度值，DA表示变换前输入图像的灰度值，α和b为线性变换方程f(D)的参数，分别表示斜率和截距。

当α=1，b=0时，保持原始图像
当α=1，b!=0时，图像所有的灰度值上移或下移
当α=-1，b=255时，原始图像的灰度值反转
当α>1时，输出图像的对比度增强
当0<α<1时，输出图像的对比度减小
当α<0时，原始图像暗区域变亮，亮区域变暗，图像求补

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
img = cv2.imread('test.jpg')

# 图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]

# 创建一幅图像
result = np.zeros((height, width), np.uint8)

# 图像灰度上移变换 DB=DA+50
for i in range(height):
    for j in range(width):

        if int(-1 * grayImage[i, j] + 255) > 255:
            gray = 255
        else:
            gray = int(-1 * grayImage[i, j] + 255)

        result[i, j] = np.uint8(gray)

# 显示图像
cv2.imshow("Gray Image", grayImage)
cv2.imshow("Result", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass
