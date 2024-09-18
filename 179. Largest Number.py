import itertools
from collections import defaultdict

class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        def helper(d):
            result = '0'
            for p in itertools.permutations(d):
                result = max(result, ''.join(str(n) * d[n] for n in p))
            print(result)
            return str(result)

        values = defaultdict(dict)
        for n in nums:
            values[str(n)[0]][n] = values[str(n)[0]].get(n, 0) + 1

        print(values)

        result = ''
        for v in sorted(values, reverse=True):
            result += helper(values[v])

        return str(int(result))

print(Solution().largestNumber(nums = [26,33,19,29,61,66,52,37,7,76,89,93,72,2,82,11,9,41,47,76,80,28,86,30,99,25,99,85,96,98,88,33,4,94,25,80,19,55,82,71,29,61,15,2,57,98,15,91,27,95,47,38,66,2,78,26,77,33,23,90,73,27,20,5,38,23,35,29,13,46,6,71,58,37,89,28,8,1,8,73,81,83,77,22,63,36,62,89,94,43,25,86,53,21,94,9,40,19,24,21]))