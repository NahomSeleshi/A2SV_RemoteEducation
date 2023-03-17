class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_freq = [0 for i in range(26)]
        for each in s:
            if char_freq[ord(each)-ord('a')] == 1:
                return each
            else:
                char_freq[ord(each)-ord('a')] += 1
                