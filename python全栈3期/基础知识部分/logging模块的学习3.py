#coding:utf-8

from test_name_pkg import logger

"""
logger对象
"""

logger1 = logger.getLogger('mylogger1')
logger2 = logger.getLogger('mylogger2')

print(id(logger1) == id(logger2))

logger1.debug("this is a debug message printed by logger1")
logger1.info("this is a info message printed by logger1")
logger1.error("this is a error message printed by logger1")

logger2.debug("this is a debug message printed by logger2")
logger2.info("this is a info message printed by logger2")
logger2.error("this is a error message printed by logger2")

