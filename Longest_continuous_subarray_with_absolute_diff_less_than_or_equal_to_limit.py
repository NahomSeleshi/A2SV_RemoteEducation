from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sorted_list = SortedList()
        left, max_length = 0, 0
        for right, value in enumerate(nums):
            sorted_list.add(value)
            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(nums[left])
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length


