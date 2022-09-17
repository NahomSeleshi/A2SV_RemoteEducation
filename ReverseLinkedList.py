# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.answer = ListNode
        if not head:
            return None
        def dfs(node):
            if not node.next:
                self.answer.next = node
                return node
            curNode = dfs(node.next)
            curNode.next = node
            return node
        temp = dfs(head)
        temp.next = None
        return self.answer.next