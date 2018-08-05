#coding:utf-8
import os
import sys
from pprint import pprint as pp

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
print(os.chdir('test1'))
print(os.getcwd())
# print(os.mkdir('test1'))

# print(os.system('ping www.baidu.com'))

stat_obj = os.stat('__init__.py')
print(stat_obj)
print(type(stat_obj))

print('os.sep-->%s' % os.sep)
print('os.linesep-->[%s]' % os.linesep)
print('os.pathsep-->[%s]' % os.pathsep)
print('os.type-->[%s]' % os.name)

print(os.path.split(r'D:\Python\pycharmWorkspace\python全栈3期\demos\os模块学习.py'))
print(os.path.dirname(r'D:\Python\pycharmWorkspace\python全栈3期\demos\os模块学习.py'))
print(os.path.basename(r'D:\Python\pycharmWorkspace\python全栈3期\demos\os模块学习.py'))

print(os.path.getatime(r'D:\Python\pycharmWorkspace\python全栈3期\demos\os模块学习.py'))

pp(dict(os.environ))
pp(type(os.environ))

pp(sys.maxunicode)
pp(sys.maxsize)
pp(sys.platform)