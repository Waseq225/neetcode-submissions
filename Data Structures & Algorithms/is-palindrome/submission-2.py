class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join([char for char in s if char.isalnum()])
        if cleaned_string.lower() == cleaned_string.lower()[::-1]:
            return True
        else:
            return False