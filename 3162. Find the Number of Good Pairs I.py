class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        good_pairs_counter = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    good_pairs_counter += 1
        return good_pairs_counter

print(Solution().numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))