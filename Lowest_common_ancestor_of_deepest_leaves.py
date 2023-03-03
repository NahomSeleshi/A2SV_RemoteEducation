# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return 0, None
            height_l, lowest_comn_l = helper(node.left)
            height_r, lowest_comn_r = helper(node.right)
            if height_l > height_r:
                return height_l + 1, lowest_comn_l
            if height_r > height_l:
                return height_r + 1, lowest_comn_r
            return height_r + 1, node
        return helper(root)[1]





