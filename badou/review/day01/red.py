# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: red.py 
@time: 2019/2/4 11:26 
"""
from pprint import pprint as pp
import sys

word_dict = dict()
for line in sys.stdin:
    word, cntStr = line.split()
    new_cnt = word_dict.setdefault(word, 0) + int(cntStr)
    word_dict[word] = new_cnt

for word in word_dict:
    print("%s\t%d" % (word, word_dict.get(word, 0)))

# cur_word = None
# word_cnt_sum = 0
#
# for line in sys.stdin:
#     word, word_cnt = line.split()
#
#     if cur_word is None:
#         cur_word = word
#         word_cnt_sum = 0
#
#     if cur_word != word:
#         print("%s\t%d" % (cur_word, word_cnt_sum))
#         word_cnt_sum = word_cnt
#         cur_word = word
#     else:
#         word_cnt_sum += int(word_cnt)
#
# print("%s\t%d" % (cur_word, word_cnt_sum))
