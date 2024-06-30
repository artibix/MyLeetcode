#
# @lc app=leetcode.cn id=2741 lang=python3
#
# [2741] 特别的排列
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = 0
        # all = list(itertools.permutations(nums))
        # for a in all:
        #     for i in range(0, len(a)-1):
        #         if a[i] % a[i+1] != 0 and a[i+1] % a[i] != 0:
        #             break
        #         if i == len(a)-2:
        #             n = n+1
        filter_two = []
        for count in range(len(nums)-1):
            if len(filter_two) != 0:
                nums = filter_two
                filter_two = []
            twos = list(itertools.combinations(nums, 2))
            if count != 0:
                for t in twos:
                    combined_list = [element for tup in t for element in tup]
                    combined_list = set(combined_list)
                    print(combined_list)
            for two in twos:
                for i in range(0, len(two)-1):
                    if two[i] % two[i+1] != 0 and two[i+1] % two[i] != 0:
                        filter_two.append(two)
            print(filter_two)
        # for count in range(len(nums)):
        #     l = []
        #     for num, i in enumerate(nums):
        #         if nums[i] % nums[i+1] != 0 and nums[i+1] % nums[i] != 0:
        #             l.append(num)
        return n % (10**9 + 7)


# test
nums = [12, 24, 96, 32, 64, 16, 48, 8, 56, 7]
print(Solution().specialPerm(nums))
# @lc code=end
