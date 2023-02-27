#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def growBST(low, high):
            # print(low, high)
            rslt = []
            if low > high:
                return [None]
            # elif low == high:
            #     rslt.append(TreeNode(val=low))  
            else:
                for rootval in range(low, high+1):
                    left = growBST(low, rootval-1)
                    right = growBST(rootval+1, high)
                    for _ in left:
                        for __ in right:
                            root = TreeNode(val=rootval)
                            root.left = _
                            root.right = __
                            rslt.append(root)
            # print(rslt)
            return rslt
        return growBST(1, n)
# @lc code=end

