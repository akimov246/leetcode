class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 == 1:
            return False
        divisors = set()
        for i in range(1, int(num // 2) + 1):
            if num % i == 0:
                divisors.add(i)
        return True if sum(divisors) == num else False

print(Solution().checkPerfectNumber(99999992))