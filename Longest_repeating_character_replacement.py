class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(ord('A'), ord('Z')+1):
            cur_char = chr(i)
            left, right, flips = 0, 0, k
        
            for right in range(len(s)):
                if s[right] != cur_char:
                    flips -= 1
                if flips < 0:
                    if s[left] != cur_char:
                        flips += 1
                    left += 1                
            max_len = max(max_len, right - left + 1)
        return max_len