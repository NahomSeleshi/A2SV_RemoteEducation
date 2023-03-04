class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited_words = {beginWord}
        queue = deque([(beginWord, 1)])
        word_list_set = set(wordList)

        while queue:
            cur_word, level = queue.popleft()
            if cur_word == endWord:
                return level
            for i in range(len(cur_word)):
                cur_word_list = list(cur_word)
                for j in range(26):
                    cur_word_list[i] = chr(ord('a') + j) 
                    possible_word = "".join(cur_word_list)
                    if possible_word not in visited_words and possible_word in word_list_set:
                        queue.append((possible_word, level + 1))
                        visited_words.add(possible_word)
        return 0