from heapq import heapify, heappop, heappush
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        heapify(min_heap)
        for i in range(len(heights)-1):
            height_difference = heights[i+1] - heights[i]
            if height_difference > 0:
                heappush(min_heap, height_difference)
            if len(min_heap) > ladders:
                bricks -= (heappop(min_heap))
            if bricks < 0:
                return i
        return len(heights)-1