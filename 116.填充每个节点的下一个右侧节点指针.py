#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def levelTraverse(root):
            if root is None:
                return [None, ]
            q = [root, ]
            rslt = []
            while q:
                cur = q.pop(0)
                rslt.append(cur)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            return rslt
        j = 1
        rslt = levelTraverse(root)
        print([_.val if _ else None for _ in rslt])
        for idx, node in enumerate(rslt):
            if idx == 2**j - 2:
                j += 1
            else:
                rslt[idx].next = rslt[idx+1]        
        return root
# @lc code=end

