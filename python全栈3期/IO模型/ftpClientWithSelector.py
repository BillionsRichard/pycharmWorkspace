# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: ftpClientWithSelector.py 
@time: 2018/6/2 23:28 
"""
from pprint import pprint as P
import socket
import os,sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SelectFtpClient:
    def __init__(self):
        self.args = sys.argv
        if len(self.args) > 1:
            self.addr = self.args[1], int(self.args[2])
        else:
            self.addr = "127.0.0.1", 8885

        self.create_socket()
        self.command_fanout()

    def create_socket(self):
        try:
            self.socket = socket.socket()
            self.socket.connect(self.addr)
            P('连接服务器成功...')
        except Exception as e:
            P('create socket exception %s' % e)

    def command_fanout(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'exit':
                break

            cmd, file = cmd.split()

            if hasattr(self, cmd): # 使用反射.
                cmd_func = getattr(self, cmd)
                cmd_func(cmd, file)
            else:
                P('Command %s not found.' % cmd)


    def put(self, cmd, file):
        if os.path.isfile(file):
            file_name = os.path.basename(file)
            file_size = os.path.getsize(file)


    def get(self, cmd, file):
        pass


if __name__ == '__main__':
    pass

