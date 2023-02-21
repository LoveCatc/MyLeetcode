#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = q = dummy
        former = q
        q = q.next
        while q is not None:
            if q.val < x:
                former.next = q.next
                q.next = p.next
                p.next = q
                p = p.next
                q = former.next
                if q == p:
                    former = q
                    q = q.next
            else:
                former = q
                q = q.next
        return dummy.next

# @lc code=end

