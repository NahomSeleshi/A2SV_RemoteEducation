class Solution:
    def set_zero(self, row_or_col, value, matrix) -> None:
        walk_row, walk_col = 0, 0
        if row_or_col == 'column':
            while walk_row < len(matrix):
                matrix[walk_row][value] = 0
                walk_row += 1
        else:
            while walk_col < len(matrix[0]):
                matrix[value][walk_col] = 0
                walk_col += 1

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cell_indexes = {'row':set(), 'column':set()}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    cell_indexes['row'].add(row)
                    cell_indexes['column'].add(col)
        for each_row in cell_indexes['row']:
            self.set_zero('row', each_row, matrix)
        for each_col in cell_indexes['column']:
            self.set_zero('column', each_col, matrix)
        
        
