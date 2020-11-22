# encoding: utf-8

"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4-> 5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        node_list = []
        node_ptr = head
        while node_ptr:
            node_list.append(node_ptr)
            node_ptr = node_ptr.next

        return node_list[-k]

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head
        for _ in range(k):
            if not fast:
                break

            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

    @staticmethod
    def print_list(head: ListNode):
        p = head
        while p:
            print(p.val)
            p = p.next


if __name__ == "__main__":
    s = Solution()
    h = ListNode(5)
    n4 = ListNode(4)
    h.next = n4
    n4.next = ListNode(10)

    h1 = s.getKthFromEnd2(h, 3)
    s.print_list(h1)
