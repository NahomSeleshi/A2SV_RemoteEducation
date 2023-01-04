class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern, s = list(pattern), s.split(" ")
        if len(pattern) != len(s):
            return False
        mapping_pattern_s = {}
        mapping_s_pattern = {}
        for key1, key2 in zip(pattern, s):
            if key1 not in mapping_pattern_s and key2 not in mapping_s_pattern:
                mapping_pattern_s[key1] = key2
                mapping_s_pattern[key2] = key1

            elif mapping_pattern_s.get(key1) != key2 or mapping_s_pattern.get(key2) != key1:
                return False
        return True
