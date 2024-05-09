class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(',', '.')

print(Solution().thousandSeparator(1234))