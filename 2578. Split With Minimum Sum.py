class Solution:
    def splitNum(self, num: int) -> int:
        num1 = ''
        num2 = ''
        for i, n in enumerate(sorted(str(num))):
            if i % 2:
                num2 += n
            else:
                num1 += n
        return sum((int(num1), int(num2)))

print(Solution().splitNum(4325))