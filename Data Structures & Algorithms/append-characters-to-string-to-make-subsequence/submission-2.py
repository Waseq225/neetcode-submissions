class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_s, pointer_t = 0, 0
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s, pointer_t = pointer_s + 1, pointer_t + 1
            else:
                pointer_s += 1
        remaining = len(t) - pointer_t
        return remaining
         