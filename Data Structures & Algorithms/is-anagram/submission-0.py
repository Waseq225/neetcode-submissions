class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result_s = "".join(sorted(s))
        result_t = "".join(sorted(t))
        total_length = len(s) + len(t)
        if len(s) != len(t):
            return False
        else:
            if result_t == result_s:
                return True
            else:
                return False

                
        