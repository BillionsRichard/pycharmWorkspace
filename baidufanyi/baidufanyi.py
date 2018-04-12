# coding: utf-8
from pprint import pprint as pp
import requests

BAIDU_FANYI_URL = 'http://fanyi.baidu.com/v2transapi'
target_word = 'shit'

kwargs = {'headers': {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length':'122',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie':'BAIDUID=71264E3CA438130C4A553BD6D7879EDC:FG=1; BIDUPSID=71264E3CA438130C4A553BD6D7879EDC; PSTM=1510757267; BDUSS=ZZSmpHekV6a1J2LVNmZ2RzQXRuTGFkeFFiN2xoQ0NnNEF3VU10cXBoZ1ZvWEZhQVFBQUFBJCQAAAAAAAAAAAEAAAC-YosJY2hldW5nY3MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUUSloVFEpaVF; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; BDRCVFR[BIMQ49Drrdf]=I67x6TjHwwYf0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSINO=3; H_PS_PSSID=25668_1452_21088_18559_17001_22074; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1516500988,1516502076; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1516502996; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'Host': 'fanyi.baidu.com',
    'Origin': 'http://fanyi.baidu.com',
    # 'Pragma':'no-cache',
    'Referer': 'http://fanyi.baidu.com/translate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }

form_data = {'from': 'en',
             'to': 'zh',
             'query': target_word,
             'transtype': 'realtime',
             # 'simple_means_flag': 3,
             # 'token': '1d8a7b6295995ea6cbc694c5bbdf3234',
             #  'sign':862636.588557,
             }

response = requests.post(BAIDU_FANYI_URL, data=form_data, headers=headers)
pp(response.reason)
pp(response.status_code)

kwargs = {'encoding': 'utf-8'}

print(response.json())
