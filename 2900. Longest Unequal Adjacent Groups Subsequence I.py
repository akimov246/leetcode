class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        result = []
        prev = None
        for i in range(len(groups)):
            if groups[i] != prev:
                result.append(words[i])
                prev = groups[i]

        return result


print(Solution().getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))