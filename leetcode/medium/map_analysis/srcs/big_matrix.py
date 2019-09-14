# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/14 16:56 
"""
from pprint import pprint as pp

BIG_GRID = [[0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1],[0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1],[1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1],[0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0],[1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0],[0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1],[0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0],[1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0],[0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1],[1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0],[1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0],[1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1],[0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0],[1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0],[0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1],[0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1],[1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,0],[0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,1],[1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1],[1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1],[0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1],[0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1],[1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0],[0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0],[1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0],[1,1,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1],[1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1],[0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0],[0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],[0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1],[0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1],[0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1],[0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,1],[1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0],[1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],[1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1],[1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0],[0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1],[0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0],[1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1],[1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1],[1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1],[1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],[1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0],[0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0],[0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],[1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1],[1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,1],[1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0],[0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,1],[1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0],[0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1],[0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],[0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0],[0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0],[0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1],[1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1],[0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0],[0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0],[0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0],[1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1]]
BIG_GRID_13 = [[1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1],[0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1],[1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0],[0,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],[1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1],[1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1],[1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0],[1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,0],[0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0],[1,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1],[1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1],[0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,1],[0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,0],[0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,1],[1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0],[0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0],[0,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1],[0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0],[0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0],[0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],[1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1],[1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0],[0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0],[1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1],[1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1],[1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0],[1,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1],[0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0],[1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1],[0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0],[0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1],[0,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1],[1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1],[1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1],[1,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0],[0,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0],[1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0],[1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1],[1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1],[0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0],[0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1],[0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0],[0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0],[0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0],[0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1],[1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0],[1,1,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0],[1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0],[1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1],[0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0],[1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1],[0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1],[0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1],[0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,0,0],[1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1],[1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0],[0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0],[0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1],[1,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1],[0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0],[1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0],[1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1],[0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0],[0,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,0,1],[1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1],[0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1],[1,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0],[1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1],[1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1]]
