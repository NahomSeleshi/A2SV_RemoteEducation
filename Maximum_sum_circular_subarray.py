class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # The approach here is, if our max subarray sum is circular (max2), our minimum
        # subarray sum is not circular. If our max subarray sum is not circular, we
        # know ways to find it (max1). So, the true circular subarray sum is max(max1, max2)

        # Here, we find the maximum subarray here (not the circular one)
        total_sum = sum(nums)
        nums1 = nums.copy()
        for i in range(1, len(nums1)):
            if nums1[i-1] > 0:
                nums1[i] += nums1[i-1]
        # This is the maximum subarray (not the circular one), max1
        max_sum = max(nums1)

        # Here, we find the minimum subarray (not the circular one), max2
        for i in range(1, len(nums)):
            if nums[i-1] < 0:
                nums[i] += nums[i-1]

        min_sum = min(nums) if min(nums) != total_sum else abs(total_sum)
        return max(total_sum-min_sum, max_sum)

