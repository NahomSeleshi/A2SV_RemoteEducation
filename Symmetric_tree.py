# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_queue = deque([root.left])
        right_queue = deque([root.right])

        while left_queue and right_queue:
            left = left_queue.popleft()
            right = right_queue.popleft()

            if left and right and left.val != right.val:
                return False
                
            if left or right:
                
                if (left and not right) or (right and not left):
                    return False
                
                left_queue.append(left.right)
                left_queue.append(left.left)
                right_queue.append(right.left)
                right_queue.append(right.right)
        
        return True