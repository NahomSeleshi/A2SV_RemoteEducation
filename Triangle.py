class Solution:
    def return_min_path(self, triangle:List[List[int]], cur_index:int, cur_row:int, memo) -> int:
        if cur_row + 1 == len(triangle):
            return triangle[cur_row][cur_index]
        if memo[cur_row][cur_index]  != "NA":
            return memo[cur_row][cur_index]

        no_shift = self.return_min_path(triangle, cur_index, cur_row + 1, memo)
        one_shift = self.return_min_path(triangle, cur_index + 1, cur_row + 1, memo)

        min_path = min(no_shift, one_shift) + triangle[cur_row][cur_index]
        memo[cur_row][cur_index] = min_path
        return min_path
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        memo = [["NA" for col in range(len(triangle[row]))] for row in range(len(triangle))]
        return self.return_min_path(triangle, 0, 0, memo)

    