class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for n in sorted(set(num), reverse=True):
            if n * 3 in num:
                return n * 3
        return ''

print(Solution().largestGoodInteger(num = "6777133339"))