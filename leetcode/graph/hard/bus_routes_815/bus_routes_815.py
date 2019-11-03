# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/27 15:20 
"""
from pprint import pprint as pp


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        from collections import defaultdict

        graph = defaultdict(set)

        bus_cnt = len(routes)

        # 建立公交路线图 （经历某站点的所有公交路线list）
        # k：站点编号
        # v: [公交编号, ...]
        for bn in range(bus_cnt):
            route = routes[bn]
            if len(route) < 2:
                continue

            if S in route and T in route:
                return 1

            for bus_site in route:
                graph[bus_site].add(bn)


        def get_bus_nums(S):
            """获取经过站点 S 的所有公交路线编号。

            :param S:
            :return:
            """
            bus_nums = []
            for i in range(bus_cnt):
                if S in routes[i]:
                    bus_nums.append(i)
            return bus_nums


        def bfs(S, T):
            """基于公交路线的 BFS。

            总体思路：从起点站开始，依次遍历经过该站点的所有公交路线。
                遍历公交路线的方法如下：依次检查该路线的每一个站点，
                1）如果站点是 终点站，则找到结果；
                2）否则，查看经过该站点的所有公交线路：如果该线路未遍历过。则放入
                队列尾部；否则跳过。

            :param S:
            :param T:
            :return:
            """
            bus_nums = get_bus_nums(S)
            if not bus_nums:
                return -1
            # print('bus_nums', bus_nums)
            nonlocal bus_cnt
            bus_visited = [False for _ in range(bus_cnt)]
            bus_queue = []
            for bn in graph.get(S, []):
                bus_queue.append(bn)
                bus_visited[bn] = True

            step = 0
            while bus_queue:
                step += 1
                bus_cnt = len(bus_queue)
                # 遍历队列里面的已有的公交路线（不包括遍历过程中添加的，否则
                # 影响 step 计数。
                for i in range(bus_cnt):
                    bn = bus_queue.pop(0)
                    bus_route = routes[bn]
                    # 遍历 该路线的所有站点。
                    for bus_site in bus_route:
                        if bus_site == T:
                            return step

                        # 检查经过该站点的所有线路是否遍历过，如未遍历过，则入队。
                        pass_this_site_buses = graph.get(bus_site, [])
                        for bn in pass_this_site_buses:
                            if not bus_visited[bn]:
                                bus_queue.append(bn)
                                bus_visited[bn] = True
            return -1


        return bfs(S, T)

if __name__ == '__main__':
    s = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    r = s.numBusesToDestination(routes, S, T)
    print(r)
