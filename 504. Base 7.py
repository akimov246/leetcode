class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        base = 7
        n = abs(num)
        ans = ''
        while n != 0:
            ans += str(n % base)
            n //= base
        return ans[::-1] if num >= 0 else '-' + ans[::-1]

print(Solution().convertToBase7(-7))