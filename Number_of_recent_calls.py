class RecentCounter:

    def __init__(self):
        self.ping_list = deque([])
        self.cur_ping = 0

    def ping(self, t: int) -> int:
        self.ping_list.append(t)
        while not t-3000 <= self.ping_list[0] <= t:
            self.ping_list.popleft()
        return len(self.ping_list)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)