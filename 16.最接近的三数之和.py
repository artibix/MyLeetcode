#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

from typing import List
import unittest
# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        near: int = 0x7fffffff
        sum: int = 0
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                d = abs(target-s)
                if s < target:
                    if d < near:
                        sum = s
                        near = d
                    l += 1
                elif s > target:
                    if d < near:
                        sum = s
                        near = d
                    r -= 1
                else:
                    return s
        return sum
# @lc code=end

# unit test

class SolutionTest(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.threeSumClosest([-1, 0, 1, 1, 55], 3))

    def test_2(self):
        s = Solution()
        self.assertEqual(0, s.threeSumClosest([0, 0, 0], 1))

    def test_3(self):
        s = Solution()
        self.assertEqual(2, s.threeSumClosest([1, 1, 1, 0], -100))

    def test_4(self):
        s = Solution()
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], 3))


if __name__ == "__main__":
    unittest.main()
