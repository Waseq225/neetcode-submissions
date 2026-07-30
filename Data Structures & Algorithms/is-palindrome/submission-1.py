class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join([char for char in s if char.isalnum()])
        new_string , cleaned_string = cleaned_string.lower(), cleaned_string.lower()
        if new_string == cleaned_string[::-1]:
            return True
        else:
            return False