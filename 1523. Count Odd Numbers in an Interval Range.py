class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2:
            low -= 1
        if high % 2:
            high += 1
        return (high - low) // 2

print(Solution().countOdds(low = 8, high = 10))