class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        return len(word_set) - len(set(letter.lower() for letter in word_set))

print(Solution().numberOfSpecialChars("aaAbcBC"))