# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: ftpClient.py
@time: 2018/5/13 15:23 
"""

class FtpClient:
    def __init__(self, addr):
        print('正在连接服务器:%s' % addr)
        self.addr = addr

    def put(self, file_name):
        print('正则上传文件:%s' % file_name)


