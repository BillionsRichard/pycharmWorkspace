def kw_fun(a,b,*args, **kwargs):
    print('不解包可变参数打印结果【元组】'.center(80, '*'))
    print(type(args))
    print(args)

    print('关键字参数打印结果【字典】'.center(80, '*'))
    print(type(kwargs))
    print(kwargs)


# kw_fun(1,2,3,4, log=True, log_level=3)#传递了关键字参数。
# kw_fun(1,2, 3, 4, {'log':True, 'log_level': 3})#并未传递关键字参数。
kw_fun(1,2, 3, 4, **{'log':True, 'log_level': 3})#传递关键字参数。