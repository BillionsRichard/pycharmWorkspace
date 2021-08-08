# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/12/20 11:32
"""

"""
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"

"cbaccdbc"
[c][b]a[c]cdb[c]

"cdadabcc"  c:2 d:1 a:1

c:1 a:1
c[d]adab[c]c
cadabc

adabc ====> cbada

"cdadabcc"
c[d]adab[c]c==cadabc

[c]adabc===adabc
ad[a]bc

"""
from collections import deque
from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = dict()
        n = len(s)
        for i,char in enumerate(s):
            last_index[char] = i

        in_stack = defaultdict(bool)
        q = deque()
        for i, char in enumerate(s):
            if in_stack[char]:
                continue

            if not q:
                q.append(char)
                in_stack[char] = True
                continue

            while q and q[-1] > char and last_index[q[-1]] > i:
                top = q.pop()
                in_stack[top] = False

            q.append(char)
            in_stack[char] = True

        return ''.join(q)





if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("cbacdcbc"))  # [c][b]acd[c]b[c]---> acdb
    print(s.removeDuplicateLetters("bcabc"))  # [c][b]acd[c]b[c]---> acdb
    print(s.removeDuplicateLetters("cbaccdbc"))  # [c][b]acd[c]b[c]---> acdb
    print(s.removeDuplicateLetters("cbaccdbc"))  # [c][b]acd[c]b[c]---> acdb
    print(s.removeDuplicateLetters("cdadabcc"))  # c[d]adab[c]c ==> cadabc
    print(s.removeDuplicateLetters("abacb"))  # c[d]adab[c]c ==> cadabc

