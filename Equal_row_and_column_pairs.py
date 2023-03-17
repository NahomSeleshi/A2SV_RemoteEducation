class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        column_array = []
        for c in range(m):
            cur_array = []
            for r in range(n):
                cur_array.append(grid[r][c])
            column_array.append(cur_array)
            
        equal_pairs = 0    
        for row in range(n):
            for i in range(len(column_array)):
                if grid[row] == column_array[i]:
                    equal_pairs += 1
        return equal_pairs