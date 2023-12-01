class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        w1 = "".join(word1)
        w2 = "".join(word2)
        return w1 == w2


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2))