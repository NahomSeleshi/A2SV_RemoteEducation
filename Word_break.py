class Solution:
    def find_word(self, index:int , orig_word:str, word_set: set, visited_indices:set):
        if index == len(orig_word):
            return True
        possible_future = False
        for i in range(index+1, len(orig_word)+1):
            if orig_word[index:i] in word_set and i not in visited_indices:
                visited_indices.add(i)
                possible_future = possible_future or self.find_word(i, orig_word, word_set, visited_indices)
        return possible_future

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.find_word(0, s, set(wordDict), set())



