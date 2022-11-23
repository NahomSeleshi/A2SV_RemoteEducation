class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0]
        for i in range(len(arr)):
            prefix_sum.append(prefix_sum[-1]+arr[i])
        final_answer = 0
        for win in range(1,len(arr)+1, 2):
            for i in range(win,len(prefix_sum)):
                final_answer += prefix_sum[i] - prefix_sum[i-win]
        
        return final_answer