#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        rsltTable = [1 for _ in range(20)]

        def growBST(left, right):
            nonlocal rsltTable
            return rsltTable[len(left)] * rsltTable[len(right)]
        
        i = 2
        while i <= n:
            nodes = [_+1 for _ in range(i)]
            rslt = 0
            for idx, node in enumerate(nodes):
                rslt += growBST(nodes[:idx], nodes[idx+1:])
                # print(rslt)
            rsltTable[i] = rslt
            i += 1
        # print(rsltTable)
        return rsltTable[n]


# @lc code=end

