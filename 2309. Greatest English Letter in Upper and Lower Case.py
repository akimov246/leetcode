class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ''
        for letter in set(s):
            if letter.lower() in s and letter.upper() in s:
                ans += letter.upper()
        return sorted(ans)[-1] if ans else ans

print(Solution().greatestLetter(s = "lEeTcOdE"))