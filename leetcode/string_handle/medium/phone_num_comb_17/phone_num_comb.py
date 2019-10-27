# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 13:19 
"""
from pprint import pprint as pp


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_alpha_dict = {'2': list('abc'),
                          '3': list('def'),
                          '4': list('ghi'),
                          '5': list('jkl'),
                          '6': list('mno'),
                          '7': list('pqrs'),
                          '8': list('tuv'),
                          '9': list('wxyz'),
                          }
        ans = []
        for digit in digits:
            chrs = num_alpha_dict.get(digit)
            if not ans:
                ans = chrs[:]
                continue

            new_ans = []
            for an in ans:
                for ch in chrs:
                    new_ans.append(an + ch)
            ans = new_ans
            del new_ans

        return ans





