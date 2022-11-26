class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = 0
        diff_freq = {0:1}
        
        for each in nums:
            prefix_sum += each
            if prefix_sum - k in diff_freq:
                answer += diff_freq[prefix_sum - k]
            if prefix_sum not in diff_freq:
                diff_freq[prefix_sum] = 1
            else:
                diff_freq[prefix_sum] = diff_freq[prefix_sum] + 1
        return answer