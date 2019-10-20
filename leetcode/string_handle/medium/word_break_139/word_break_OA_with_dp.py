# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/19 8:13 
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        s_len = len(s)
        # dp[i] 记录 s[0:i] 是否在字典中。
        dp = [False for _ in range(s_len + 1)]

        for i in range(s_len):
            for j in range(i + 1, s_len + 1):
                if i == 0:
                    if s[i:j] in wordDict:
                        dp[j] = True

                # i > 0 但是 [0:i] 不在字典中
                elif not dp[i]:
                    continue
                # i > 0 且 [0:i] 在字典中
                elif s[i:j] in wordDict:
                    dp[j] = True

        return dp[s_len]
