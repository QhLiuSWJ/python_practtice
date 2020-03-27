# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:RTool.py
@time:2020/03/22
"""


import sys
import socket
import threading
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from PyQt5.QtWidgets import QApplication,QMainWindow
from UI.test1.robotTool1.GUI import Ui_MainWindow

class TestGUI(Ui_MainWindow):

    def __init__(self, MainWindow):
        """
        初始化界面 ，连接槽函数，以及设置校验器
        """
        self.setupUi(MainWindow)
        self.connect_slot()
        self.server_validator()

    def start_tcp_server(self):
        # 设置 “开始监听” 按钮不可用
        self.listenButton.setDisabled(True)
        # 实例化一个socket
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            ipText = self.ipLineEdit.text()
            portValue = int(self.portLineEdit.text())
            self.sock.bind((ipText,portValue))
        except Exception as e:
            print("请检查ip和端口号")
            print(e)
        else:
            self.sock.listen(1)
            # 创建一个进程，用于处理socket连接和接收数据
            server_th = threading.Thread(target=self.tcp_connect_concurrency)
            server_th.start()
            print("正在监听")

    # 进程函数
    def tcp_connect_concurrency(self):
        try:
            connect ,address = self.sock.accept()
        except Exception as e:
            print(e)
        self.base_connect = connect
        connect_address = address[0] + ":" + str(address[1])
        self.connectLineEdit.setText(connect_address)
        while True:
            recv_msg = self.base_connect.recv(1024)
            self.recvLineEdit.setText(recv_msg.decode('utf-8'))

    def tcp_close(self):
        """
        点击'disconnect'按钮，断开当前连接
        """
        if self.listenButton.isEnabled()==False:
            self.listenButton.setDisabled(False)
        try:
            self.base_connect.close()
            self.connectLineEdit.setText("")
        except AttributeError as e:
            pass
        except Exception as e:
            print(e)

    def send_text(self):
        """
        点击“发送”发送数据/文本
        """
        send_msg = self.sendLineEdit.text()
        self.base_connect.send(send_msg.encode('utf-8'))

    def server_validator(self):
        """
        设置 ip 和 port 文本输入框的限制
        """
        ipValidator = QRegExpValidator(QRegExp('^((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'))
        portValidator = QIntValidator(0,65535)
        self.ipLineEdit.setValidator(ipValidator)
        self.portLineEdit.setValidator(portValidator)
        self.ipLineEdit.setPlaceholderText("请输入ip地址")
        self.portLineEdit.setPlaceholderText("端口")

    def connect_slot(self):
        """连接各控件的槽函数"""
        self.listenButton.clicked.connect(self.start_tcp_server)
        self.disconnectButton.clicked.connect(self.tcp_close)
        self.sendButton.clicked.connect(self.send_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = TestGUI(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
