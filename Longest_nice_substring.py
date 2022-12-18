class Solution:
    def check_nice(self, cur_str):
        chars = set(cur_str)
        for c in chars:
            if c.islower() and c.upper() not in chars or c.isupper() and c.lower() not in chars:
                return False, len(cur_str)
        return True, len(cur_str)
    
    def longestNiceSubstring(self, s: str) -> str:
        longest_nice, max_len = "", float("-inf")
        for start_index in range(len(s)):
            for end_index in range(start_index + 1, len(s)+1):
                is_nice, cur_len = self.check_nice(s[start_index:end_index])
                if is_nice and cur_len > max_len:
                    longest_nice = s[start_index:end_index]
                    max_len = cur_len
        return longest_nice
