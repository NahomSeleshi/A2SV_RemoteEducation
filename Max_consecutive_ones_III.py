class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            # if nums at end is 0, we have to reduce k by one else, leave it.
            k -= (1 - nums[right])

            # k is less than 0 means we cannot expand our window furthur so we
            # have to shrink our window from left and if the value at the left
            # index before shrink was zero, we have to increase the value of k by one.

            # if k is negative, we will keep widening the window from right and shrinking
            # it from left so the max window we found early will be preserved.
            if k < 0:
                k += (1 - nums[left])
                # this line is to preserve the window that we currently have
                left += 1
        return right - left + 1 
        