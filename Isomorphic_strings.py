class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = defaultdict(str)
        mapping_t_s = defaultdict(str)

        for char1, char2 in zip(s, t):
            if char1 not in mapping_s_t and char2 not in mapping_t_s:
                mapping_s_t[char1] = char2
                mapping_t_s[char2] = char1
            elif mapping_s_t[char1] != char2 or mapping_t_s[char2] != char1:
                return False
        return True