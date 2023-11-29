class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        num = tuple(int(n) for n in str(num))
        new_num = sum(num)
        return self.addDigits(new_num)



print(Solution().addDigits(1337))