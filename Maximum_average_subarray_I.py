class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])
        max_ave = cur_sum/k
        for i in range(k,n):
            cur_sum += (-nums[i-k] + nums[i])
            max_ave = max(max_ave, cur_sum/k)
        return max_ave