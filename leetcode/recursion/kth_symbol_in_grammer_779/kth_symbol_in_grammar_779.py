# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2019/12/29 12:18
"""

"""
在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）


例子:

输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

注意：

N 的范围 [1, 30].
K 的范围 [1, 2^(N-1)].
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-symbol-in-grammar
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # CACHE = dict()

    def kthGrammar(self, N: int, K: int) -> int:

        def robot(N):
            """返回第N行所有数字构造的数组

            :param N:
            :return:
            """
            # if N in Solution.CACHE:
            #     return Solution.CACHE.get(N, [])

            if N == 1:
                # Solution.CACHE[1] = [0]
                return [0]

            if N == 2:
                # Solution.CACHE[2] = [0, 1]
                return [0, 1]

            n_1_nums = robot(N - 1)
            n_nums = []

            for n in n_1_nums:
                rep = [0, 1] if n == 0 else [1, 0]
                n_nums.extend(rep)

            del n_1_nums
            # Solution.CACHE[N] = n_nums
            return n_nums

        n_nums = robot(N)
        return n_nums[K - 1]
