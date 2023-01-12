class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_numbers = 0
        for row in range(len(grid)):
            cur_row = grid[row]
            left, right = 0, len(cur_row)-1
            while left <= right:
                mid = left + (right - left) // 2
                if cur_row[mid] < 0:
                    right = mid - 1 
                else:
                    left = mid + 1
            negative_numbers += (len(cur_row)-left)
        return negative_numbers