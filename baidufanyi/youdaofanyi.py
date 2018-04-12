# coding: utf-8
from pprint import pprint as pp
import requests

YOUDAO_FANYI_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
target_word = 'shit'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

form_data = {
    'i': target_word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult': 'false',
}

response = requests.post(YOUDAO_FANYI_URL, data=form_data, headers=headers)
pp(response.reason)
pp(response.status_code)

kwargs = {'encoding': 'utf-8'}

print(response.url)
