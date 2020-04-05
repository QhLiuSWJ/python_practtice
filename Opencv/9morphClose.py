# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:9morphClose.py
@time:2020/04/01
"""

import cv2
import numpy as np


src = cv2.imread('J.JPG',cv2.IMREAD_UNCHANGED)

kernel = np.ones((5,5),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel,iterations=2)

cv2.imshow('src',src)
cv2.imshow('result',result)
dst = cv2.morphologyEx(result, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('dst',dst)
cv2.imwrite('JOPEN.jpg',result)

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass