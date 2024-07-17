class Solution:
    def countEven(self, num: int) -> int:
        return len([n for n in range(1, num + 1) if sum(int(digit) for digit in str(n)) % 2 == 0])

print(Solution().countEven(30))