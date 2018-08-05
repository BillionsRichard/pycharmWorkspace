#coding:utf-8

import logging
import time
import sys

"""
%(funcName)s

"""
logging.basicConfig(
    level=logging.WARNING, #只打印waning级别以上的日志（DEBUG < INFO < WARN < ERROR < CRITICAL)
    # filename="test.log", #定义日志文件名,默认打印到控制台
    filemode='a', # 覆盖写， 默认是追加模式，
    format='[%(asctime)s] [%(levelname)s] %(filename)s[%(lineno)d] %(message)s', # 非常重要的参数。
    stream=open('demo.log', 'a', encoding='utf-8'), #不能和filename同时指定，推荐使用filename，可以指定编码

)

"""
print('logging的最简单应用--向控制台输出日志'.center(120, '-'))
time.sleep(1)

logging.debug('this is a debug message...')
logging.info('this is a info message...')
logging.warn('this is a warn message...')
logging.warning('this is a warning message...')
logging.error('this is a error message...')
logging.critical('this is a critical message...')

print('logging的应用--向日志文件输出'.center(120, '-'))
time.sleep(1)
"""


logging.debug('this is a debug message to log file')
logging.info('this is a info message to log file')
logging.warning('this is a warning message to log file')
logging.error('this is an error message to log file')
logging.critical('this is a critical message to log file')

print(sys.getdefaultencoding())