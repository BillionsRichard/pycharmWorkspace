# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: server.py 
@time: 2018/6/3 14:28 
"""
from pprint import pprint as P
import socket


server = socket.socket()
server.bind(('127.0.0.1', 8089))
server.listen(10)

while True:
    client, addr = server.accept()
    buf = client.recv(1024)

    client.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n', 'utf8'))
    data = open('test.html', 'rb').read()
    P(data)
    client.sendall(data)