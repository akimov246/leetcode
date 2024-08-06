class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        if len(nums) > 2:
            subarrays = set()
            for i in range(2, len(nums) + 1):
                current = nums[i - 2:i]
                sum_ = sum(current)
                if sum_ in subarrays:
                    return True
                subarrays.add(sum_)
        return False

print(Solution().findSubarrays(nums = [77,95,90,98,8,100,88,96,6,40,86,56,98,96,40,52,30,33,97,72,54,15,33,77,78,8,21,47,99,48]))