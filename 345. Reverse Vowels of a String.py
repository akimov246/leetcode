class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        VOWELS = "aeiouAEIOU"
        indexes = [i for i in range(len(s)) if s[i] in VOWELS]
        left = indexes[:len(indexes) // 2]
        right = indexes[len(indexes) // 2:][::-1]
        for l, r in zip(left, right):
            s[l], s[r] = s[r], s[l]
        return "".join(s)

print(Solution().reverseVowels("leetcode"))