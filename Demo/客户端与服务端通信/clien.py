#coding:utf-8
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

while True:
    data = input('输入给服务器发送的数据：')
    client.send(data.encode('utf-8'))
    info = client.recv(1024)
    print('服务器说：%s' % info.decode('utf-8'))
