class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        short = min(nums1, nums2, key=len)
        if short is nums1:
            long = nums2
        else:
            long = nums1
        for num in short:
            if num in long:
                res.append(num)
                long.remove(num)
        return res

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        # [1, 1, 2, 2]
        # [2, 2]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

#print(Solution().intersect([1, 2, 2, 1], [2, 2]))
print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))