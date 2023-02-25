# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return sum(self.dfs(root, None, None, []))

    def dfs(self, node, parent, grand_parent, nodes):
        if not node:
            return 
        if grand_parent and grand_parent.val % 2 == 0:
            nodes.append(node.val)
        self.dfs(node.left, node, parent, nodes)
        self.dfs(node.right, node, parent, nodes)
        return nodes