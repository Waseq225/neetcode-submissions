class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length = len(t)
        index_t = 0
        for i in range(len(s)):
            if s[i] == t[index_t]:
                index_t += 1
                if index_t == length:
                    return 0
        return length - index_t
         