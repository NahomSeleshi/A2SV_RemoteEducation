class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_size = float("inf")
        cur_sum = 0
        left, right = 0, 0
        while left < n:
            if cur_sum >= target:
                cur_sum -= nums[left]
                min_size = min(min_size, right-left)
                left += 1
            else:
                if right == n:
                    break
                cur_sum += nums[right]
                right += 1
        return min_size if min_size != float("inf") else 0
                
        