# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/1/5 12:17
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        from collections import defaultdict

        N = len(rooms)
        visited = defaultdict(bool)
        keys_queue = deque(rooms[0])
        visited[0] = True

        while keys_queue:
            key = keys_queue.popleft()
            # if visited[key]:
            #     continue
            visited[key] = True
            for nk in rooms[key]:
                if not visited[nk]:
                    visited[nk] = True
                    keys_queue.append(nk)
        return len(visited) == N


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    s = Solution()
    act = s.canVisitAllRooms(rooms)
    print(act)
