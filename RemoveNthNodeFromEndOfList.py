# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        listLength = 0
        while temp:
            listLength += 1
            temp = temp.next
        if listLength == n:
            return head.next
        preDeletion = 1
        temp1 = head
        while preDeletion < listLength-n:
            preDeletion += 1
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return head