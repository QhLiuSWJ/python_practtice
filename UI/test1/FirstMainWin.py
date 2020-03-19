# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:FirstMainWin.py
@time:2020/03/18
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        self.setWindowTitle('FirstMainWin')
        self.resize(400, 300)
        # 获取MainWin的状态，存在属性status
        self.status = self.statusBar()
        self.status.showMessage('存在5s', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('11.ico'))
    mainWin = FirstMainWin()
    mainWin.show()
    sys.exit(app.exec_())
