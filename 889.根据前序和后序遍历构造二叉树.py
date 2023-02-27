#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def grow(preorder, postorder):
            if not preorder:
                return None
            if len(preorder) == 1:
                return TreeNode(val=preorder[0])
            rootval = preorder[0]
            leftval = preorder[1]
            leftidx = postorder.index(leftval)

            postorderLeft = postorder[:leftidx+1]
            postorderRight = postorder[leftidx+1:-1]
            preorderLeft = preorder[1:leftidx+2]
            preorderRight = preorder[leftidx+2:]

            root = TreeNode(val=rootval)
            left = grow(preorderLeft, postorderLeft)
            right = grow(preorderRight, postorderRight)
            root.left = left
            root.right = right
            return root
        return grow(preorder, postorder)

# @lc code=end

