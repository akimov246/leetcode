class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        for val in list(str(num)):
            if num % int(val) == 0:
                result += 1
        return result

print(Solution().countDigits(7))