class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated_sequences = set()
        available_sequences = set()
        for i in range(len(s)-9):
            cur_DNA = s[i:i+10]
            if cur_DNA in available_sequences:
                repeated_sequences.add(cur_DNA)
            else:
                available_sequences.add(cur_DNA)
        return repeated_sequences