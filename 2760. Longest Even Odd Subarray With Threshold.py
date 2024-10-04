class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        result = 1 if any(n % 2 == 0 and n <= threshold for n in set(nums)) else 0
        #result = 0

        for l in range(len(nums)):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                for i in range(l + 1, len(nums)):
                    if nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                        result = max(result, i - l + 1)
                    else:
                        break

        return result

print(Solution().longestAlternatingSubarray(nums = [4,10,3], threshold = 10))