#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

from typing import List
import unittest
# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for head in range(len(nums)-3):
            head_num = nums[head]
            if head > 0 and head_num == nums[head - 1]:
                continue
            for tail in range(len(nums) - 1, 2 + head, -1):
                tail_num = nums[tail]
                if tail < len(nums) - 1 and tail_num == nums[tail+1]:
                    continue
                l, r = head + 1, tail - 1
                while l < r:
                    s = head_num + tail_num + nums[l] + nums[r]
                    if s == target:
                        ans.append([head_num, tail_num, nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return ans
# @lc code=end

# unit test


class SolutionTest(unittest.TestCase):
    def test_1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        self.assertEqual([[-2, 2, -1, 1], [-2, 2, 0, 0], [-1, 1, 0, 0]],
                         Solution().fourSum(nums, target))

    def test_2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        self.assertEqual([[2, 2, 2, 2]], Solution().fourSum(nums, target))

    def test_3(self):
        nums = [-3, -1, 0, 2, 4, 5]
        target = 0
        self.assertEqual([[-3, 4, -1, 0]], Solution().fourSum(nums, target))

    def test_4(self):
        nums = [-2, -1, -1, 1, 1, 2, 2]
        target = 0
        self.assertEqual([[-2, 2, -1, 1], [-1, 1, -1, 1]],
                         Solution().fourSum(nums, target))


if __name__ == '__main__':
    unittest.main()
