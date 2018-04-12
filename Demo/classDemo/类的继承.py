#coding:utf-8

class Father(object):
    def __init__(self, wealth):
        self.wealth = wealth
        print("father creating...")


class Son(Father):
    def __init__(self, wealth):
        print("son creating...")
        super(Son, self).__init__(wealth)


s = Son(1)