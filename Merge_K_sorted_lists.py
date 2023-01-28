# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapify(min_heap)
        for head in lists:
            while head:
                heappush(min_heap, head.val)
                head = head.next
                
        answer = ListNode()
        walk_answer = answer
        while min_heap:
            walk_answer.next = ListNode(heappop(min_heap))
            walk_answer = walk_answer.next

        return answer.next