class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer1 = 0
        answer2 = 0
        for n in nums1:
            if n in nums2:
                answer1 += 1
        for n in nums2:
            if n in nums1:
                answer2 += 1
        return [answer1, answer2]

print(Solution().findIntersectionValues(nums1 = [2,3,2], nums2 = [1,2]))