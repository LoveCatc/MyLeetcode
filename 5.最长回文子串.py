#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        rslt = s[0]
        def findPalin1(s, idx):
            rslt = s[idx]
            i = 0
            while idx-i >=0 and idx+i<len(s):
                if s[idx-i] == s[idx+i]:
                    rslt = s[idx-i:idx+i+1]
                    i+=1
                else:
                    break
            return rslt
        def findPalin2(s, idx):
            rslt = s[idx]
            i = 0
            while idx-i >=0 and idx+i+1<len(s):
                if s[idx-i] == s[idx+i+1]:
                    rslt = s[idx-i:idx+i+2]
                    i+=1
                else:
                    break
            return rslt
        for i in range(len(s)):
            tmp1 = findPalin1(s, i)
            tmp2 = findPalin2(s, i)
            if len(rslt) > len(tmp1) and len(rslt) > len(tmp2):
                pass
            if len(tmp1) > len(tmp2) and len(tmp1) > len(rslt):
                rslt = tmp1
            if len(tmp2) > len(tmp1) and len(tmp2) > len(rslt):
                rslt = tmp2
            # print(rslt, tmp1, tmp2)
        return rslt
# @lc code=end

