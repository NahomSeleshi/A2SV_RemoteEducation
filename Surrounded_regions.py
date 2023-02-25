class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        for row in range(len(board)):
            if board[row][0] == "O":
                self.dfs(row, 0, board, visited)
            if board[row][len(board[0])-1] == "O":
                self.dfs(row, len(board[0])-1, board, visited)
        for col in range(len(board[0])):
            if board[0][col] == "O":
                self.dfs(0, col, board, visited)
            if board[len(board)-1][col] == "O":
                self.dfs(len(board)-1, col, board, visited)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"

    def dfs(self, row, col, board, visited):
        if not 0 <= row <len(board) or not 0 <= col <len(board[0]):
            return 
        if (row, col) in visited or board[row][col] == "X":
            return
        visited.add((row, col))

        # Traverse 4 directionally
        for dr, dc in [[0,1], [0, -1], [1, 0], [-1, 0]]:
            new_r, new_c = row + dr, col + dc
            self.dfs(new_r, new_c, board, visited)
        return 