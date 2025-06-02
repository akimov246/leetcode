class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        operations = 0
        score = None

        while len(nums) > 1:
            if score is None:
                score = sum(nums[:2])
            else:
                if sum(nums[:2]) != score:
                    break
            nums = nums[2:]
            operations += 1

        return operations


print(Solution().maxOperations(nums = [3,2,1,4,5]))