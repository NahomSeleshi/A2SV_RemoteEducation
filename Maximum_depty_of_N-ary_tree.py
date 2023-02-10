"""
# Definition for a Node."""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(cur_height, node):
            if not node:
                return cur_height
                
            cur_height += 1
            max_height = cur_height
            if node.children:
                for each_child in node.children:
                    max_height = max(max_height, dfs(cur_height, each_child))

            return max_height
        
        return dfs(0, root) if root else 0
