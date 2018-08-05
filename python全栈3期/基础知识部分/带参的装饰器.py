# coding:utf-8
usr_list = [
    {'usr_name': 'sam', 'passwd':'sam'},
    {'usr_name': 'tom', 'passwd':'tom'},
    {'usr_name': 'jack', 'passwd':'jack'},
    {'usr_name': 'eva', 'passwd':'eva'},
]

login_status = []


"""
定义一个带参的装饰器函数，实现对函数的鉴权

"""
def auth(auth_type='filedb'):

    def auth_fun(func):

        def wrapper(*args, **kwargs):
            print('认证类型是：%s' % auth_type)
            usr_name = args[0]
            if auth_type == 'filedb':
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
            elif auth_type == 'ldap':
                print('鬼才特么会玩儿...\n')
            else:
                print('什么鬼认证方式....\n')

        return wrapper

    return auth_fun


# @auth_fun
def index():
    print('欢迎登陆京东主页...\n')


@auth(auth_type='filedb')
def home(usr_name):
    print('欢迎%s回到主页...\n' % usr_name)


@auth(auth_type='mysqldb')
def shopping_car(usr_name):
    print('%s 的购物车里有[%s, %s, %s]\n' % (usr_name, '奶茶', '妹妹', '娃娃'))


# @auth_fun
def order():
    print('欢迎登陆京东主页...\n')


# index()
home('eva')
shopping_car('sam')
home('eva')
