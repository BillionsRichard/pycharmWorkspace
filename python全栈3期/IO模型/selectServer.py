# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: selectServer.py 
@time: 2018/6/2 14:25 
"""
from pprint import pprint as P
import socket
import select

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)

rlist = [server_socket, ]

while True:
    r, w, s = select.select(rlist, [], [])  # 水平触发

    for des in r:
        if des is server_socket:
            conn_sock, addr = des.accept()
            rlist.append(conn_sock) #将客户端通信的套接字放入监听列表中。
        else:
            client_data = conn_sock.recv(1024).decode('utf8')

            print('client<<<%s' % client_data)

            conn_sock.send(client_data.upper().encode('utf8'))



    print('>>>>>>>>')
