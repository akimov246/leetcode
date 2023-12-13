class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        counter = 0
        mem = None
        for num in nums:
            if num != mem:
                mem = num
                counter += 1
            if counter == 3:
                return num
        return nums[0]



print(Solution().thirdMax([2,1]))