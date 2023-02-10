# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(cur_sum, node):
            
            cur_sum += node.val
            if cur_sum == targetSum and not node.left and not node.right:
                return True
            
            left = dfs(cur_sum, node.left) if node.left else False
            right = dfs(cur_sum, node.right) if node.right else False
            
            return left or right
            
        return dfs(0, root) if root else False