import string
from collections import defaultdict

class Solution:

    alphabet = {letter: num for letter, num in zip(string.ascii_lowercase, range(len(string.ascii_lowercase)))}

    def checkDistances(self, s: str, distance: list[int]) -> bool:
        indexes = defaultdict(list)
        for i in range(len(s)):
            indexes[s[i]].append(i)
        indexes = dict(indexes)

        for letter in set(s):
            if indexes[letter][1] - indexes[letter][0] - 1 != distance[self.alphabet[letter]]:
                return False

        return True


print(Solution().checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))