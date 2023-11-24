class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join([char.lower() for char in s if char.isdigit() or char.isalpha()])
        return result == result[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))