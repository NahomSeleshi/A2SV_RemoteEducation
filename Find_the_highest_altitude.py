class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer, current_altitude = 0, 0
        for each in gain:
            current_altitude += each
            answer = max(answer, current_altitude)
        return answer