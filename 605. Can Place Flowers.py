class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return True if (flowerbed[0] == 0 and n >= 1 or n == 0) else False
        i = 0
        while i != len(flowerbed):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if (i == 0 and flowerbed[i + 1] == 0) or \
                   (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0) or \
                   (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                        flowerbed[i] = 1
                        n -= 1
            i += 1

        return True if n <= 0 else False

print(Solution().canPlaceFlowers([0,0,1,0,0], 1))