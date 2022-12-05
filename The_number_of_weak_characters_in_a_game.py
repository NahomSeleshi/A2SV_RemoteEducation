class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        properties.sort(key = lambda x: (-x[0], x[1]))
        weak_characters, max_def = 0, 0
        
        for cur_att, cur_def in properties:
            if cur_def < max_def:
                weak_characters += 1
            else:
                max_def = cur_def
        return weak_characters