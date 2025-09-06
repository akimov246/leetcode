class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = ''
        num1 = str(num1).rjust(4, '0')
        num2 = str(num2).rjust(4, '0')
        num3 = str(num3).rjust(4, '0')

        for chars in zip(num1, num2, num3):
            key += min(chars)

        return int(key)


print(Solution().generateKey(num1 = 1, num2 = 10, num3 = 1000))