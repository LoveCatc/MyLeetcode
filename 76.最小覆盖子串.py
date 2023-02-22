#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def str2dict(x: str) -> dict:
            d = dict()
            for _ in x:
                d[_] = d.get(_, 0) + 1
            return d
        def cmpdict(x:dict, y:dict) -> bool:
            for _ in x.keys():
                if x[_] > y.get(_, 0):
                    return False
            return True
        
        tdict = str2dict(t)
        left = 0
        right = 0
        shortest = len(s)
        shortstr = ""

        while right < len(s):
            # print(left, right)
            sdict = str2dict(s[left:right+1])
            if not cmpdict(tdict, sdict):
                right += 1
            else:
                if shortest > right-left+1:
                    shortest = right-left+1
                    shortstr = s[left:right+1]
                left += 1
        return shortstr
        

# @lc code=end

