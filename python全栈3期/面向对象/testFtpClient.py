# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: testFtpClient.py 
@time: 2018/5/13 15:25 
"""
from ftpClient import FtpClient

f1 = FtpClient('127.0.0.1')

if hasattr(f1, 'put'):
    func_put = getattr(f1, 'put')
    func_put()
else:
    print('do other handle...')

