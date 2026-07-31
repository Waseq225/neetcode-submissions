from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = Counter(nums)
        output = sorted(result.keys(), key=lambda x: result[x], reverse=True)
        return output[:k]