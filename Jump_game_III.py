class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        queue = deque([start])
        visited_indices = set([start])

        while queue:
            cur_index = queue.popleft()
            if arr[cur_index] == 0:
                return True

            left_jump, right_jump = cur_index - arr[cur_index], cur_index + arr[cur_index]

            if left_jump >= 0 and left_jump not in visited_indices:
                queue.append(left_jump)
                visited_indices.add(left_jump)

            if right_jump < len(arr) and right_jump not in visited_indices:
                queue.append(right_jump)
                visited_indices.add(right_jump)

        return False

