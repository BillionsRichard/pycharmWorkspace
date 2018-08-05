# encoding: utf-8  

"""
（2）给定一个IP地址和一个子网，判断IP地址是否在子网范围内
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: IP地址.py 
@time: 2018/7/26 21:13 
"""
from pprint import pprint as P
import IPy

def is_ip_in_sub_net(ip, sub_net):
    """

    :param ip:
    :param sub_net:
    :return:
    """
    try:
        return ip in IPy.IP(sub_net)
    except Exception as e:
        print(e)
        return False