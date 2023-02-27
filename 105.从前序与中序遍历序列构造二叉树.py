#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def grow(preorder, inorder):
            if not preorder:
                return None
            rootval = preorder[0]
            rootidx = inorder.index(rootval)
            
            inorderLeft = inorder[:rootidx]
            inorderRight = inorder[rootidx+1:]
            preorderLeft = preorder[1:rootidx+1]
            preorderRight = preorder[rootidx+1:]

            root = TreeNode(val=rootval)
            left = grow(preorderLeft, inorderLeft)
            right = grow(preorderRight, inorderRight)
            root.left = left
            root.right = right
            return root
        return grow(preorder, inorder)
# @lc code=end

