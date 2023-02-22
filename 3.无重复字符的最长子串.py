#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            print(left, right)
            if len(s[left:right+1]) == len(list(set(s[left:right+1]))):
                longest = max(longest, right-left+1)
                right += 1
            else:
                left += 1

        return longest


# @lc code=end

