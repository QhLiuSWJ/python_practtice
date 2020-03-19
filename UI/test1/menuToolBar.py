# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:menuToolBar.py
@time:2020/03/19
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")

        self.setWindowTitle('StatusBar')
        exitAct = QAction(QIcon('test.jpg'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        exitAct1 = QAction(QIcon('test.jpg'), '&File', self)
        exitAct1.setShortcut('Ctrl+Q')
        exitAct1.setStatusTip('Exit application')
        exitAct1.triggered.connect(qApp.quit)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(exitAct1)

        self.setGeometry(300, 300, 250, 150)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
