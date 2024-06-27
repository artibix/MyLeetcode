#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#
from typing import List

# @lc code=start


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = 0
        for l in range(len(nums)):
            r = l+1
            while r < len(nums):
                s = nums[l] + nums[r]
                if s < target:
                    n += 1
                    r += 1
                else:
                    break
        return n
# @lc code=end
