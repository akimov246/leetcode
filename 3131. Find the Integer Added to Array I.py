class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        min1 = min(nums1)
        min2 = min(nums2)
        return min2 - min1

print(Solution().addedInteger(nums1 = [2,6,4], nums2 = [9,7,5]))