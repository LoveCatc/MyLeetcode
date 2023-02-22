#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = [[m[i] for m in matrix] for i in range(len(matrix))]
        # print(matrix)
        # matrix = [_[::-1] for _ in matrix]
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][-(j+1)]
                matrix[i][-(j+1)] = tmp
# @lc code=end

