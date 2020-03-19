# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:QlabelDemo.py
@time:2020/03/19
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import *


class QLabelDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('伙伴关系')
        # 加&是加热键，alt+首字母可以直接切换到对应伙伴
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        # 伙伴控件
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel.setBuddy(passwordLineEdit)
        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        # 后面的参数是指的占用 一行两列
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        # 后面的参数是指的占用 一行两列
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)
        btnOK.clicked.connect(self.onClick_Button)

    def linkHover(self):
        print('鼠标滑过，触发事件')

    def linkClick(self):
        print('鼠标单击')
# 注意这个后面最好设置为传参数
    #获取当前的窗口的位置
    def onClick_Button(self):
        print("1、窗体坐标系")
        print("widget.x()=%d" % testLabel.x())
        print("widget.geometry().x()=%d" % testLabel.geometry().x())
        print("widget.geometry().x()=%d" % testLabel.frameGeometry().x())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    testLabel = QLabelDemo()
    testLabel.show()
    sys.exit(app.exec_())
