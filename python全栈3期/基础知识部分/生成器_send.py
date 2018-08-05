def producer():
    print('第一次...')
    first = yield  1

    print('第二次...%s' % first)
    yield  2

    print('第三次...')
    yield  3

p = producer()

print('准备迭代生成器....')
r1 = next(p)

print('第一次迭代结果')
print(r1)

print('第一次向生成器发送内容.....')
r2 = p.send('send call ')

print('发送完毕....')
print(r2)

print('第2次向生成器发送内容.....')
r3 = p.send('send call 2')
print(r3)

