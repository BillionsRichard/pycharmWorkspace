# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/17 9:08
"""
import heapq


class LRUCache:
    def __init__(self, capacity: int):
        self.cache_list = []  # (times,key,value)
        self.time_unit = 0
        self.capacity = capacity
        self.query_cache = []  # [time, key, value]

    def get(self, key: int) -> int:
        self.time_unit += 1

        t_k_v = heapq.nlargest(1, self.cache_list)
        if t_k_v and t_k_v[1] == key:
            t_k_v[0] = self.time_unit + 1
            return

        for tkv_list in self.cache_list:
            # k in cache, update time.
            if tkv_list[1] == key:
                tkv_list[0] = self.time_unit
                heapq.heapify(self.cache_list)
                self.query_cache = (self.time_unit-1, )
                return tkv_list[2]

        return -1

    def put(self, key: int, value: int) -> None:
        self.time_unit += 1

        for tkv_list in self.cache_list:
            # k in cache, update time and value.
            if tkv_list[1] == key:
                tkv_list[0] = self.time_unit
                tkv_list[2] = value
                heapq.heapify(self.cache_list)
                return

        # k not in cache
        # not full
        if len(self.cache_list) < self.capacity:
            t_k_v = [self.time_unit, key, value]
            heapq.heappush(self.cache_list, t_k_v)
            return
        # full, replace lru key.
        heapq.heapreplace(self.cache_list, [self.time_unit, key, value])
        return

