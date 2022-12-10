class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        col = len(mat[0])-1
        for i in range(len(mat)):
            _sum += mat[i][i] + mat[i][col]
            col-=1
        if len(mat)% 2 != 0:
            _sum -= mat[len(mat)//2][len(mat)//2]
        return _sum 