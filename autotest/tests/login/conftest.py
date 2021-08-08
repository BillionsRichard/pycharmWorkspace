# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/11/1 10:53
"""

import pytest


@pytest.fixture(scope="package", autouse=True)
def st_login():
    print("初始化---login")

    yield

    print("清除---login")
