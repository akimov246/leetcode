class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        flowers_need = m * k
        if flowers_need > len(bloomDay):
            return -1

        blooms = sorted(list(set(bloomDay)))
        left = 0
        right = len(blooms) - 1
        middle = (left + right) // 2

        def check(bloom: int) -> int:
            counter = 0
            bouquet = 0
            for day in bloomDay:
                if day <= bloom:
                    counter += 1
                    if counter == k:
                        bouquet += 1
                        counter = 0
                        if bouquet == m:
                            return bloom
                else:
                    counter = 0
            return 0

        days = -1
        while left <= right:
            if res := check(blooms[middle]):
                days = res
                right = middle - 1
                middle = (left + right) // 2
            else:
                left = middle + 1
                middle = (left + right) // 2
        return days



print(Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))