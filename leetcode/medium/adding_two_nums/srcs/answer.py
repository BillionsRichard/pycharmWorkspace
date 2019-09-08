# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/9/1 11:07 
"""
from pprint import pprint as pp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self._val_list = None

    def append(self, new_node):
        self.next = new_node
        return new_node

    def __iter__(self):
        self._collect_vals()
        return iter(self._val_list)

    def _collect_vals(self):
        self._val_list = [self.val]
        ptr = self.next
        while ptr:
            self._val_list.append(ptr.val)
            ptr = ptr.next

    def __eq__(self, other):
        return self.get_list_value() == other.get_list_value()

    @staticmethod
    def box_into_list(num: int):
        if num < 0:
            raise Exception('Must be non-negative numbers.')
        if num < 10:
            return ListNode(num)

        numbers = []
        while num > 0:
            numbers.append(num % 10)
            num = num // 10

        head = ListNode(numbers[0])
        ptr = head
        for num in numbers[1:]:
            ptr = ptr.append(ListNode(num))

        return head


def get_list_value(list_head) -> int:
    nums = [val for val in list_head]
    nums_len = len(nums)
    sum = 0
    for i in range(nums_len):
        sum += nums[i] * (10 ** i)
    return sum


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = get_list_value(l1)
        v2 = get_list_value(l2)
        t = v1 + v2
        return ListNode.box_into_list(t)
