#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

from typing import List
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(nlogn)
        ans = []
        for i in range(len(nums)-2):  # O(n)
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            # 优化一
            if x + nums[i+1] + nums[i+2] > 0:
                break
            # 优化二
            if x + nums[-1] + nums[-2] < 0:
                continue
            l, r = i+1, len(nums)-1
            while l < r:  # O(n)
                s = x + nums[l] + nums[r]
                if s == 0:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return ans
# @lc code=end
