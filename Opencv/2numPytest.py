# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:2numPytest.py
@time:2020/03/29
"""
import cv2
import numpy


def testNumpy():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    blue = img.item(78, 100, 0)
    green = img.item(78, 100, 1)
    red = img.item(78, 100, 2)
    print(blue)
    print(green)
    print(red)
    cv2.imshow('Demo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Numpyset():
    img = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    blue = img.item(78, 100, 0)
    green = img.item(78, 100, 1)
    red = img.item(78, 100, 2)
    print(blue)
    print(green)
    print(red)
    img.itemset((78, 100, 0), 100)
    img.itemset((78, 100, 1), 100)
    img.itemset((78, 100, 2), 100)
    print(img.item(78, 100, 0))
    print(img.item(78, 100, 1))
    print(img.item(78, 100, 2))
    # img.itemset((78, 100), (100, 100, 100))

    print(img[78, 100])
    cv2.imshow('Demo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # testNumpy()
    Numpyset()
