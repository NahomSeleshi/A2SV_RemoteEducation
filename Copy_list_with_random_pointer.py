"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        walk_head = head
        while walk_head:
            walk_head_copy = Node(walk_head.val)
            nodes[walk_head] = walk_head_copy
            walk_head = walk_head.next
        
        walk_head_2 = head
        while walk_head_2:
            nodes[walk_head_2].next = nodes[walk_head_2.next]
            nodes[walk_head_2].random = nodes[walk_head_2.random]
            walk_head_2 = walk_head_2.next
        
        return nodes[head]

