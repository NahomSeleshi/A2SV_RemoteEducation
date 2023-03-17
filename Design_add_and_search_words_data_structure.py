class Trie_node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie_node('#')

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for each_char in word:
            if not each_char in cur_node.children:
                cur_node.children[each_char] = Trie_node(each_char)
            cur_node = cur_node.children[each_char]
        
        cur_node.is_end_of_word = True

    def search(self, word: str, index:int = 0, temp:Trie_node = None) -> bool:
        if (index >= len(word) and temp and not temp.is_end_of_word):
            return False
        cur_node = temp if temp else self.root
        for char_index in range(index,len(word)):
            if word[char_index] == '.':
                word_is_there = False
                for each in cur_node.children:
                    word_is_there = word_is_there or self.search(word, char_index+1, cur_node.children[each])
                return word_is_there
            if word[char_index] not in cur_node.children:
                return False
            cur_node = cur_node.children[word[char_index]]
        return cur_node.is_end_of_word
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)