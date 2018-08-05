# coding:utf-8
usr_list = [
    {'usr_name': 'sam', 'passwd':'sam'},
    {'usr_name': 'tom', 'passwd':'tom'},
    {'usr_name': 'jack', 'passwd':'jack'},
    {'usr_name': 'eva', 'passwd':'eva'},
]

login_status = []


"""
定义一个装饰器函数，实现对函数的鉴权

"""
def auth_fun(func):
    def wrapper(*args, **kwargs):

        usr_name = args[0]

        if usr_name in login_status:
            return func(*args, **kwargs)
        else:
            passwd = input('%s的密码:' % usr_name).strip()
            for usr_info in usr_list:
                if usr_info.get('usr_name') == usr_name and usr_info.get('passwd') == passwd:
                    login_status.append(usr_name)
                    return func(*args, **kwargs)
            else:
                print('用户名或者密码错误....')

    return wrapper


# @auth_fun
def index():
    print('欢迎登陆京东主页...\n')


@auth_fun
def home(usr_name):
    print('欢迎%s回到主页...\n' % usr_name)


@auth_fun
def shopping_car(usr_name):
    print('%s 的购物车里有[%s, %s, %s]\n' % (usr_name, '奶茶', '妹妹', '娃娃'))


@auth_fun
def order():
    print('欢迎登陆京东主页...\n')


# index()
home('eva')
shopping_car('sam')
home('eva')
