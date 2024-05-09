class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs_counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs_counter += 1
        return good_pairs_counter

print(Solution().numIdenticalPairs(nums = [1,2,3,1,1,3]))