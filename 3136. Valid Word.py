from string import ascii_letters, digits

class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        vowel = False
        consonant = False

        for char in set(word):
            if char in ascii_letters:
                if char in 'aeiouAEIOU':
                    vowel = True
                else:
                    consonant = True
            elif char not in digits:
                return False

        return vowel and consonant


print(Solution().isValid(word = "AhI"))