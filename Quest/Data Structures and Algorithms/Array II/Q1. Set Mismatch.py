class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        counter = {n: 0 for n in range(1, len(nums) + 1)}
        result = []
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] == 2:
                result.append(n)

        for n, c in counter.items():
            if c == 0:
                result.append(n)
                return result

print(Solution().findErrorNums([1, 2, 2, 4]))