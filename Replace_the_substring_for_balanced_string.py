class Solution:
    def balancedString(self, s: str) -> int:
        char_count = Counter(s)
        one_fourth = len(s)//4

        # this dictionary holds the characters that are going
        # to be replaced and their corresponding count 
        needed_chars = {}
        for each in char_count:
            if char_count[each] > one_fourth:
                needed_chars[each] = char_count[each]- one_fourth
        
        min_length = float("inf")
        left, right = 0, 0
        # this is the number of distinct letters that we need to replace
        distinct_letters = len(needed_chars)
        
        # if no distinct letters to be replaced, return a size of zero
        if distinct_letters == 0:
            return 0

        # Here, we are trying to find a window that contains each letters to 
        # be replaced with the frequency of that letter.
        while right < len(s):
            if s[right] in needed_chars:
                needed_chars[s[right]] -= 1
                if needed_chars[s[right]] == 0:
                    distinct_letters -= 1
            right += 1
            while distinct_letters == 0:
                if s[left] in needed_chars:
                    if needed_chars[s[left]] == 0:
                        distinct_letters += 1
                    needed_chars[s[left]] += 1
                left += 1
                min_length = min(min_length, right - left + 1)
        
        return min_length