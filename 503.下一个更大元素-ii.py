#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
from typing import List


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         new_list = []
#         for index, num in enumerate(nums):
#             nf = 0
#             f2 = False
#             if index == length - 1:
#                 nf = nf + 1
#             if index == 0:
#                 nf = nf + 1

#             for i in range(index + 1, length):
#                 if nums[i] > num:
#                     new_list.append(nums[i])
#                     f2 = True
#                     break
#                 if i == length - 1:
#                     nf = nf + 1
#             if f2:
#                 continue

#             for i in range(0, index):
#                 if nums[i] > num:
#                     new_list.append(nums[i])
#                     break
#                 if i == index - 1:
#                     nf = nf + 1

#             if nf == 2:
#                 new_list.append(-1)
#                 nf = 0

#         return new_list

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/next-greater-element-ii/solutions/637573/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode-bwam/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end
