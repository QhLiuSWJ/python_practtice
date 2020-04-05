# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:1readimage.py
@time:2020/03/29
"""

import cv2


def readimg():
    img = cv2.imread('test.jpg')
    cv2.imshow("test", img)

    k = cv2.waitKey(1111)  # 0 无限期等待键盘输入，>0delay毫秒
    if k == 111:
        cv2.destroyAllWindows()
        cv2.destroyWindows()  # 删除指定窗口

    cv2.imwrite("testxxx.jpg", img)  # 写入到本地，


def changeimg():
    img = cv2.imread('testxxx.jpg', cv2.IMREAD_UNCHANGED)
    """
        img = cv2.imread(文件名,[,参数])
    参数(1) cv2.IMREAD_UNCHANGED (图像不可变)
    参数(2) cv2.IMREAD_GRAYSCALE (灰度图像)
    参数(3) cv2.IMREAD_COLOR (读入彩色图像)
    参数(4) cv2.COLOR_BGR2RGB (图像通道BGR转成RGB)

    """
    test = img[88, 142]
    print(test)  # 打印某点的RGB 输出是一个list RGB
    blue = img[88, 142, 0]
    print(blue)
    green = img[88, 142, 1]
    print(green)
    red = img[88, 142, 2]
    print(red)
    cv2.imshow("test", img)
    k = cv2.waitKey(0)
    if k == 111:
        cv2.destroyAllWindows(test)
    # cv2.destroyAllWindows(test)

    cv2.imwrite('testzzz.jpg', img)


def changeimgtest():
    img = cv2.imread('testxxx.jpg', cv2.IMREAD_UNCHANGED)
    """
        img = cv2.imread(文件名,[,参数])
    参数(1) cv2.IMREAD_UNCHANGED (图像不可变)
    参数(2) cv2.IMREAD_GRAYSCALE (灰度图像)
    参数(3) cv2.IMREAD_COLOR (读入彩色图像)
    参数(4) cv2.COLOR_BGR2RGB (图像通道BGR转成RGB)

    """
    img[10:100, 10:100] = [255, 255, 255]

    cv2.imshow("test", img)
    k = cv2.waitKey(0)
    if k == 111:
        cv2.destroyWindow('test')
    # cv2.destroyAllWindows(test)

    cv2.imwrite('testyyy.jpg', img)


if __name__ == '__main__':
    changeimgtest()
    # changeimg()
    # readimg()
