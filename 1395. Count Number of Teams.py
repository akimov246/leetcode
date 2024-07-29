from itertools import zip_longest

class Solution:
    def numTeams(self, rating:list[int]) -> int:

        counter = 0

        for middle in range(1, len(rating) - 1):
            left_lower = 0
            left_higher = 0
            right_lower = 0
            right_higher = 0
            for left, right in zip_longest(range(middle), range(middle + 1, len(rating))):
                if left is not None:
                    if rating[left] < rating[middle]:
                        left_lower += 1
                    else:
                        left_higher += 1
                if right is not None:
                    if rating[right] < rating[middle]:
                        right_lower += 1
                    else:
                        right_higher += 1

            counter += left_lower * right_higher + left_higher * right_lower

        return counter


print(Solution().numTeams(rating = [2,5,3,4,1]))
