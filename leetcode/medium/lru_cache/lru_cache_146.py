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
        self.cache_list = []  # (times,key)
        self.cache_dict = {}  # k v
        self.time_unit = 0
        self.capacity = capacity

    def get(self, key: int) -> int:

        self.time_unit += 1
        if key in self.cache_dict:
            for tk in self.cache_list:
                if tk[1] == key:
                    tk[0] = self.time_unit
                    heapq.heapify(self.cache_list)
                    return self.cache_dict.get(key)

        return -1

    def put(self, key: int, value: int) -> None:
        self.time_unit += 1

        if key not in self.cache_dict:
            # not full
            if len(self.cache_dict) < self.capacity:
                self.cache_dict[key] = value
                heapq.heappush(self.cache_list, [self.time_unit, key])
                return

            _,old_key = heapq.heapreplace(heapq, [self.time_unit, key])
            self.cache_dict.pop(old_key)
            self.cache_dict[key] = value
            return

        # in dict, update directly
        self.cache_dict[key] = value
        for tk in self.cache_list:
            if tk[1] == key:
                tk[0] = self.time_unit
                heapq.heapify(self.cache_list)
                return
