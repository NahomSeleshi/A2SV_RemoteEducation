# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, comp = head, head
        while comp:
            if cur.val == comp.val:
                comp = comp.next
            else:
                cur.next = comp
                cur = cur.next
                comp = comp.next
        if cur:
            cur.next = None
        return head