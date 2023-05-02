class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        first, last = nums[0], nums[-1]
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            max_num = max(nums[i] + k, nums[-1] - k)
            min_num = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, max_num - min_num)
        return ans