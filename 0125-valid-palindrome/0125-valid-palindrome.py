class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum())
        return word.lower() == "".join(reversed(word.lower()))