from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter = defaultdict(int)
        for word in s1.split() + s2.split():
            counter[word] += 1
        return [c for c in counter if counter[c] == 1]


print(Solution().uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))