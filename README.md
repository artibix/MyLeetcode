## [1] 两数之和

算法启蒙，第一次了解 hash 表的强大之处

## [2] 两数相加

我的思路很简单，将链表转成数字再相加得到和，再把和转成链表，空间和时间复杂度都很感人。

官方解释就是链表不对称的补 0，将每个数相加余 10 得到需要存储的数字和 carry。

## [3] 无重复字符的最长子串

稀里糊涂做出来的，最后把我的代码给 chatgpt 优化就好看多了；整体思想也是利用了 **滑动窗口 + 链表**，也从 K 神哪里看到了动态规划解法，比较难，后面的题用到再深入。

## [4] 寻找两个正序数组的中位数

第一眼想到的是遍历数组然后存在二进制里面，再遍历二进制的一半得到中位数；不好写，然后就直接合并数组 sort，看题解还有两种解法，一个是二分法，一个根据中位数的定义划分得到中位数，后面两个时间复杂度是 log(m+n)。

## [1480] 一维数组的动态和

列表推导式一步到位

## [2288] 价格减免

python 解起来还是比较简单，思路和官方差不多，让 ai 优化代码变成一行，但是没跑出来

## [2713] 矩阵中严格递增的单元格数

这题真的难，考虑了很多最终还是去找题解了，只看到动态规划的解法

## [520] 检测大写字母

用 python 非常简单

## [503] 下一个更大元素 II

我的思路：双循环，官解：拉长列表 + 单调栈