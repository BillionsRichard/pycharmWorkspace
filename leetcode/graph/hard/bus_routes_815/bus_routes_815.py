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
        from collections import defaultdict
        graph = defaultdict(list)
        visited = dict()
        bus_cnt = len(routes)
        for bn in range(bus_cnt):
            route = routes[bn]
            if len(route) < 2:
                continue

            if S in route and T in route:
                return 1

            route_len = len(route)
            lst_site = route[0]
            for i in range(1, route_len):
                k = lst_site, bn
                v = route[i], bn
                graph[k].append(v)
                lst_site = route[i]
            k = lst_site, bn
            v = route[0], bn
            graph[k].append(v)


        print('bus graph===>')
        pp(graph)

        def get_bus_nums(S):
            bus_nums = []
            for i in range(bus_cnt):
                if S in routes[i]:
                    bus_nums.append(i)
            return bus_nums



        def bfs(S, T):
            bus_nums = get_bus_nums(S)
            if not bus_nums:
                return -1
            print('bus_nums', bus_nums)
            nonlocal bus_cnt
            min_bus_num = bus_cnt
            can_reach = True
            for start_bus_num in bus_nums:
                start_k = (S, start_bus_num)
                queue = [start_k]
                visited_bus_nums = set()
                visited.clear()
                visited[start_k] = True
                visited_bus_nums.add(S)
                # visited_bus_num_set.add(site_to_bus_dict.get(S))
                visited_bus_num = 1
                reached = False

                while not reached and queue:
                    site, cur_bus_num = queue.pop(0)

                    next_sites_and_bus_nums = graph.get((site, cur_bus_num))

                    for ns, bn in next_sites_and_bus_nums:
                        if not visited.get((ns, bn)):
                            visited[(ns, bn)] = True
                            if bn not in visited_bus_nums:
                                visited_bus_nums.add(bn)

                                if ns == T:
                                    min_bus_num = min(min_bus_num,
                                                      len(visited_bus_nums))
                                    reached = True
                                    visited_bus_nums.remove(bn)
                                    continue

                                queue.append((ns, bn))
                    if reached:
                        can_reach = True

            return min_bus_num if can_reach else -1

        return bfs(S, T)


if __name__ == '__main__':
    s = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    r = s.numBusesToDestination(routes, S, T)
    print(r)
