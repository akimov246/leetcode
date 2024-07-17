class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        num_of_prefixes = 0
        for word in words:
            if word.startswith(pref):
                num_of_prefixes += 1
        return num_of_prefixes

print(Solution().prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))