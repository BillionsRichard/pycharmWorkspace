# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: wsgiDemo01.py 
@time: 2018/6/22 8:19 
"""
from pprint import pprint as P
from wsgiref.simple_server import make_server

def app(environ, start_response):
    P(environ)
    P(start_response)
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'<h1>Hello wsgi server</h1>']

httpd = make_server('', 8080, app)
httpd.serve_forever()

