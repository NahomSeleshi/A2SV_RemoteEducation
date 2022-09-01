class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notInArr2 = []
        numFreq = Counter(arr1)
        answer = []
        for each in arr2:
            for i in range(numFreq[each]):
                answer.append(each)
            del numFreq[each]
        for each in numFreq:
            for i in range(numFreq[each]):
                notInArr2.append(each)
        answer.extend(sorted(notInArr2))
        return answer
        