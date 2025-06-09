class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        nums.reverse()
        arr1 = [nums.pop()]
        arr2 = [nums.pop()]

        while nums:
            if arr1[-1] > arr2[-1]:
                arr1.append(nums.pop())
            else:
                arr2.append(nums.pop())

        return arr1 + arr2


print(Solution().resultArray(nums = [2,1,3]))