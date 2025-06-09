class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            n = str(n)
            n = max(n) * len(n)
            result += int(n)

        return result

print(Solution().sumOfEncryptedInt(nums = [10,21,31]))