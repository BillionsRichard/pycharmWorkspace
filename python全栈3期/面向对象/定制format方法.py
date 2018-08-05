# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 定制format方法.py 
@time: 2018/5/15 8:20 
"""

class Date:
    format_dict = {
        'ymd': '{0.year}{0.month}{0.day}',
        'mdy': '{0.month}{0.day}{0.year}',
        'y-m-d': '{0.year}-{0.month}-{0.day}',
    }
    dft_fmt = format_dict.get('ymd')

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        print('format called..')
        fmt = Date.format_dict.get(format_spec, Date.dft_fmt)
        print(fmt)
        return fmt.format(self)


d = Date(2018,5,15)
print(format(d))
print(format(d, 'y-m-d'))