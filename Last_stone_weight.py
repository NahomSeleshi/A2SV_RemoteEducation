from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapify(max_heap)
        for each in stones:
            heappush(max_heap, -each)

        while len(max_heap) > 1:
            stone1, stone2 = -heappop(max_heap), -heappop(max_heap)
            if stone1 != stone2:
                heappush(max_heap, -(stone1-stone2))

        return -max_heap[0] if max_heap else 0