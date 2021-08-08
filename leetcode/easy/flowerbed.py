# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2021/1/1 22:54
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_cnt = flowerbed.count(1)
        N = len(flowerbed)
        for idx, ele in enumerate(flowerbed):
            if ele == 1:
                continue

            if idx == 0 and idx + 1 < N and flowerbed[idx + 1] == 0:
                flowerbed[0] = 1
                continue

            if flowerbed[idx - 1] == 0 and idx + 1 < N and flowerbed[
                idx + 1] == 0:
                flowerbed[idx] = 1
                continue

        print(flowerbed)
        return flowerbed.count(1) - flower_cnt >= n


if __name__ == '__main__':
    s = Solution()
    l = [0,0,1,0,1]
    n = 1
    print(s.canPlaceFlowers(l, 1))