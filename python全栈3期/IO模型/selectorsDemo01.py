# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: selectorsDemo01.py 
@time: 2018/6/2 18:53 
"""
from pprint import pprint as P
import selectors
import socket

SELECTOR = selectors.DefaultSelector()

def accept_fun(socket, mask):
    client_skt, client_addr = socket.accept()
    client_port = client_addr[1]
    P('client coming:%s' % client_port)
    SELECTOR.register(client_skt, selectors.EVENT_READ, read_fun)


def read_fun(socket, mask):
    data = socket.recv(1000).decode('utf8')

    if data:
        print('received：%s' % data)
        socket.send(data.upper().encode('utf8'))
    else:
        P('no data received....')



server_sock = socket.socket()
server_sock.bind(("127.0.0.1", 8080))
server_sock.listen(100)
server_sock.setblocking(False)

SELECTOR.register(server_sock, selectors.EVENT_READ, accept_fun)

while True:
    events = SELECTOR.select() #循环监听事件。
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask) #调用事先注册的回掉函数。
