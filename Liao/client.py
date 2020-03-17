import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8000))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in ['4','5','6']:
    # 发送数据:
    s.send(str(data).encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()