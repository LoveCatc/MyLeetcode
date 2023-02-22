#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        upper = 0
        lower = n-1
        left = 0
        right = n-1
        rslt = [[0 for _ in range(n)] for __ in range(n)]
        counter = 1
        i = 0
        j = 0
        while counter <= n*n:
            if counter <= n*n:
                for j in range(left, right+1, 1):
                    rslt[i][j] = counter
                    counter += 1
                upper += 1
            if counter <= n*n:
                for i in range(upper, lower+1, 1):
                    rslt[i][j] = counter
                    counter += 1
                right -= 1
            if counter <= n*n:
                for j in range(right, left-1, -1):
                    rslt[i][j] = counter
                    counter += 1
                lower -= 1
            if counter <= n*n:
                for i in range(lower, upper-1, -1):
                    rslt[i][j] = counter
                    counter += 1
                left += 1
        return rslt

# @lc code=end

