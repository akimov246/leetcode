class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        for word in s.split():
            ans += word[::-1] + ' '
        return ans[:len(ans) - 1]

print(Solution().reverseWords("Let's take LeetCode contest"))