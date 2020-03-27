import socket
import threading
import time
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QMessageBox, QWidget,QFileDialog
import sys
from UI.test1.robotTest.robotTool import robotToolUI


class sockServer(robotToolUI):
    def __init__(self):
        super(sockServer, self).__init__()
        self.initUI()
        self.connect_slot()
        # self.connectButton.setText('a')
        # self.setWindowTitle('1q')
        # self.connect_slot()
        # self.server_validator()

    def start_tcp_server(self):
        self.connectButton.setDisabled(True)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Waiting for connection1')
        try:
            robotIP = self.IPLineEdit.text()
            robotPort = self.PortLineEdit.text()
            print('Waiting for connection1')
            self.sock.bind((str(robotIP), int(robotPort)))
            print('Waiting for connection2')
        except Exception as e:
            # print()
            # reply = QMessageBox.Information(self, 'Remind!', 'Please set the ip and port correctly')
            print(e)
        else:
            print('Wait')
            self.sock.listen(1)
            print('Waiting for connection')
            # 开启一个线程用于监听来的一个tcp链接
            t = threading.Thread(target=self.tcpLink)
            t.start()
            print("正在监听")

    def tcpLink(self):
        try:
            sock, address = self.sock.accept()
        except Exception as e:
            print(e)
        self.base_connect = sock
        print('Accept a new connection from %s:%s...' % address)
        self.CurLineEdit.setText(str(address))
        # sock.send(b'welcome')
        dataname = 'data' + time.strftime("%Y_%m_%d %H_%M_%S")
        with open(dataname + '.txt', 'w') as fr:
            while True:
                data = self.base_connect.recv(2000).decode('gbk')
                fr.write(data + '\r')
                # time.sleep(3)
                if not data or data == 'exit':
                    break
                print(data)
                # sock.send(('hello,%s' % data.decode('utf-8')).encode('utf-8'))
            self.base_connect.close()
        print('Connection from %s:%s closed' % address)

    def tcp_close(self):
        """
        点击'disconnect'按钮，断开当前连接
        """
        if not self.connectButton.isEnabled():
            self.connectButton.setDisabled(False)
        # self.sock.close()
        try:
            self.base_connect.close()
            self.CurLineEdit.setText("")
        except AttributeError as e:
            pass
        except Exception as e:
            print(e)

    def connect_slot(self):
        # self.connectButton.clicked.connect(self.start_tcp_server)
        self.connectButton.clicked.connect(self.start_tcp_server)
        self.disconnectButton.clicked.connect(self.tcp_close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ss = sockServer()
    ss.show()
    sys.exit(app.exec_())
