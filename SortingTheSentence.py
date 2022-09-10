class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(map(str, s.split(" ")))
        s.sort(key = lambda x: x[-1])
        answer = "".join(each[:len(each)-1] + " " for each in s)
        return answer[:len(answer)-1]