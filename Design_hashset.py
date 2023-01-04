class MyHashSet:

    def __init__(self):
        self.my_hashset = [False for i in range((10**6)+1)]

    def add(self, key: int) -> None:
        self.my_hashset[key] = True

    def remove(self, key: int) -> None:
        self.my_hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.my_hashset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)