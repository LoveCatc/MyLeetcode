#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def grow(nums):
            if not nums:
                return None
            # print(nums)
            maxp = max(nums)
            maxpidx = nums.index(maxp)
            leftnums = nums[:maxpidx]
            rightnums = nums[maxpidx+1:]
            node = TreeNode(val=maxp)
            node.left = grow(leftnums)
            node.right = grow(rightnums)
            return node
        root = grow(nums)
        return root
# @lc code=end

