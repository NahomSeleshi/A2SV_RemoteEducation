class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        used_characters, max_length = defaultdict(int), 0
        left, right = 0, 0
        while right < len(s):
            if used_characters[s[right]] != 0:
                max_length = max(max_length, right - left)
                used_characters[s[left]] -= 1
                left +=1
            else:
                used_characters[s[right]] += 1
                right += 1
        max_length = max(max_length, right - left)
        return max_length

        