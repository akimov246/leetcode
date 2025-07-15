class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        permutation_difference = 0
        for i in range(len(s)):
            permutation_difference += abs(i - t.index(s[i]))
        return permutation_difference

print(Solution().findPermutationDifference(s = "abc", t = "bac"))