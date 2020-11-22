# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/11/22 10:17
"""
from typing import List
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        pre_dict = defaultdict(list)
        for par, sons in enumerate(graph):
            for son in sons:
                pre_dict[son].append(par)

        def path_to(end):
            if end == 0:
                return [[0]]

            parents = pre_dict.get(end, [])

            all_paths = []
            for parent in parents:
                paths_to_parent = path_to(parent)
                for pre_path in paths_to_parent:
                    pre_path.append(end)
                    all_paths.append(pre_path)

            return all_paths

        return path_to(len(graph) - 1)


if __name__ == "__main__":
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    s = Solution()
    print(s.allPathsSourceTarget(graph))
