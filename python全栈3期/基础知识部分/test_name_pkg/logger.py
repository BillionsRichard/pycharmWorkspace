# coding:utf-8
import logging


def getLogger(logger_name):
    """获取logger对象

    :return:
    """
    logger = logging.getLogger(logger_name) if logger_name else logging.getLogger()

    fh = logging.FileHandler(filename="demo2.log", encoding='utf-8', )
    sh = logging.StreamHandler()

    fm = logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s] %(pathname)s[%(lineno)d] %(message)s')

    fh.setFormatter(fm)
    sh.setFormatter(fm)

    logger.addHandler(fh)
    logger.addHandler(sh)

    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger = getLogger()

    logger.debug("this is a message from get logger.")
