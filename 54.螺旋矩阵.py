#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper = 0
        lower = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        i = 0
        j = 0
        rslt = []
        while len(rslt) < len(matrix) * len(matrix[0]):
            for j in range(left, right+1, 1):
                rslt.append(matrix[i][j])
            upper += 1
            if len(rslt) >= len(matrix) * len(matrix[0]):
                break
            for i in range(upper, lower+1, 1):
                rslt.append(matrix[i][j])
            right -= 1
            if len(rslt) >= len(matrix) * len(matrix[0]):
                break
            for j in range(right, left-1, -1):
                rslt.append(matrix[i][j])
            lower -= 1
            if len(rslt) >= len(matrix) * len(matrix[0]):
                break
            for i in range(lower, upper-1, -1):
                rslt.append(matrix[i][j])
            left += 1
            if len(rslt) >= len(matrix) * len(matrix[0]):
                break

        return rslt
# @lc code=end

