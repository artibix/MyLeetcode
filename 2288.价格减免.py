#
# @lc app=leetcode.cn id=2288 lang=python3
#
# [2288] 价格减免
#

# @lc code=start
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        new_words = []
        for word in words:
            if word[0] == '$' and word[1:].isdigit():
                word = '$' + \
                    f"{(float(word.strip('$')) * (100 -discount) / 100):.2f}"
                new_words.append(word)
            else:
                new_words.append(word)

        return str.join(' ', new_words)

# @lc code=end
