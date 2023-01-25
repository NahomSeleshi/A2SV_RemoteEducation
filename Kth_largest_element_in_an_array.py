from heapq import heapify, heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapify(min_heap)

        for each in nums:
            heappush(min_heap, each)
            if len(min_heap) > k:
                heappop(min_heap)
        
        return min_heap[0]

