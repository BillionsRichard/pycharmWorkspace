# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: 包装标准类.py 
@time: 2018/5/13 17:27 
"""

class MyList(list):

    def show_middle(self):
        idx = int(len(self) /2)
        return self[idx]

    def append(self, obj):
        if type(obj) is str:
            # list.append(self, obj)
            super().append(obj) # 等价于上述的写法.
        else:
            print('只能添加字符串....')



l1 = MyList('hello world..')
l2 = list('hello world.')
print(l1)
print(l2)

print(type(l1))
print(type(l2))

print(l1.show_middle())

l1.append('ooxx')
l1.append(3)
print(l1)