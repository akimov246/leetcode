class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for word, char in zip(words, s):
            if word[0] != char:
                return False
        return True

print(Solution().isAcronym(words = ["alice","bob","charlie"], s = "abc"))