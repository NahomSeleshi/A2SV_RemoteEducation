class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix_sum, right_prefix_sum = [0],[0]
        for i in range(len(nums)):
            left_prefix_sum.append(left_prefix_sum[-1] + nums[i])
        left_prefix_sum.append(0)
        for j in range(len(nums)-1, -1,-1):
            right_prefix_sum.append(right_prefix_sum[-1] + nums[j])
        right_prefix_sum.append(0)
        right_prefix_sum.reverse()
        for pivot_index in range(1,len(nums)+1):
            if left_prefix_sum[pivot_index-1] == right_prefix_sum[pivot_index + 1]:
                return pivot_index-1
        return -1