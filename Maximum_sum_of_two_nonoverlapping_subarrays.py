class Solution:

    def validate_subarrays(self, first, second, firstLen, secondLen):
        f_s = first - firstLen + 1
        s_s = second - secondLen + 1
        if s_s <= f_s <= second or f_s <= s_s <= first or s_s < 0 or f_s < 0:
            return False
        return True

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for i in range(len(nums)):
           prefix_sum.append(prefix_sum[i] + nums[i])
        
        maximum_sum = float("-inf")
        for f in range(len(prefix_sum)):
            for s in range(len(prefix_sum)):
                if self.validate_subarrays(f, s, firstLen, secondLen):
                    maximum_sum = max(maximum_sum, prefix_sum[f]-prefix_sum[f-firstLen] + prefix_sum[s]-prefix_sum[s-secondLen])

        return maximum_sum

           