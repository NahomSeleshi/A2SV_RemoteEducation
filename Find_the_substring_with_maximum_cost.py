class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        corresponding_values = []
        value_map = {}
        for i in range(len(chars)):
            value_map[chars[i]] = vals[i]
            
        for each_char in s:
            if each_char in value_map:
                corresponding_values.append(value_map[each_char])
            else:
                corresponding_values.append(ord(each_char)-ord('a')+1)
        
        for i in range(1, len(corresponding_values)):
            if corresponding_values[i-1] > 0:
                corresponding_values[i] += corresponding_values[i-1]
                
        max_value = max(corresponding_values)
        return max_value if max_value > 0 else 0