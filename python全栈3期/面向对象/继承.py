class Dad:
    money = 10
    def __init__(self,name):
        print('dad')
        self.name = name

    def hit_son(self):
        print('%s is hitting son.' % self.name)

class Son(Dad):
    pass


# d = Dad('alex')
# s = Son('jack')
#
# print(Son.money)

print(Dad.__dict__)
print(Son.__dict__)