# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:testpen.py
@time:2020/04/05
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('testpen.png')
rows, cols = src.shape[:2]
img = cv2.GaussianBlur(src, (3, 3), 0)
cv2.imshow('0', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 255])
cv2.imshow("1", gray)
edges = cv2.Canny(gray, 50, 250, apertureSize=3)
plt.plot(hist, color='red')
plt.show()
cv2.imshow("2", edges)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=90, maxLineGap=10)

# 下面输出的四个点分别为四个顶点
for x1, y1, x2, y2 in lines[0]:
    print((x1, y1), (x2, y2))
for x1, y1, x2, y2 in lines[1]:
    print((x1, y1), (x2, y2))

# 绘制边缘
for x1, y1, x2, y2 in lines[0]:
    cv2.line(gray, (x1, y1), (x2, y2), (0, 0, 255), 1)

# # 根据四个顶点设置图像透视变换矩阵
# pos1 = np.float32([[114, 82], [287, 156], [8, 322], [216, 333]])
# pos2 = np.float32([[0, 0], [188, 0], [0, 262], [188, 262]])

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass
