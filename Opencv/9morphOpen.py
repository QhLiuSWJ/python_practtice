# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:9morphOpen.py
@time:2020/04/01
"""
import cv2
import numpy as np


src = cv2.imread('Dilation.JPG',cv2.IMREAD_UNCHANGED)

kernel = np.ones((5,5),np.uint8)
result = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel,iterations=2)

cv2.imshow('src',src)
cv2.imshow('result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass