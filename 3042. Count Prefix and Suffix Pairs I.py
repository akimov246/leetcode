class Solution:
    @classmethod
    def countPrefixSuffixPairs(self, words: list[str]) -> int:

        def isPrefixAndSuffix(str1, str2: str):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            return False

        counter = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                counter += isPrefixAndSuffix(words[i], words[j])

        return counter

print(Solution().countPrefixSuffixPairs(words = ["a","aba","ababa","aa"]))