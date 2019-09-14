# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/13 22:43 
"""
from pprint import pprint as pp

class Solution:
    def countCharacters(self, words, chars):
        word_cnt = len(words)
        word_cab_list = list(chars)
        word_tot_len = 0
        for i in range(word_cnt):
            word = words[i]
            for word_chr in word:
                if list(word).count(word_chr) > word_cab_list.count(word_chr):
                    break
            else:
                word_tot_len += len(word)

        return word_tot_len


if __name__ == '__main__':
    s = Solution()
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(s.countCharacters(words, chars))
