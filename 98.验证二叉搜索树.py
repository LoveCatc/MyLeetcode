#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rslt = []
        def trav(node):
            nonlocal rslt
            if node is None:
                return
            trav(node.left)
            rslt.append(node.val)
            trav(node.right)
        trav(root)
        prediff = [rslt[i]-rslt[i-1] for i in range(1, len(rslt))]
        # print(rslt, prediff)
        for _ in prediff:
            if _ <= 0:
                return False
        return True
            
# @lc code=end

