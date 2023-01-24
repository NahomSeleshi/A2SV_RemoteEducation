from heapq import heapify, heappop, heappush
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = collections.Counter(nums)
        min_heap = []
        heapify(min_heap)

        for key in num_freq:
            heappush(min_heap, [num_freq[key], key])
            if len(min_heap) > k:
                heappop(min_heap)

        return [each[1] for each in min_heap]