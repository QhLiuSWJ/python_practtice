# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:robotTool.py
@time:2020/03/20
"""

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout, QTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout, QLabel, QDesktopWidget, \
    QMessageBox, QGroupBox, QFileDialog
from PyQt5.QtGui import QIcon, QRegExpValidator, QIntValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5 import QtCore
import random
import numpy as np
from scipy import interpolate


# from UI.test1.robotTest.sockServer import *


class robotToolUI(QWidget):
    def __init__(self):
        super(robotToolUI, self).__init__()
        # self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('../icon.PNG'))
        self.setWindowTitle('Robot Tool')
        self.setGeometry(400, 400, 600, 400)
        # 设置第一行
        self.IPLineEdit = QLineEdit()
        self.PortLineEdit = QLineEdit()
        self.CurLineEdit = QLineEdit()
        self.connectButton = QPushButton('连接')
        self.disconnectButton = QPushButton('断开')
        ipLable = QLabel('IP:', self)
        portLable = QLabel('&Port:', self)
        disconnectButtonLable = QLabel('Current:', self)
        ipLable.setBuddy(self.IPLineEdit)
        portLable.setBuddy(self.PortLineEdit)
        disconnectButtonLable.setBuddy(self.PortLineEdit)
        spacerLeft = QSpacerItem(20, 20, QSizePolicy.Expanding)
        # spacerLeft.setGeometry(20)
        # 设置行layout
        h_layout_1 = QHBoxLayout()
        h_layout_1.addSpacerItem(spacerLeft)
        h_layout_1.addWidget(ipLable)
        h_layout_1.addWidget(self.IPLineEdit)
        h_layout_1.addSpacerItem(spacerLeft)
        h_layout_1.addWidget(portLable)
        h_layout_1.addWidget(self.PortLineEdit)
        h_layout_1.addSpacerItem(spacerLeft)
        h_layout_1.addWidget(self.connectButton)
        h_layout_1.addSpacerItem(spacerLeft)
        h_layout_1.addWidget(disconnectButtonLable)
        h_layout_1.addWidget(self.CurLineEdit)
        h_layout_1.addWidget(self.disconnectButton)
        h_layout_1.addSpacerItem(spacerLeft)
        # 设置第二行
        # h_layout_2 = QHBoxLayout()
        # self.connectSignalOut = QTextEdit()
        # spacer2 = QSpacerItem(20, 40, QSizePolicy.Fixed)
        # # self.connectSignalOut.setSizeIncrement(400, 100)
        # h_layout_2.addSpacerItem(spacer2)
        # h_layout_2.addWidget(self.connectSignalOut)
        # h_layout_2.addSpacerItem(spacer2)
        self.selectButton = QPushButton('选择文件')
        self.displayButton = QPushButton('画图')
        self.filePathlineEdit = QLineEdit()
        self.filePathlineEdit.setPlaceholderText('当前文件框')
        spacer2 = QSpacerItem(20, 40, QSizePolicy.Fixed)
        # self.connectSignalOut.setSizeIncrement(400, 100)
        h_layout_3 = QHBoxLayout()
        h_layout_3.addSpacerItem(spacer2)
        h_layout_3.addWidget(self.selectButton)
        h_layout_3.addWidget(self.filePathlineEdit)
        h_layout_3.addSpacerItem(spacer2)
        h_layout_3.addWidget(self.displayButton)
        # set the slot of connect button
        # connectButton.clicked.connect(self.connectRobot)
        self.fig = plt.figure(figsize=(5, 4))
        self.canvas = FC(self.fig)
        self.axes = self.fig.add_subplot('111')
        self.axes.set_title('plot')
        VLayout = QVBoxLayout()
        VLayout.addLayout(h_layout_1)
        # VLayout.addStretch(1)
        # VLayout.addLayout(h_layout_2)
        # VLayout.addStretch(10)
        VLayout.addLayout(h_layout_3)
        # VLayout.addStretch(1)
        VLayout.addWidget(self.canvas)
        self.setLayout(VLayout)

        self.centerScreen()
        self.ip_port_validator()

        self.selectButton.clicked.connect(self.openFile)
        self.displayButton.clicked.connect(self.dispaly)

    def dispaly(self):
        posx = []
        posz = []
        fr = open(str(self.filePathlineEdit.text()), 'r')
        try:
            while True:
                pos = fr.readline().replace("\n", '')
                # exit or null break
                if pos == 'exit' or not pos:
                    break
                print(pos)
                splitPos = pos.split(' ')
                print(splitPos)
                # print(splitPos)
                posx.append(splitPos[1])

                posz.append(splitPos[3])
        finally:
            print('ok')
            fr.close()
        length = len(posx)
        print(length)
        print(posx)
        x = np.linspace(0, (length-1) * 0.1, length)
        # y = x
        xx = [1, 23, 3]
        yy = [1, 23, 3]
        ax = self.axes
        ax.cla()
        ax.plot(x, posx)
        ax.plot(x, posz)
        # ax.plot(xx,yy)
        self.canvas.draw()
        # self.axes.plot(x, posx)
        # self.draw()

        # self.axes.plot(x, posx)
        # print('xxx')
        # self.draw()
        # timer = QTimer(self)
        # timer.timeout.connect(self.update_figure)
        # timer.start(100)

        # self.axes.cla()
        # self.axes.plot(x, posx)
        # self.draw()
        # self.axes = fig.add_subplot(111)

        # FigureCanvas.__init__(self, fig)
        # self.setParent(parent)
        #
        # FigureCanvas.setSizePolicy(self,
        #                            QSizePolicy.Expanding,
        #                            QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)
        # self.axes.plot(x, posz)
        # self.draw()
        # self.setParent(parent)
        #
        # FigureCanvas.setSizePolicy(self,
        #                            QSizePolicy.Expanding,
        #                            QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)

    def openFile(self):
        get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            "./",
                                                            "All Files (*);;Text Files (*.txt);;Image Files (*.png);;")

        self.filename_path = get_filename_path
        print(get_filename_path)
        if ok:
            self.filePathlineEdit.setText(str(get_filename_path))

    def centerScreen(self):
        screensize = QDesktopWidget().screenGeometry()
        wigScreen = self.geometry()
        newLeft = (screensize.width() - wigScreen.width()) / 2
        newTop = (screensize.height() - wigScreen.height()) / 2
        self.move(newLeft, newTop)

    def ip_port_validator(self):
        # ipValidator = QRegExpValidator(
        #    QtCore.QRegExp("((2[0-4]\\d|25[0-5]|[01]?\\d\\d?)\\.){4}"))
        portValidator = QIntValidator(0, 65535)
        # self.IPLineEdit.setValidator(ipValidator)
        self.PortLineEdit.setValidator(portValidator)
        self.IPLineEdit.setPlaceholderText('ip地址')
        self.PortLineEdit.setPlaceholderText('端口')

    def update_figure(self):
        x = np.linspace(0, 10, 10)
        y = [random.randint(0, 10) for i in range(10)]
        xx = np.linspace(0, 10)
        f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
        yy = f(xx)
        print('test')
        self.axes.cla()
        self.axes.plot(x, y, 'o', xx, yy)
        self.draw()


class PlotCanvas(FC):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FC.__init__(self, fig)
        self.setParent(parent)

        FC.setSizePolicy(self,
                         QSizePolicy.Expanding,
                         QSizePolicy.Expanding)
        FC.updateGeometry(self)
        # self.init_plot()  # 打开App时可以初始化图片
        # self.plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = robotToolUI()
    mainWin.show()
    sys.exit(app.exec_())
