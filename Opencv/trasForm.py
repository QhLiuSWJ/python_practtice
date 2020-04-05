# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:trasForm.py
@time:2020/04/05
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("test.jpg")

rows, cols = src.shape[:2]
print(rows)
print(cols)
pos1 = np.float32([[50, 50], [200, 50], [50, 200]])
pos2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pos1, pos2)
result = cv2.warpAffine(src, M, (int(cols/2), int(rows/2)))

cv2.imshow("org", src)
cv2.imshow("res", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass
