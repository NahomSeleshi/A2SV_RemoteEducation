class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([])
        for i in range(len(tickets)):
            if i == k:
                queue.append([tickets[i], 'T'])
            else:
                queue.append([tickets[i], 'F'])
        time_taken = 0
        while queue:
            ticket, flag = queue.popleft()
            ticket -= 1
            time_taken += 1
            if ticket == 0 and flag == 'T':
                break
            if ticket > 0:
                queue.append([ticket, flag])
        return time_taken