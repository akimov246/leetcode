class Solution:
    def reverse(self, x: int) -> int:
        bit_range_32 = range(-2**31, 2**31)
        x = str(x)
        sign = ''
        if x[0] in '-+':
            sign = x[0]
            x = x[1:]
        x = int(sign + x[::-1])
        return x if x in bit_range_32 else 0

print(Solution().reverse(123))