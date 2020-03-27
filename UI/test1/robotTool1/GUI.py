# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:GUI.py
@time:2020/03/22
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 50))
        self.groupBox.setObjectName("groupBox")
        self.listenButton = QtWidgets.QPushButton(self.groupBox)
        self.listenButton.setGeometry(QtCore.QRect(260, 15, 61, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listenButton.sizePolicy().hasHeightForWidth())
        self.listenButton.setSizePolicy(sizePolicy)
        self.listenButton.setObjectName("listenButton")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 13, 241, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ipLabel = QtWidgets.QLabel(self.layoutWidget)
        self.ipLabel.setObjectName("ipLabel")
        self.horizontalLayout.addWidget(self.ipLabel)
        self.ipLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.horizontalLayout.addWidget(self.ipLineEdit)
        self.portLabel = QtWidgets.QLabel(self.layoutWidget)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout.addWidget(self.portLabel)
        self.portLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout.addWidget(self.portLineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 10, 181, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.connectLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.connectLineEdit.setGeometry(QtCore.QRect(10, 13, 111, 19))
        self.connectLineEdit.setReadOnly(True)
        self.connectLineEdit.setObjectName("connectLineEdit")
        self.disconnectButton = QtWidgets.QPushButton(self.groupBox_2)
        self.disconnectButton.setGeometry(QtCore.QRect(130, 12, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setObjectName("disconnectButton")
        self.sendLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sendLineEdit.setGeometry(QtCore.QRect(60, 70, 281, 31))
        self.sendLineEdit.setObjectName("sendLineEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(360, 70, 75, 31))
        self.sendButton.setObjectName("sendButton")
        self.recvLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.recvLineEdit.setGeometry(QtCore.QRect(60, 120, 281, 31))
        self.recvLineEdit.setObjectName("recvLineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 31, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.sendLineEdit.raise_()
        self.sendButton.raise_()
        self.recvLineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Tool"))
        self.groupBox.setTitle(_translate("MainWindow", "网络配置"))
        self.listenButton.setText(_translate("MainWindow", "开始监听"))
        self.ipLabel.setText(_translate("MainWindow", "IP地址:"))
        self.portLabel.setText(_translate("MainWindow", "端口:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "当前连接"))
        self.disconnectButton.setText(_translate("MainWindow", "断开"))
        self.sendButton.setText(_translate("MainWindow", "发送"))
        self.label.setText(_translate("MainWindow", "发送:"))
        self.label_2.setText(_translate("MainWindow", "接收:"))


if __name__ == '__main__':
    pass
