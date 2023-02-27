#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def grow(inorder, postorder):
            if not postorder:
                return None
            rootval = postorder[-1]
            rootidx = inorder.index(rootval)

            inorderLeft = inorder[:rootidx]
            inorderRight = inorder[rootidx+1:]
            postorderLeft = postorder[:rootidx]
            postorderRight = postorder[rootidx:-1]

            root = TreeNode(val=rootval)
            left = grow(inorderLeft, postorderLeft)
            right = grow(inorderRight, postorderRight)
            root.left = left
            root.right = right
            return root
        return grow(inorder, postorder)
# @lc code=end

