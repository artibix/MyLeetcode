#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


# my solution 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3: Optional[ListNode] = ListNode(0)
        l1_num: int = 0
        l2_num: int = 0

        # 循环待优化
        for i in range(0, 100):
            l1_num += l1.val * 10**i
            l1 = l1.next
            if l1 == None:
                break

        for i in range(0, 100):
            l1_num += l2.val * 10**i
            l2 = l2.next
            if l2 == None:
                break

        l3_num = l1_num + l2_num
        l3_str = str(l3_num)
        l3_str_reversed = l3_str[::-1]
        current = l3
        for char in l3_str_reversed:
            current.next = ListNode(int(char))
            current = current.next
        return l3.next

# the bast vote solution

# class Solution:
#     # @return a ListNode
#     def addTwoNumbers(self, l1, l2):
#         carry = 0
#         root = n = ListNode(0)
#         while l1 or l2 or carry:
#             v1 = v2 = 0
#             if l1:
#                 v1 = l1.val
#                 l1 = l1.next
#             if l2:
#                 v2 = l2.val
#                 l2 = l2.next
#             carry, val = divmod(v1+v2+carry, 10)
#             n.next = ListNode(val)
#             n = n.next
#         return root.next

# @lc code=end
