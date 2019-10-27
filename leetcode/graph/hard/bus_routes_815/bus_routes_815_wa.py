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
        graph = defaultdict(set)
        site_to_bus_dict = dict()
        visited = dict()
        bus_num = len(routes)
        for bn in range(bus_num):
            route = routes[bn]
            if len(route) < 2:
                continue
            if S in route and T in route:
                return 1

            for site in route:
                if site not in site_to_bus_dict:
                    site_to_bus_dict[site] = bn
                visited[site] = False

        print(site_to_bus_dict)

        for route in routes:
            for site in route:
                other_sites = route[:]
                other_sites.remove(site)
                for s in other_sites:
                    graph[site].add(s)
        pp(graph)

        visited_bus_num_set = set()
        queue = [S]
        visited_bus_num_set.add(site_to_bus_dict.get(S))

        visited[S] = True

        while queue:
            cur_site = queue.pop(0)
            next_sites = graph.get(cur_site)
            for ns in next_sites:
                if not visited[ns]:
                    visited[ns] = True
                    bus_n = site_to_bus_dict.get(ns)
                    visited_bus_num_set.add(bus_n)
                    if ns == T:
                        return len(visited_bus_num_set)
                    queue.append(ns)

        return -1


if __name__ == '__main__':
    s = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    S = 1
    T = 6
    r = s.numBusesToDestination(routes, S, T)
    print(r)
