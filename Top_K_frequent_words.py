from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # This implementation uses a max heap
        
        word_freq = collections.Counter(words)
        max_heap = []
        heapify(max_heap)

        for word, freq in word_freq.items():
            heappush(max_heap, [-freq, word])

        top_k_words = []
        for i in range(k):
            top_k_words.append(heappop(max_heap)[1])  

        return top_k_words

        # This implementation uses sorting

        # word_freq = collection.Counter(words)
        # word_freq = sorted(word_freq.items(), key = lambda x: (-x[1], x[0]))

        # return [word_freq[each][0] for each in range(k)]
