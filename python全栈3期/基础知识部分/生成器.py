#生成器自动实现了迭代器协议
#可以直接调用next()方法。

"""
生成器函数：
1、常规函数定义：使用yield。
"""

def yield_fun():
    yield 'ok'

g = yield_fun()

print(g.__next__())
# print(g.__next__())

"""
列表解析生成“生成器”----生成器表达式。
"""

g = ('鸡蛋%s' % i for i in range(4))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# print(sum(i for i in range(1000000000000000000000000)))

def yield_child():
    print('开始生孩子1啦。。。。')
    yield '儿子。。。'

    print('又开始生孩子2啦。。。')
    yield '女儿。。。'

    print('再开始生孩子3啦。。。')
    yield '儿子1.。。。'

g = yield_child()

print(next(g))
print(next(g))
print(next(g))

g = yield_child()
print(next(g))