# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        zigzag_traversal = []
        direction = "LR" # this tells us to go from left to right or right to left
        
        while queue:

            children = []
            for i in range(len(queue)):

                cur_node = queue.popleft()
                children.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

            if direction == "LR":
                zigzag_traversal.append(children)
            else:
                zigzag_traversal.append(children[::-1])

            direction = "RL" if direction == "LR" else "LR"

        return zigzag_traversal
                