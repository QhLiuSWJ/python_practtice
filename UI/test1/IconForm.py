# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:FirstMainWin.py
@time:2020/03/18
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QToolTip, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()

        self.button = QPushButton("我的按钮")
        self.initUI()

    def initUI(self):
        self.setWindowTitle('居中')
        self.setGeometry(2000, 2000, 250, 250)
        self.move(0, 0)
        # self.resize(800, 700)
        self.setWindowIcon(QIcon('11.ico'))

        self.button.setToolTip('这是按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def centerFun(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWin = IconForm()
    mainWin.centerFun()
    mainWin.show()
    sys.exit(app.exec_())
