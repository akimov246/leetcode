class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        words = words[left:right + 1]
        vowels = 'aeiou'
        result = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                result += 1
        return result

print(Solution().vowelStrings(words = ["are","amy","u"], left = 0, right = 2))