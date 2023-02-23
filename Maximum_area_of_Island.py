class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.find_area(row, col, grid))
        return max_area

    def find_area(self, row, col, grid):
        if grid[row][col] == 0:
            return 0
        cur_area = 1
        grid[row][col] = 0
        for dr, dc in [[1,0], [-1,0], [0,1], [0, -1]]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                cur_area += self.find_area(new_row, new_col, grid)
        return cur_area
