"""
函数嵌套：函数中定义了函数。

闭包：


"""


def father(name):
    print('from father:%s' % name)

    def son():
        print('我的爸爸是：%s' % name)
        def grandson():
            print('我的爷爷是:%s' % name)
        grandson()

    print(locals())
    son()

father('Sam')