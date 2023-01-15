class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        vote = defaultdict(int)

        # one elemenent of this list below holds [the leader of the election, the number 
        # of votes he has, and the time that he is leading] as a single element [a, 5, 15]. 
        # Candidate a is leading with 5 votes at the 15th time unit.
        self.vote_at_time = []
        
        for i in range(len(times)):
            vote[persons[i]] += 1
            if self.vote_at_time:
                last_guy, max_vote, time = self.vote_at_time[-1]
                if max_vote <= vote[persons[i]]:
                    self.vote_at_time.append([persons[i], vote[persons[i]], times[i]])
                else:
                    self.vote_at_time.append([last_guy, max_vote, times[i]])
            else:
                self.vote_at_time.append([persons[i], vote[persons[i]], times[i]])

    def q(self, t: int) -> int:
        left, right = 0, len(self.vote_at_time)-1
        while left <= right:
            mid = left + (right - left) // 2
            person , _, time = self.vote_at_time[mid]
            if time <= t:
                left = mid + 1
            else:
                right = mid - 1
        return self.vote_at_time[left-1][0]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
