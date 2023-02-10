# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.tilt = 0
        def dfs(node):
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            self.tilt += abs(left - right)

            return left + right + node.val
        dfs(root)
        return self.tilt