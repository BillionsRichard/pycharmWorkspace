#coding:utf-8

import hashlib


# 设置盐值，得到不同的hash值
obj1 = hashlib.md5('sault'.encode('utf-8'))
obj11 = hashlib.md5('sault'.encode('utf-8'))
obj2 = hashlib.md5('sault1'.encode('utf-8'))

obj1.update('hello'.encode('utf-8'))
obj2.update('hello'.encode('utf-8'))

obj1.update('world'.encode('utf-8'))
obj11.update('helloworld'.encode('utf-8'))

digest1 = obj1.hexdigest()
digest11 = obj11.hexdigest()
digest2 = obj2.hexdigest()

print(digest1)
print(digest11)
print(digest2)

print(len(digest1))
print(len(digest2))
