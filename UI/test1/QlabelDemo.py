# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:QlabelDemo.py
@time:2020/03/19
"""
import sys
import server
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText("<font color=yellow> 这是一个文本标签。</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<font color=red> 欢迎使用python GUI</font>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("test.jpg"))
        # label4.setOpenExternalLinks(True)
        # True 打开网页，false调用槽函数
        label4.setText("<a href='www.baidu.com'>感谢关注</a>")
        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addWidget(label2)
        vBox.addWidget(label3)
        vBox.addWidget(label4)

        label4.linkHovered.connect(self.linkHover)
        label4.linkActivated.connect(self.linkClick)
        self.setLayout(vBox)
        self.setWindowTitle('Qlabel控件演示')

        pushbutton = QPushButton()
        pushbutton.setText('connect')
        pushbutton.clicked.connect(lambda: self.linkClick())
        vBox.addWidget(pushbutton)

    def linkHover(self):
        print('鼠标滑过，触发事件')

    def linkClick(self):
        print('鼠标单击')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testLabel = QLabelDemo()
    testLabel.show()
    sys.exit(app.exec_())
