from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = Counter(nums).most_common(1)[0][0]
        loss = set([value for value in range(1, len(nums) + 1)]).difference(set(nums))
        return [duplicate, *loss]

print(Solution().findErrorNums([1,1]))