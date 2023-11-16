class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        if len(nums) == 1:
            return "1" if "0" in nums else "0"
        nums_gen = (str(bin(i))[2:].ljust(len(nums), "0") for i in range(len(nums) * len(nums)))
        for num in nums_gen:
            if num not in nums:
                return num




nums = ["01", "10"]
print(Solution().findDifferentBinaryString(nums))