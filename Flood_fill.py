class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        m, n = len(image), len(image[0])

        def dfs(row, col, parent_color):
            for dx, dy in [[0,1], [0,-1], [1, 0], [-1, 0]]:
                cur_row, cur_col = row + dx, col + dy
                if 0 <= cur_row < m and 0 <= cur_col < n:
                    if image[cur_row][cur_col] == parent_color and ((cur_row, cur_col) not in visited):
                        visited.add((cur_row, cur_col))
                        dfs(cur_row, cur_col, parent_color)
            image[row][col] = color

        dfs(sr, sc, image[sr][sc])        
        return image
            