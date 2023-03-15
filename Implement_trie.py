class Trie_node:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for each_char in word:
            if not cur_node.children[ord(each_char)-ord('a')]:
                cur_node.children[ord(each_char)-ord('a')] = Trie_node()
            cur_node = cur_node.children[ord(each_char)-ord('a')]
        cur_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for each_char in word:
            if not cur_node.children[ord(each_char)-ord('a')]:
                return False
            cur_node = cur_node.children[ord(each_char)-ord('a')]
        return cur_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for each_char in prefix:
            if not cur_node.children[ord(each_char)-ord('a')]:
                return False
            cur_node = cur_node.children[ord(each_char)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)