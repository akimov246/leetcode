class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = list(pattern)
        words = s.split()
        if len(letters) != len(words):
            return False
        if len(set(letters)) != len(set(words)):
            return False
        d = {}
        for letter, word in zip(letters, words):
            value = d.get(letter)
            if not value:
                d[letter] = word
            else:
                if word != value:
                    return False
        return True

# Решение с Leetcode
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))

from itertools import zip_longest
print(Solution().wordPattern("abba", "dog cat dog cat"))
print(set(zip("abba", ["dog", "cat", "cat", "dog", "cat"])))
print(set(zip_longest("abba", ["dog", "cat", "cat", "dog", "cat"])))