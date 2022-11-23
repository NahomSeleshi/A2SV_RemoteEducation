class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        cur_min = min(nums)
        return 1 if cur_min > 0 else abs(cur_min) + 1