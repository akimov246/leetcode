import operator

from functools import reduce

class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        result = 0
        length = 2
        while length < len(arr) + 1:
            for i in range(len(arr)):
                if length + i == len(arr) + 1:
                    break
                if reduce(operator.xor, arr[i:i + length]) == 0:
                    result += length - 1
            length += 1

        return result

print(Solution().countTriplets(arr = [2,3,1,6,7]))