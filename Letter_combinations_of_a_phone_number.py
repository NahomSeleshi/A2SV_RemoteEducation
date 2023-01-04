class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        possible_combinations = []
        digit_to_alphabet = {'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'],'4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],'6': ['m', 'n', 'o'],'7': ['p', 'q', 'r','s'],
                         '8': ['t', 'u', 'v'],'9': ['w', 'x', 'y','z'], }

        def combination_generator(cur_string, cur_index):
            if cur_index >= len(digits):
                possible_combinations.append(cur_string)
                return 
            for each_char in digit_to_alphabet[digits[cur_index]]:
                combination_generator(cur_string + each_char, cur_index + 1)
        combination_generator("", 0)
        return possible_combinations