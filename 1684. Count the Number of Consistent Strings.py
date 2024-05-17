class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        consistent = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                consistent += 1
        return consistent

print(Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))