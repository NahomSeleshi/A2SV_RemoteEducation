class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: (x[0], -x[1]))
        
        min_arrows = 0
        for cur_idx in range(len(points)-1):
            if points[cur_idx][1] < points[cur_idx + 1][0]:
                min_arrows += 1
                continue
            points[cur_idx + 1][1] = min(points[cur_idx][1], points[cur_idx + 1][1])

        return min_arrows + 1