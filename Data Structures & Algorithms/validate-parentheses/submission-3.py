class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            old_length = len(s)
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if len(s) == old_length:
                break
        return s == ''
