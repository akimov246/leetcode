class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        tmp_candies = sorted(list(set(candies)))
        min_ = -1
        max_ = tmp_candies[-1]
        for tmp in tmp_candies:
            if tmp + extraCandies >= max_:
                min_ = tmp
                break
        return [False if kid < min_ else True for kid in candies]


print(Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))