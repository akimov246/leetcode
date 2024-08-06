class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        triplets = 0
        for i in range(1, len(nums) - 1):
            if nums[i] - diff in nums and nums[i] + diff in nums:
                triplets += 1
        return triplets

print(Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))