class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check the rows
        for row in board:
            if self.check_duplicate(row):
                return False
        
        #check the columns
        for col in range(len(board[0])):
            if self.check_duplicate([board[i][col] for i in range(len(board))]):
                return False
                
        #check the small matrices
        for i in range(0,len(board),3):
            for j in range(0, len(board[0]), 3):
                if self.check_duplicate(self.build_string(board, i, j)):
                    return False
        return True
      
    def build_string(self, board, row,col) -> List[str]:
        answer_list = []
        for i in range(row, row+3):
            for j in range(col, col+3):
                answer_list.append(board[i][j])
        return answer_list
                
    def check_duplicate(self, cur_list: List[str]) -> bool:
        cur_nums = set()
        for each in cur_list:
            if each == '.':
                continue
            if each in cur_nums:
                return True
            else:
                cur_nums.add(each)
        return False