from functools import cache

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        number_of_good_triplets = 0
        # @cache
        # def helper(x, y, z):
        #     return (abs(x - y) <= a) and \
        #            (abs(y - z) <= b) and \
        #            (abs(x - z) <= c)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                     if (abs(arr[i] - arr[j]) <= a) and \
                        (abs(arr[j] - arr[k]) <= b) and \
                        (abs(arr[i] - arr[k]) <= c):
                    #if helper(arr[i], arr[j], arr[k]):
                        number_of_good_triplets += 1
        return number_of_good_triplets

print(Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))