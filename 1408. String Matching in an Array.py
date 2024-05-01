class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        substrings = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[j].find(words[i]) != -1:
                        substrings.add(words[i])
                        break
        return list(substrings)

print(Solution().stringMatching(words = ["mass","as","hero","superhero"]))