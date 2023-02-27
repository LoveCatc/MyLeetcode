#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        rslt = None
        def trav(node):
            nonlocal counter, rslt
            if node is None:
                return 
            trav(node.left)
            counter += 1
            if counter == k:
                rslt = node.val
            trav(node.right)
        trav(root)
        return rslt
# @lc code=end

