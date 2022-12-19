class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_sum = float("inf")
        nums.sort()
        for i in range(n-2):
            left, right, cur_num = i+1, n-1, nums[i]
            while left < right:
                cur_sum = cur_num + nums[left] + nums[right]
                min_sum = cur_sum if abs(min_sum - target) > abs(cur_sum-target) else min_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    return cur_sum
        return min_sum