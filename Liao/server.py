import socket
import threading
import time


def tcpLink(sock, address):
    print('Accept a new connection from %s:%s...' % address)
    # sock.send(b'welcome')
    data = 'data' + time.strftime("%Y_%m_%d %H_%M_%S")
    with open('C:/Users/QHL/Desktop/流畅的Python/' + data + '.txt', 'w') as fr:
        while True:
            data = sock.recv(2000).decode('gbk')
            fr.write(data + '\r')
            # time.sleep(3)
            if not data or data == 'exit':
                break
            print(data)
            # sock.send(('hello,%s' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
    print('Connection from %s:%s closed' % address)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 59000))
s.listen(5)
print('Waiting for connection')
while True:
    sock, address = s.accept()
    # 开启一个线程用于监听来的一个tcp链接
    t = threading.Thread(target=tcpLink, args=(sock, address))
    t.start()
