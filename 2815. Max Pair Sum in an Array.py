from collections import defaultdict

class Solution:
    def maxSum(self, nums: list[int]) -> int:
        d = defaultdict(list)
        for n in nums:
            d[max(str(n))].append(n)

        result = -1

        for key in d:
            d[key] = sorted(d[key])
            if len(d[key]) > 1:
                result = max(result, sum(d[key][-2:]))

        return result

print(Solution().maxSum([51,71,17,24,42]))