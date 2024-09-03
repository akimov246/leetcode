class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        result = set(nums1) & set(nums2)
        return min(result) if result else -1

print(Solution().getCommon(nums1 = [1,2,3], nums2 = [2,4]))