# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site: 
@software: PyCharm
@time: 2019/11/17 17:55
"""
from collections import OrderedDict


class LFUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
            self[key] = value
            return

        # key not in dict
        if len(self) < self.capacity:
            self[key] = value
            return

        self.popitem(last=False)
        self[key] = value
        return

    # Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
