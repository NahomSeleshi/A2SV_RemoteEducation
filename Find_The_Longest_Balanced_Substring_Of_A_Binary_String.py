class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        cur_index = 0
        longest_bal_substring = 0
        
        while cur_index < len(s):
            while cur_index < len(s) and s[cur_index] != '0':
                cur_index += 1
            if cur_index == len(s):
                break
            zero_start = cur_index
            while cur_index < len(s) and s[cur_index] == '0':
                cur_index += 1
            if cur_index == len(s):
                break
            zero_window = cur_index - zero_start
            one_start = cur_index
            while cur_index < len(s) and s[cur_index] == '1':
                cur_index += 1
            one_window = cur_index - one_start
            longest_bal_substring = max(longest_bal_substring, 2*(min(zero_window, one_window)))
            
        return longest_bal_substring