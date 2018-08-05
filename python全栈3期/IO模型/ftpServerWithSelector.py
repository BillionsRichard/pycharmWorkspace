# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: ftpServerWithSelector.py 
@time: 2018/6/2 23:18 
"""
from pprint import pprint as P
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import socket
import selectors


class SelectFtpServer:
    def __init__(self):
        self.dic = {}
        self.hasReceived = 0
        self.sel = selectors.DefaultSelector()
        self.create_socket()
        self.handle()

    def create_socket(self):
        self.server = socket.socket()
        self.server.bind(('127.0.0.1', 8088))
        self.server.listen(10)
        self.sel.register(self.server, selectors.EVENT_READ, self.accept)

    def handle(self):
        events = self.sel.select()

        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

    def accept(self, socket, mask):
        client, addr = socket.accept()
        client.setblocking(False)
        self.sel.register(client, selectors.EVENT_READ, self.read)

        self.dic[addr] = {}

    def read(self, client, mask):



if __name__ == '__main__':
    SelectFtpServer()
