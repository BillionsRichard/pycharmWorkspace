from functools import reduce

num_list = range(1,10+1)
chs = ['a', 'b', 'c', 'd']
print(reduce(lambda x,y:x*y, num_list))
print(reduce(lambda x,y:x+y, num_list))
print(reduce(lambda x,y:x+'*'+y,chs))

