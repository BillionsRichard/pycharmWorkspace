# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/11/13 21:06
"""

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

import collections


class Solution:
    def isNumber(self, s: str) -> bool:
        if not s.strip():
            return False

        s = s.strip().lower()
        cnt_dict = collections.Counter(s)
        valid_chars = ["+", "-", "e", "."] + list("0123456789")
        for c in cnt_dict:
            if c not in valid_chars:
                return False

        if cnt_dict.get("e", 0) > 1:
            return False

        if cnt_dict.get("+", 0) > 2:
            return False

        if cnt_dict.get("-", 0) > 2:
            return False

        if "e" in s:
            pre, post = s.split("e")
            if not post:
                return False

            if "." in post:
                return False

            if len(post) == 1 and post in ["+", "-"]:
                return False

            # 1e+12 ok
            if (
                    "+" in post and not post.startswith("+")
            ) or collections.Counter(post).get("+", 0) > 1:
                return False

            if (
                    "-" in post and not post.startswith("-")
            ) or collections.Counter(post).get("-", 0) > 1:
                return False

            if not pre:
                return False

            if len(pre) == 1 and pre in ["+", "-", "."]:
                return False

            pre_cnt_dict = collections.Counter(pre)
            for c in list("+-."):
                if pre_cnt_dict.get(c, 0) > 1:
                    return False

            if ("+" in pre and not pre.startswith("+")) or (
                    "-" in pre
                    and not pre.startswith("-")
                    or ("+" in pre and "-" in pre)
            ):
                return False

            return True

        pre = s
        pre_cnt_dict = collections.Counter(pre)
        if ("+" in pre and not pre.startswith("+")) or (
                "-" in pre
                and not pre.startswith("-", 0)
                or ("+" in pre and "-" in pre)
                or pre_cnt_dict.get(".", 0) >= 2
                or pre_cnt_dict.get("-", 0) >= 2
                or pre_cnt_dict.get("+", 0) >= 2
        ):
            return False

        if pre == ".":
            return False

        if pre in ['+.', '.+', "-+", "+-", '-.', '.-']:
            return False

        return True


if __name__ == "__main__":
    s = "0e1"
