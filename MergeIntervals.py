class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                if intervals[i][1] > intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
            else:
                answer.append(intervals[i])
            i+=1
        answer.append(intervals[-1])
        return answer