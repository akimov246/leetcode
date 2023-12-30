import math
from collections import Counter

# Посредственное решение (ебал мозга больше часа, хотя тут нехуй делать)
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        if len(words) == 1:
            return True
        words_union = ''.join(words)
        letter_counter = Counter(words_union)
        counts = tuple(letter_counter.values())
        if all(c >= len(words) for c in counts):
            if all(c != 1 for c in counts):
                if all(math.gcd(max(counts), c) != 1 for c in counts):
                        return True
        return False

# Решиение с leetcode (В принципе, тоже самое, только без идиотских 3 условий)
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counts = {}

        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1

        n = len(words)
        for value in counts.values():
            if value % n != 0:
                return False
        return True

print(Solution().makeEqual(["aaaaaa","bbb","cc"]))
#print(Solution().makeEqual(["aaaaaaaaaaaaaaaaa","aaaaa","aaaaaa","aaaaaaaaa","a","aaa","aaaa","bbbbbbbbbbbbbbbbbbbbbbb","bb","b","bb","bb","ccccccccccccccccccccccccccccccccccccccc","c","ccccc"]))