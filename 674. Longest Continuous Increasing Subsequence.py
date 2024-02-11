class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:

        def helper(start_idx: int, nums: list[int]):
            counter = 1
            prev_idx = start_idx
            curr_idx = prev_idx + 1
            while curr_idx < len(nums):
                if nums[prev_idx] < nums[curr_idx]:
                    counter += 1
                else:
                    break
                prev_idx += 1
                curr_idx = prev_idx + 1
            return counter

        ans = 1
        for i in range(len(nums)):
            ans = max(ans, helper(i, nums))
        return ans





print(Solution().findLengthOfLCIS(nums = [1,3,5,4,2,3,4,5]))