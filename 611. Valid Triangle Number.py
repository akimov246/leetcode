class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        valid = 0

        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    valid += j - i
                    j -= 1
                else:
                    i += 1

        return valid


print(Solution().triangleNumber([2,5,6,7,9]))