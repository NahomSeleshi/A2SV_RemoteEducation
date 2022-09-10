class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for each in points:
            distance.append([math.sqrt(each[0]**2 + each[1]**2),each])
        distance.sort()
        return [distance[i][1] for i in range(k)]