#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = []
        def trav(node):
            if node is None:
                return
            nonlocal q
            q.append(node)
            trav(node.left)
            trav(node.right)
        trav(root)
        for idx, n in enumerate(q):
            if idx == len(q)-1:
                break
            q[idx].left = None
            q[idx].right = q[idx+1]           
# @lc code=end

