class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = {}
        counter2 = {}
        for c1, c2 in zip(word1, word2):
            counter1[c1] = counter1.get(c1, 0) + 1
            counter2[c2] = counter2.get(c2, 0) + 1
        for char in set(word1).union(set(word2)):
            if abs(counter1.get(char, 0) - counter2.get(char, 0)) > 3:
                return False
        return True

print(Solution().checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))