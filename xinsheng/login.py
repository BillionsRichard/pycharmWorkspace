# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: login.py 
@time: 2018/11/18 22:28 
"""
from pprint import pprint as P

import requests


class Login(object):
    def __init__(self):
        self.headers = {
            'Host': 'uniportal.huawei.com',
            'Referer': 'https://uniportal.huawei.com/uniportal/login.do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

        self.login_url = 'https://uniportal.huawei.com'
        self.post_url = 'https://uniportal.huawei.com/uniportal/login.do'
        self.logined_url = 'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=919&cate=44&cityId=8'
        self.session = requests.Session()

    def login(self, user_name, passwd):
        post_data = {
            ''
        }