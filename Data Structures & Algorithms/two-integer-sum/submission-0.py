class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in indices:
                return [indices[diff], i]
            indices[value] = i
        return