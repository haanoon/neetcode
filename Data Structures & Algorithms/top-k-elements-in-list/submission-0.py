from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [item for item, frqr in heapq.nlargest(k,c.items(),key = lambda x: x[1])]