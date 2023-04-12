class Solution:
    def give_min_option(self, row:int, col:int, memo:dict, grid:List[List[int]]):
        if row >= len(grid) or col >= len(grid[0]):
            return inf
        
        if memo[(row, col)]:
            return memo[(row, col)]

        if row == len(grid)-1 and col == len(grid[0])-1:
            return grid[row][col]
        
        bottom = self.give_min_option(row + 1, col, memo, grid)
        right = self.give_min_option(row, col + 1, memo, grid)

        min_option = min(bottom, right)
        memo[(row, col)] = min_option + grid[row][col]
        return min_option + grid[row][col]

    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = defaultdict(int)
        return self.give_min_option(0, 0, memo, grid)