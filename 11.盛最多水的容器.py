#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
import unittest

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            s = min(height[left], height[right]) * (right - left)
            ans = max(ans, s)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
# @lc code=end

# unit test


class SolutionTest(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(1, s.maxArea([1, 1]))

    def test_2(self):
        s = Solution()
        self.assertEqual(49, s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    unittest.main()
