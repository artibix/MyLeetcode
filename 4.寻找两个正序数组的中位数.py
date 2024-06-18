#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start

import math
from typing import List


class Solution:
    ###   answer 1  ###
    # 2094/2094 cases passed (32 ms)
    # Your runtime beats 98.33 % of python3 submissions
    # Your memory usage beats 14.7 % of python3 submissions (16.8 MB)
    ###################

    def custom_round(self, n):
        if n - math.floor(n) < 0.5:
            return math.floor(n)
        else:
            return math.ceil(n)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        l = len(n)
        if l % 2 == 0:
            i1 = self.custom_round(l/2)
            i2 = self.custom_round(i1 + 1)
            return (n[i1-1] + n[i2-1]) / 2
        else:
            i = self.custom_round(l/2)
            return n[i-1]

# TODO：二分法
# @lc code=end
