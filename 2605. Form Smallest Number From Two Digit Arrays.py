class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        if s := set(nums1) & set(nums2):
            return min(s)

        min1 = min(nums1)
        min2 = min(nums2)
        return int(str(min(min1, min2)) + str(max(min1, min2)))

print(Solution().minNumber(nums1 = [4,1,3], nums2 = [5,7]))