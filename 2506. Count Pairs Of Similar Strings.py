class Solution:
    def similarPairs(self, words: list[str]) -> int:
        words = [set(word) for word in words]
        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    result += 1
        return result

print(Solution().similarPairs(words = ["aba","aabb","abcd","bac","aabc"]))