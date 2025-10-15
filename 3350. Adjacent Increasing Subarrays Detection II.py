class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        subarrays = []
        result = 0

        start_idx = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                subarrays.append(nums[start_idx: i])
                start_idx = i
        subarrays.append(nums[start_idx: i + 1])

        for i in range(len(subarrays) - 1):
            result = max(result, len(min(subarrays[i + 1], subarrays[i], key=len)))
            result = max(result, len(subarrays[i]) // 2)
        result = max(result, len(subarrays[-1]) // 2)

        return result


print(Solution().maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1]))