#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        num = 0
        diff = dict()
        for L in trips:
            diff[L[1]] = diff.get(L[1], 0) + L[0]
            diff[L[2]] = diff.get(L[2], 0) - L[0]
        # print(diff)
        sortDiff = sorted(diff.items(), key=lambda x:x[0])
        for p in sortDiff:
            num += p[1]
            if num > capacity:
                return False
        return True
# @lc code=end

