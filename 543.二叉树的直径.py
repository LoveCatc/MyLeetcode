#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        rslt = 0
        def depthOfNode(node):
            if node is None:
                return -1
            leftdep = depthOfNode(node.left)+1
            rightdep = depthOfNode(node.right)+1
            return max(leftdep, rightdep) 
        def trav(root):
            nonlocal rslt
            if root is None:
                return
            if depthOfNode(root.left) + depthOfNode(root.right) + 2 > rslt:
                rslt = depthOfNode(root.left) + depthOfNode(root.right) + 2
            trav(root.left)
            trav(root.right)
        trav(root)
        return rslt
# @lc code=end

