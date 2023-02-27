#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        allTrees = []
        rslt = []
        def isSameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return isSameTree(node1.left, node2.left) \
                    and isSameTree(node1.right, node2.right)
            
        def trav(node):
            if node is None:
                return 
            nonlocal allTrees, rslt
            rsltFlag = False
            for n in allTrees:
                if not n.val == node.val:
                    continue
                else:
                    if isSameTree(n, node):
                        rsltFlag = True
                        inRsltFlag = False
                        for _ in rslt:
                            if isSameTree(node, _):
                                inRsltFlag = True
                        # print(node, inRsltFlag)
                        if not inRsltFlag:
                            rslt.append(node)
            if not rsltFlag:
                allTrees.append(node)
            
            trav(node.left)
            trav(node.right)
        trav(root)
        return rslt

# @lc code=end

