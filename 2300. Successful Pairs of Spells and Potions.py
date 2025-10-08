from functools import cache

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = []
        potions.sort(reverse=True)

        @cache
        def search(spell):
            left = 0
            right = len(potions) - 1
            middle = (right + left) // 2

            while left <= right:
                product = spell * potions[middle]
                if product < success:
                    right = middle - 1
                else:
                    if middle == len(potions) - 1 or spell * potions[middle + 1] < success:
                        return middle + 1
                    else:
                        left = middle + 1
                middle = (right + left) // 2
            else:
                return 0

        for s in spells:
            pairs.append(search(s))

        return pairs


print(Solution().successfulPairs(spells = [1,2,3,4,5,6,7], potions = [1,2,3,4,5,6,7], success = 25))