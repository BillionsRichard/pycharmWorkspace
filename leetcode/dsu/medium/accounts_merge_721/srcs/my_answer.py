# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/7 22:41 
"""
from collections import defaultdict
from typing import List

"""
每个账户由名称和邮箱地址组成，不同账户中，只要有相同的一个邮箱地址，则合并为一个账户
所以可以把账户看作一个点，只要两个账户有相同的邮箱地址，则将两个点连起来
"""


class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, p):
        """找前驱。

        :param p:
        :return:
        """
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        """判断 p, q 是否 连同：p q 的前驱是否相同。

        :param p:
        :param q:
        :return:
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """ 连通 P Q

        :param p:
        :param q:
        :return:
        """
        if self.is_connected(p, q):
            return

        parent_p = self.find(p)
        parent_q = self.find(q)

        if self.rank[parent_p] < self.rank[parent_q]:  # 以权重较大为父节点
            self.parent[parent_p] = parent_q

        elif self.rank[parent_q] < self.rank[parent_p]:  # 以权重较大为父节点
            self.parent[parent_q] = parent_p

        else:
            self.parent[parent_q] = parent_p  # q 的父节点指向 p 的父节点
            self.rank[parent_p] += 1  # p 的父节点 权重 +1， 子节点越多，权重越大


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 记录已经出现过的邮箱地址:账户
        lookup = {}
        n = len(accounts)
        un = Union(n)
        # 第一步，找到相关联的账户，并使用并查集记录
        for idx, account in enumerate(accounts):
            email = account[1:]
            for em in email:
                if em in lookup:  # 如果之前已经有该 email， 则合并。
                    un.union(idx, lookup[em])
                else:
                    lookup[em] = idx  # 记录每个 email 的前驱

        # 第二步，将相关联账户的邮箱地址合并起来
        joint_account = defaultdict(set)
        for i in range(n):
            root = un.find(i)
            for em in accounts[i][1:]:
                joint_account[root].add(em)

        # 第三步，输出结果
        res = []
        for key, val in joint_account.items():
            res.append([accounts[key][0]] + list(sorted(val)))

        return res


if __name__ == '__main__':
    from pprint import pprint as pp

    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    ans = s.accountsMerge(accounts)
    pp(ans)
    # s1 = set(['johnsmith@mail.com', 'john00@mail.com'])
    # s2 =  set(['johnsmith@mail.com', 'john_newyork@mail.com'])
    # print(s1 & s2)
