#coding:utf-8
args = (1,23, 'a', 'e')
args1 = [1,2,3,4]

#不解包传参数（作为一个单独的参数）
print(args, 2) # 实际传递了2个参数

#解包传参数（解包成多个参数传递)
print(*args, 2)  #实际传递了 len(args) + 1 = 5 个参数

print('*'*10)
print(args1)
print('*'*10)
print(*args1)

def var_arg_fun(x, *args):
    print(x)
    print(args)
    print(*args)

var_arg_fun(2, args)