class People(object):
    __star = 'earth'
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salry = salary

    def get_id(self):
        print('my id is:%s' % self.id)