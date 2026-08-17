class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_tier = iter(t)
        for char in s:
            if char not in t_tier:  
                return False
        return True
