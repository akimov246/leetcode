class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) < 5:
            return 0

        nums.sort()
        print(nums)

        way1 = max(nums[3:]) - min(nums[3:])
        way2 = max(nums[2:-1]) - min(nums[2:-1])
        way3 = max(nums[1:-2]) - min(nums[1:-2])
        way4 = max(nums[:-3]) - min(nums[:-3])

        return min(way1, way2, way3, way4)

print(Solution().minDifference(nums = [1,5,0,10,14]))