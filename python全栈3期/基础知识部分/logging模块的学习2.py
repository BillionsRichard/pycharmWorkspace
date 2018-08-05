#coding:utf-8

import logging
import time
import sys

"""
%(funcName)s

"""

# logging.basicConfig(
#     level=logging.WARNING, #只打印waning级别以上的日志（DEBUG < INFO < WARN < ERROR < CRITICAL)
#     # filename="test.log", #定义日志文件名,默认打印到控制台
#     filemode='a', # 覆盖写， 默认是追加模式，
#     format='[%(asctime)s] %(filename)s[%(lineno)d] %(message)s', # 非常重要的参数。
#     stream=open('demo.log', 'a', encoding='utf-8'), #不能和filename同时指定，推荐使用filename，可以指定编码
#
# )

"""
logger对象
"""

logger = logging.getLogger()

fh = logging.FileHandler(filename="demo2.log",encoding='utf-8',)
sh = logging.StreamHandler()

fm = logging.Formatter('%(asctime)s [%(levelname)s] %(pathname)s[%(lineno)d] %(message)s')

fh.setFormatter(fm)
sh.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(sh)

print(logger.getEffectiveLevel())
logger.setLevel(logging.DEBUG)
print(logger.getEffectiveLevel())

logger.debug("this is a debug message")
logger.info("this is a info message")
logger.error("this is a error message")

