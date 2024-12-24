class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        k = set(range(1, k + 1))
        operations = 0
        for n in nums[::-1]:
            if n in k:
                k.remove(n)
            operations += 1
            if not k:
                return operations

print(Solution().minOperations(nums = [3,1,5,4,2], k = 2))