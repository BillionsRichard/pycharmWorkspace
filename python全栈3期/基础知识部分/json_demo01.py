#coding:utf-8

import json
import pickle
from pprint import pprint as pp

info = json.load(open('./json_text.txt', 'r', encoding='utf-8'))
pp(info)
pp(type(info))

pp('pickle'.center(80, '*'))
pp(pickle.dumps(info))
pickle.dump(info,open('./pickle_file', 'wb'))

pickle_load_obj = pickle.load(open('./pickle_file', 'rb'))
pp(pickle_load_obj)
pp(type(pickle_load_obj))