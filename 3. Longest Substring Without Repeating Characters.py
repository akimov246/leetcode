class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            length = 1
            while i + length <= len(s):
                substring = s[i:i + length]
                if len(substring) == len(set(substring)):
                    longest = max(length, longest)
                    length += 1
                else:
                    break
        return longest


print(Solution().lengthOfLongestSubstring(s = "a"))