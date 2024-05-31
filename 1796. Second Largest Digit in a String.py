class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for i in range(9, -1, -1):
            if str(i) in s:
                digits.append(i)
                if len(digits) > 1:
                    break

        return digits[1] if len(digits) > 1 else -1

print(Solution().secondHighest(s = "dfa12321afd"))