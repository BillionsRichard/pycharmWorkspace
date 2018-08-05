#codig:utf-8

country = 'china'

class Chinese:
    country='中国'

    def __init__(self, name):
        self.name = name

        print('---->%s' % Chinese.country) # 类的属性必须显式通过类来访问.
        print('---->%s' % country)


print(Chinese.__dict__)
print(Chinese.country)

p1 = Chinese('alex')
print(p1.country)