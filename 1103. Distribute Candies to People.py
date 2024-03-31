class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        c = 1
        index = 0
        ans = [0 for _ in range(num_people)]
        while candies > 0:
            ans[index] += c if candies - c > 0 else candies
            candies -= c
            c += 1
            index += 1
            if index == num_people:
                index = 0
        return ans


print(Solution().distributeCandies(candies = 7, num_people = 4))