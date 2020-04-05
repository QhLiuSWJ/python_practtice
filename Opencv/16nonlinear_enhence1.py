# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:16nonlinear_enhence.py
@time:2020/04/05
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def log_plot(c):
    x = np.arange(0, 256, 0.01)
    y = c * np.log(x + 1)+0.5
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u'对数坐标系')
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.show()


def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    # 注意这里只是无符号整型
    return output

def gamma_plot(c,v):
    x=np.arange(0,256,0.01)
    y=c*x**v
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u'对数坐标系')
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.show()

def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut) #像素灰度值的映射
    output_img = np.uint8(output_img+0.5)
    return output_img


src = cv2.imread('test.jpg')
cv2.imshow('src', src)
log_plot(42)
gamma_plot(0.00000005,4)
outgama=gamma(src,0.00000005,4)
cv2.imshow('outgama',outgama)
out = log(42, src)
c=np.uint8(8)
print(type(c))
print(out.shape)
print(src.shape)
cv2.imshow('out', out)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass
