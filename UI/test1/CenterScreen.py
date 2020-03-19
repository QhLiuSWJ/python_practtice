# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:FirstMainWin.py
@time:2020/03/18
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterScreen(QMainWindow):
    def __init__(self):
        super(CenterScreen, self).__init__()

        self.setWindowTitle('居中')
        self.move(0, 0)
        self.resize(800, 700)
        # 获取MainWin的状态，存在属性status
        self.status = self.statusBar()
        self.status.showMessage('存在5s', 5000)

    def centerFun(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('11.ico'))
    mainWin = CenterScreen()
    mainWin.centerFun()
    mainWin.show()
    sys.exit(app.exec_())
