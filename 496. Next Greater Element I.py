class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for x in nums1:
            mem = len(ans)
            for i in range(nums2.index(x), len(nums2)):
                if nums2[i] > x:
                    ans.append(nums2[i])
                    break
            if len(ans) == mem:
                ans.append(-1)
        return ans

print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))