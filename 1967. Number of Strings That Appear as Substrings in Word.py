class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        substrings = 0
        for pattern in patterns:
            if pattern in word:
                substrings += 1
        return substrings

print(Solution().numOfStrings(patterns = ["a","abc","bc","d"], word = "abc"))