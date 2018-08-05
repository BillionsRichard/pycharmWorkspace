# coding:utf-
from pprint import pprint as pp

class Room(object):
    province = 'SC'
    def __init__(self, name, owner, width, lenght, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = lenght
        self.height = height

    @property  # 隐藏计算过程，和普通数据属性使用方法类似。
    def calc_area(self):
        area = self.width * self.length
        print('%s 住的 %s 的面积是 %s' % (self.owner, self.name, area))


    @classmethod # 类方法，不和实例关联。通过类或者实例（通常不这么用）调用时，自动传递类作为第一个参数。
    def test(cls):
        print(cls)
        print('from test %s' % cls.province)

    @staticmethod # 静态方法，
    def wash(a, b, c):
        print(Room.province)
        print('正在打扫%s %s %s' % (a, b, c))



# r1 = Room('Ncdh', 'sam', 30, 30, 4)
# r1.calc_area

Room.wash(1,2,3)

pp(Room.__dict__)