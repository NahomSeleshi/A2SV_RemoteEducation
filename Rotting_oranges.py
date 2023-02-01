class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rot_queue = deque([])
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rot_queue.append([row, col])

        min_minutes = 0
        while rot_queue:
            for i in range(len(rot_queue)):
                cur_row, cur_col = rot_queue.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    new_row, new_col = cur_row + dx, cur_col + dy
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        rot_queue.append([new_row, new_col])
            min_minutes += 1

        # if we find a fresh orange after all the rotten oranges infect the possible fresh oranges, we return -1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1

        return min_minutes - 1 if min_minutes != 0 else 0
