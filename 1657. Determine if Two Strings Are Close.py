from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        if sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values()):
            return True
        return False

print(Solution().closeStrings('abc', 'bca'))