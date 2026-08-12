class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        non_space = s.strip().split()
        return len(non_space[-1])        