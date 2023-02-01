# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        averages = []
        
        while queue:
            cur_sum, queue_length = 0, len(queue)
            for i in range(len(queue)):
                cur_node = queue.popleft()
                cur_sum += cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            averages.append(cur_sum / queue_length)
        
        return averages