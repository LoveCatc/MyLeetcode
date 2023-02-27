#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def trav(node, parentVal):
        #     if node is None:
        #         return parentVal
        #     rightval = trav(node.right, parentVal)
        #     if node.val >= 0:
        #         node.val = node.val + max(parentVal, rightval)
        #     else:
        #         node.val = node.val + min(parentVal, rightval)
        #     leftval = trav(node.left, node.val)
        #     return max(leftval, node.val)
        def trav(node, parentVal):
            if node is None:
                return parentVal
            # traverse to rightest node
            rightVal = trav(node.right, parentVal)
            # update the value of current node
            if node.right is not None:
                # a node is updated by itself and its right son trees
                node.val = rightVal + node.val
            else:
                # if no right son trees, using parent info to update
                node.val = node.val + parentVal
            # now traverse to left nodes
            leftVal = trav(node.left, node.val)

            return leftVal  # note here 
        

        if root is None:
            return None

        dummy = TreeNode(val = 0)
        dummy.right = root
        trav(dummy.right, 0)
        return dummy.right
            
# @lc code=end

