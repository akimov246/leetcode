class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        result = 0
        for word in words:
            if s.startswith(word):
                result += 1
        return result

print(Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc"))