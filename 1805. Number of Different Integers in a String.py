from string import ascii_lowercase

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for char in ascii_lowercase:
            word = word.replace(char, ' ')
        return len(set(int(num) for num in word.split()))

print(Solution().numDifferentIntegers(word = "a123bc34d8ef34"))