# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 21:42 
"""
# from pprint import pprint as pp

"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的
机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出
发的先生，所以该行程必须从 JFK 出发。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 
["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更
大更靠后。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-itinerary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
from pprint import pprint as pp


class Solution:
    # TODO: 该代码提交后用例 6 超时。

    def findItinerary(self, tickets: list) -> list:
        self.ports_graph_dict = defaultdict(list)
        tkt_num_dict = dict()
        for src, dst in tickets:
            self.ports_graph_dict[src].append(dst)
            tkt = (src, dst)
            tkt_num_dict[tkt] = tkt_num_dict.get(tkt, 0) + 1

        self.tkt_num_dict = tkt_num_dict
        self.min_route = None
        self.tkt_num = len(tickets)

        pp(self.ports_graph_dict)
        pp(self.tkt_num_dict)
        print('tkt num', self.tkt_num)

        ports = ['JFK']
        next_ports = self.ports_graph_dict.get('JFK', [])
        for next_port in next_ports:
            tkt = ('JFK', next_port)
            self.tkt_num_dict[tkt] -= 1
            ports.append(next_port)

            self.dfs(next_port, ports)

            self.tkt_num_dict[tkt] += 1
            ports = ['JFK']

        print('all routes:')
        return self.min_route.split()

    def dfs(self, src_port: str, ports: list):
        """深度优先遍历算法（DFS）

        :param src_port:
        :param ports:
        :return:
        """

        next_ports = self.ports_graph_dict.get(src_port, [])
        if not next_ports:
            # 递归调用下一步：检查路线是否遍历完，如果遍历完，则记录结果
            # ----很重要！！！
            cur_ports_str = ' '.join(ports)
            if sum(self.tkt_num_dict.values()) == 0 and \
                    (self.min_route is None or cur_ports_str < self.min_route):
                self.min_route = cur_ports_str

        for next_port in next_ports:
            tkt = (src_port, next_port)
            # IMPORTANT ! 由于 出发地和目的地都相同的机票可能不止一张，
            # 故通过计数来标记已经遍历过的机票
            if self.tkt_num_dict.get(tkt, 0) > 0:
                ports.append(next_port)
                self.tkt_num_dict[tkt] -= 1

                self.dfs(next_port, ports)

                # 递归调用下一步：检查路线是否遍历完，如果遍历完，则记录结果
                # ----很重要！！！
                cur_ports_str = ' '.join(ports)
                if sum(self.tkt_num_dict.values()) == 0 and \
                        (self.min_route is None or
                         cur_ports_str < self.min_route):
                    self.min_route = cur_ports_str

                ports.pop()
                self.tkt_num_dict[tkt] += 1
