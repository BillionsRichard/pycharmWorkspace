def test(x, y, z):
    print(x)
    print(y)
    print(z)



# test(1,2,3)
# test(1,2,z=3)#关键字传递参数
# test(1,z=2,y=3)
#
# test(z=3,y=2,x=1)


def var_arg_fun(x, **kwargs):
    print(x)
    print(kwargs)


var_arg_fun(1, **dict(z=1,y=2))