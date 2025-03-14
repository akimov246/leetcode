class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if len(candies) == 1 and k == 1:
            return candies[0]

        candies.sort()

        max_candies_in_pile = max(0, candies[-1])

        left = 0
        right = max_candies_in_pile
        middle = (left + right + 1) // 2

        def check(current_try):
            if current_try == 0:
                return False
            counter = 0
            for pile in reversed(candies):
                counter += pile // current_try
                if counter >= k:
                    return True
            return False

        result = 0
        while left < right:
            if check(middle):
                left = middle
                result = max(result, middle)
            else:
                right = middle - 1
            middle = (left + right + 1) // 2

        return result
