#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n+1)]
        val = [0 for _ in range(n+1)]
        for b in bookings:
            diff[b[0]] += b[2]
            if b[1] + 1 <= n:
                diff[b[1]+1] -= b[2]
        for i in range(n):
            val[i+1] = val[i] + diff[i+1]
        return val[1:]
# @lc code=end

