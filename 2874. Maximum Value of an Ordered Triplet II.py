class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        prefix_max = dict()
        current_max = nums[0]
        for i in range(len(nums)):
            current_max = max(current_max, nums[i])
            prefix_max[i] = current_max
        #print(prefix_max)

        suffix_max = dict()
        current_max = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            current_max = max(current_max, nums[i])
            suffix_max[i] = current_max
        #print(suffix_max)

        result = 0
        for j in range(1, len(nums) - 1):
            result = max(result, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])

        return result

print(Solution().maximumTripletValue(nums = [1,10,3,4,19]))