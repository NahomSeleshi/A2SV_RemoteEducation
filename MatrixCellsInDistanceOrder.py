class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        answer = []
        disWithCoordinates = []
        for i in range(rows):
            for j in range(cols):
                curDis = abs(i-rCenter) + abs(j-cCenter)
                disWithCoordinates.append([curDis,[i,j]])
        disWithCoordinates.sort()
        for i in range(len(disWithCoordinates)):
            answer.append(disWithCoordinates[i][1])
        return answer