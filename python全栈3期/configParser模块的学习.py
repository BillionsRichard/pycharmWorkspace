import configparser

config = configparser.ConfigParser()


config['DEFAULT'] = {
    'serverActiveInterval': 45,
    'compression': 'yes',
    'compressLevel':'9'
}

config['topsecret.server.com'] = {}

topSecret = config['topsecret.server.com']
topSecret['Host Port'] = '50020'
topSecret['ForwardX11'] = 'no'

config['bitbucket.org'] = {'user':'hg'}



with open('example.ini', 'w') as f:
    config.write(f)