class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        x = low
        while x <= high:
            if x % 2:
                count += 1
                x += 2
            else:
                x += 1

        return count

print(Solution().countOdds(low = 3, high = 7))