# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@file: cut.py 
@time: 2018/12/23 10:59 
"""
from pprint import pprint as P
import token
import jieba
from sklearn.feature_extraction.text import CountVectorizer

s = "中文分词和大数据，还有云计算，相当于将数组中的字符拼接成字符串"

s_list = ["中文分词", '大数据', '云计算']
s_list = ["中文分词", '中文计算', '大数据', '云计算', "用结巴分词做中文分词"]
s_l = [" ".join(jieba.cut(x)) for x in s_list]

# jieba.load_userdict(open("./mydict", encoding="utf8"))
# jieba.load_userdict("mydict")
print("/".join(jieba.cut(s, cut_all=False)))


"""
    ngram_range : tuple (min_n, max_n)
        The lower and upper boundary of the range of n-values for different
        n-grams to be extracted. All values of n such that min_n <= n <= max_n
        will be used.

        """
n_gram = CountVectorizer(ngram_range=(2,2), min_df=1)
x1 = n_gram.fit_transform(s_l)
print(x1)
print(n_gram.vocabulary_)

