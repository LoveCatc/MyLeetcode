#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def str2dict(x: str) -> dict:
            d = dict()
            for _ in x:
                d[_] = d.get(_, 0) + 1
            return d
        def isDiffWord(x: dict, y:dict)->bool:
            for _ in x.keys():
                if x[_] != y.get(_, 0):
                    return False
            return True
        
        if len(p) > len(s):
            return []
        
        left = 0
        right = len(p)
        rslt = []
        sdict = str2dict(s[left:right])
        pdict = str2dict(p)
        while right <= len(s):
            # print(window)
            if isDiffWord(pdict, sdict):
                rslt.append(left)
            # print(left, right, sdict)
            sdict[s[left]] -= 1
            left += 1
            if right == len(s):
                break
            sdict[s[right]] = sdict.get(s[right], 0) + 1
            right += 1
        return rslt

# @lc code=end

