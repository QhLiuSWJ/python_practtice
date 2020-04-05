# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:3ROIget.py
@time:2020/03/29
"""
import cv2
import numpy as np


def getShape():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    print(img.shape)
    print(img.size)  # 获取所有像素个数
    print(img.dtype)  # 获取图像数据类型
    cv2.imshow("Demo", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getROI():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    # 实现定义好imgROI的大小
    imgROI = np.ones((90, 90, 3))
    imgROI = img[10:100, 10:100]  # 第一个参数：x，第二个参数：y
    print(imgROI.shape)
    img[100:190, 100:190] = imgROI  # 进行ROI的替换
    cv2.imshow("Demo", img)
    cv2.imshow("ROI", imgROI)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getRGB():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    cv2.imshow('B', b)
    cv2.imshow('G', g)
    cv2.imshow('R', r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getMerge():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    # b = img[:, :, 0]
    # g = img[:, :, 1]
    # r = img[:, :, 2]
    # cv2.imshow('B', b)
    # cv2.imshow('G', g)
    # cv2.imshow('R', r)
    b, g, r = cv2.split(img)
    m = cv2.merge([b, g, r])
    cv2.imshow('merge bgr', m)

    # opencv 默认手机 BGR进行读取
    b, g, r = cv2.split(img)  # 将三个通道进行拆分
    rgb = cv2.merge([r, g, b])
    cv2.imshow('merge rgb', rgb)  # canvar同名的话会覆盖之前的

    # mbg = cv2.merge([b, g])
    # cv2.imshow('merge bg', mbg)
    # mgr = cv2.merge([g, r])
    # cv2.imshow('merge gr', mgr)
    # mbr = cv2.merge([b, r])
    # cv2.imshow('merge br', mbr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def setRGB():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    rows, cols, chn = img.shape
    b = cv2.split(img)[0]
    print(b.shape) # b此时的大小是（256，256）
    g = np.zeros((rows, cols), dtype=img.dtype) # zeros，设定的是一个（256，256）的零矩阵
    r = np.zeros((rows, cols), dtype=img.dtype)
    m = cv2.merge([b, g, r]) # 是对三个（256，256）的零矩阵进行操作，最后得到的是一个RGB的彩色图像，读入默认顺序是BGR
    cv2.imshow('B', b)
    cv2.imshow('Merge', m)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #     # getShape()
    #     getROI()
    # getRGB()
    # getMerge()
    setRGB()
