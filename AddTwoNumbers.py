# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        temp = answer
        remainder = 0
        while l1 and l2:
            curSum = l1.val + l2.val + remainder
            curAnswer = curSum % 10
            remainder = int(str(curSum)[0]) if curSum > 9 else 0
            temp.next = ListNode(curAnswer)
            temp = temp.next
            l1,l2 = l1.next, l2.next
        if l1:
            while l1:
                curSum = l1.val + remainder
                curAnswer = curSum % 10
                remainder = int(str(curSum)[0]) if curSum > 9 else 0
                temp.next = ListNode(curAnswer)
                temp = temp.next
                l1 = l1.next
        else:
            while l2:
                curSum = l2.val + remainder
                curAnswer = curSum % 10
                remainder = int(str(curSum)[0]) if curSum > 9 else 0
                temp.next = ListNode(curAnswer)
                temp = temp.next
                l2 = l2.next
        if remainder > 0:
            temp.next = ListNode(remainder)
        return answer.next