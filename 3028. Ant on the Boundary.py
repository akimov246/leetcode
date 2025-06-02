class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        returns_to_the_boundary = 0
        counter = 0
        for n in nums:
            counter += n
            if not counter:
                returns_to_the_boundary += 1

        return returns_to_the_boundary



print(Solution().returnToBoundaryCount(nums = [2,3,-5]))