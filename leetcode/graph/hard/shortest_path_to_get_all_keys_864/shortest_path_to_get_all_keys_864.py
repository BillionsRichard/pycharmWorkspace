# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/1/5 12:24
"""
from typing import List
from collections import defaultdict
from collections import deque
from collections import namedtuple


class Solution:
    """
    示例 1：

    输入：[
            "@.a.#",
            "###.#",
            "b.A.B"]
    输出：8
    示例 2：

    输入：["@..aA",
          "..B#.",
          "....b"]
    输出：6
    """

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        def is_lock(ch: str) -> bool:
            return "A" <= ch <= "Z"

        def is_key(ch: str) -> bool:
            return "a" <= ch <= "z"

        def is_room(ch: str) -> bool:
            return ch == "."

        def is_wall(ch: str) -> bool:
            return ch == "#"

        def is_start_point(ch: str) -> bool:
            return ch == "@"

        def is_can_walk(x, y, ks):
            return (
                x in range(m)
                and y in range(n)
                and (
                    is_room(grid[x][y])
                    or is_start_point(grid[x][y])
                    or is_key(grid[x][y])
                    or (is_lock(grid[x][y]) and grid[x][y].lower() in ks)
                )
            )

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        start_pt = None
        K = 0
        for i in range(m):
            for j in range(n):
                if is_start_point(grid[i][j]):
                    start_pt = (i, j)
                elif is_key(grid[i][j]):
                    K += 1

        NodeState = namedtuple(
            "NodeState", field_names=["x", "y", "ks", "step"]
        )
        start_state = NodeState(start_pt[0], start_pt[1], "", 0)
        visited_state = defaultdict(bool)
        visited_state[(start_pt[0], start_pt[1], "")] = True
        access_queue = deque([start_state])

        while access_queue:
            state = access_queue.popleft()
            if len(state.ks) == K:
                return state.step

            for d in range(4):
                nx, ny = state.x + dx[d], state.y + dy[d]
                nks = list(state.ks)

                if is_can_walk(nx, ny, state.ks):
                    nchar = grid[nx][ny]
                    if is_key(nchar) and nchar not in nks:
                        nks.append(nchar)

                    nks_str = "".join(sorted(nks))
                    if visited_state[(nx, ny, nks_str)]:
                        continue

                    visited_state[(nx, ny, nks_str)] = True
                    nstart = NodeState(nx, ny, nks_str, state.step + 1)
                    access_queue.append(nstart)

        return -1


if __name__ == "__main__":
    grid = ["@.a.#", "###.#", "b.A.B"]
    s = Solution()
    # print(s.shortestPathAllKeys(grid))
    # grid = [
    #     "@..aA",
    #     "..B#.",
    #     "....b"]
    # print(s.shortestPathAllKeys(grid))
    # grid = ["@...a",
    #         ".###A",
    #         "b.BCc"]
    grid = ["@...a", ".###A", "b.BCc"]
    print(s.shortestPathAllKeys(grid))
