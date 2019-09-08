# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: sentenceToWordVector.py
@time: 2018/9/16 8:24 
"""
from pprint import pprint as pp
import jieba

s1 = "这只皮靴号码大了。那只号码合适"
s2 = "这只皮靴号码不小。那只更合适"


def get_term_frequency(sentence):
    """获取一段文本（一句话）中的各个词语的词频。

    :param sentence:
    :return:
    """
    word_list = jieba.cut(sentence, cut_all=True)
    word_freq = dict()
    for word in word_list:
        word_cnt = word_freq.get(word, 0) + 1
        word_freq[word] = word_cnt
    return word_freq


# word_cnt_map2 = dict()
# for word in s2_word_list:
#     word_cnt = word_cnt_map2.get(word, 0) + 1
#     word_cnt_map2[word] = word_cnt


def word_list_to_vector(word_list, word_cnt_map, stop_word_set):
    """句子转成向量

    :param all_word_list:
    :param word_cnt_map:
    :param stop_word_set:
    :return:
    """
    vector = []

    for word in word_list:
        if word in stop_words_set:
            continue
        vector.append(word_cnt_map.get(word, 0))
    return vector


def get_stop_words_set(file_name):
    """Read stop words to a set and return it.

    :param file_name:
    :return:
    """
    stop_words_set = set()
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                if word:
                    stop_words_set.add(word)

    return stop_words_set


stop_words_set = get_stop_words_set("stop_words")
s1_word_freq = get_term_frequency(s1)
s2_word_freq = get_term_frequency(s2)
all_word_list = list(set(list(s1_word_freq.keys()) + list(s2_word_freq.keys())))

pp(all_word_list)
s1_vector = word_list_to_vector(all_word_list, s1_word_freq, stop_words_set)
s2_vector = word_list_to_vector(all_word_list, s2_word_freq, stop_words_set)

print(s1_vector)
print(s2_vector)
print(stop_words_set)
# [1, 2, 0, 1, 0]
# [1, 1, 1, 1, 1]