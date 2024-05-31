class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def gen():
            it1 = iter(word1)
            it2 = iter(word2)
            for _ in range(len(max(word1, word2, key=len))):
                try:
                    yield next(it1)
                except: pass
                try:
                    yield next(it2)
                except: pass

        return ''.join(gen())

print(Solution().mergeAlternately(word1 = "abc", word2 = "pqr"))