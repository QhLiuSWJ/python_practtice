# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:pydoc.py
@time:2020/03/19
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()
        formLayout = QFormLayout()
        formLayout.addWidget(qbtn)
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
