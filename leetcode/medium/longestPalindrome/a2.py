# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/8 11:48 
"""
from collections import namedtuple

Palindrome = namedtuple('Palindrome', field_names=['start', 'end'])


class Solution:
    def longestPalindrome(self, input_str: str) -> str:
        if not input_str:
            return ''

        if len(set(input_str)) == 1:
            return input_str

        if len(input_str) == 1:
            return input_str

        p_list = self.find_smallest_palindrome(input_str)
        sub_str_list = self.find_long_palindromes(input_str, p_list)

        sub_str_list.sort(key=len)
        if sub_str_list:
            return sub_str_list[-1]
        else:
            return input_str[0]

    @staticmethod
    def find_long_palindromes(input_str, p_list):
        """基于最小的回文串(xx, xyx)，分别向左右查找更大的回文串。

        :param input_str:
        :param p_list:
        :return:
        """
        str_len = len(input_str)

        sub_str_list = []
        for p in p_list:
            i, j = p
            i -= 1
            j += 1

            while i >= 0 and j < str_len and input_str[i] == input_str[j]:
                i -= 1
                j += 1

            sub_str_list.append(input_str[i + 1:j])
        return sub_str_list

    @staticmethod
    def find_smallest_palindrome(input_str):
        """找到最小的回文串：即：xx or xyz 形式的回文串。

        :param input_str:
        :return:
        """
        str_len = len(input_str)
        p_list = []

        for i in range(str_len):
            if i + 1 < str_len and input_str[i] == input_str[i + 1]:
                p = Palindrome(i, i + 1)
                p_list.append(p)

            if i + 2 < str_len and input_str[i] == input_str[i + 2]:
                p = Palindrome(i, i + 2)
                p_list.append(p)

        return p_list
