from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for char in ascii_lowercase:
            if not char in sentence:
                return False
        return True

print(Solution().checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))