#
# @lc app=leetcode.cn id=2713 lang=python3
#
# [2713] 矩阵中严格递增的单元格数
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置
        g = sorted(g.items(), key=lambda p: p[0])
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in g:
            # 先把所有 f 值都算出来，再更新 row_max 和 col_max
            fs = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            for (i, j), f in zip(pos, fs):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return max(row_max)


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/solutions/2286920/dong-tai-gui-hua-you-hua-pythonjavacgo-b-axv0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end
