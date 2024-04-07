from functools import cache

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        @cache
        def counter(word: str) -> dict[str, int]:
            c = {}
            for w in word:
                c[w] = c.get(w, 0) + 1
            return c

        i = 1
        while i < len(words):
            if counter(words[i]) == counter(words[i - 1]):
                words.pop(i)
                i = 1
                continue
            i += 1
        return words

print(Solution().removeAnagrams(words = ["abba","baba","bbaa","cd","cd"]))