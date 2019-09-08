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


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = Solution.get_list_val(l1)
        v2 = Solution.get_list_val(l2)
        t = v1 + v2
        return Solution.box_into_list(t)

    @staticmethod
    def get_list_val(list_head: ListNode) -> int:
        ptr = list_head
        numbers = []
        while ptr:
            numbers.append(ptr.val)
            ptr = ptr.next

        nums_len = len(numbers)
        the_sum = 0
        for i in range(nums_len):
            the_sum += numbers[i] * (10 ** i)
        return the_sum

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
            ptr.next = ListNode(num)
            ptr = ptr.next

        return head
