# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: client.py 
@time: 2018/6/2 16:46 tgsgta
"""
from pprint import pprint as P
import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8080))

while True:
    data = input('client>>').strip()
    client_socket.send(data.encode('utf8'))

    recved_data = client_socket.recv(1024)

    print('Server<<<%s' % recved_data.decode('utf-8'))
