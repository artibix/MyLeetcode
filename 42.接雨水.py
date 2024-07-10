#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

from typing import List
import unittest

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
# @lc code=end

# unit test


class SolutionTest(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
