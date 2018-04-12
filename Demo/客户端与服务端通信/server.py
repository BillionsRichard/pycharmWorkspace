#coding:utf-8
import socket
import threading

def run(clientSocket):
    data = clientSocket.recv(1024)
    print('客户端说：%s' % data.decode('utf-8'))

    sendData = 'hello %s' % data.decode('utf-8')

    clientSocket.send(sendData.encode('utf-8'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8888))
server.listen(5)

print('服务器启动成功，等待连接。。。')
while True:
    clientSocket, clientAddress = server.accept()
    print("%s--%s连接成功" %(clientSocket, clientAddress))

    t = threading.Thread(target=run, args=(clientSocket,))
    t.start()

