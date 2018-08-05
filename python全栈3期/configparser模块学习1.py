import configparser

"""
配置文件的增删查改


"""


config = configparser.ConfigParser()
config.read('./example.ini')

print('sections()方法获取除“default"外的所有配置分区key值'.center(80, '-'))
print(config.sections())

print('\n')
print('options(section_name)获取除指定分区(包括default）的外的所有配置分区配置子段key值'.center(80, '-'))
print(config.options('bitbucket.org'))

# print(config.options('DEFAULT')) # 不能获取default分区

print('\n')
print(config.items('topsecret.server.com'))
print('\n')


for key in config['bitbucket.org']: # 注意“default” section的特殊性。
    print(key)


print('配置文件的遍历'.center(80, '-'))
for section in config:
    # print(type(config[section]))
    print('%s' % section.center(40, '*'))
    for key in config[section]:

        print('%s--->%s' % (key, config[section].get(key)))

print('配置文件的修改'.center(120, '^'))

config.add_section('yuan')
# config.remove_section('topsecret.server.com')
config.remove_option('topsecret.server.com', 'forwardx11')

config['yuan']['db'] = 'mysql'
config['bitbucket.org']['user'] = 'root'

config.write(open('newConfig.ini', 'w'))