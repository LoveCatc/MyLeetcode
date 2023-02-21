#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sumMatrix = [[None for __ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.sumMatrix[0][0] = self.matrix[0][0]
                elif i == 0 and j != 0:
                    self.sumMatrix[0][j] = self.sumMatrix[0][j-1] + self.matrix[0][j]
                elif j == 0 and i != 0:
                    self.sumMatrix[i][0] = self.sumMatrix[i-1][0] + self.matrix[i][0]
                else:
                    self.sumMatrix[i][j] = self.matrix[i][j] + self.sumMatrix[i-1][j] + self.sumMatrix[i][j-1] - self.sumMatrix[i-1][j-1]
        # print(self.sumMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.sumMatrix[row2][col2]
        elif row1 == 0 and col1 != 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1]
        elif col1 == 0 and row1 != 0:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row1-1][col2]
        else:
            return self.sumMatrix[row2][col2] - self.sumMatrix[row2][col1-1] - self.sumMatrix[row1-1][col2] + self.sumMatrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

