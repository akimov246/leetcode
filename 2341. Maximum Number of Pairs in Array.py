class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        pairs = 0
        leftover = 0
        for c in counter.values():
            if c % 2 == 0:
                pairs += c // 2
            else:
                leftover += 1
                pairs += (c - 1) // 2

        return [pairs, leftover]

print(Solution().numberOfPairs(nums = [1,3,2,1,3,2,2]))