from itertools import chain

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        result = []
        for value in set(chain(nums1, nums2, nums3)):
            counter = 0
            if value in nums1:
                counter += 1
            if value in nums2:
                counter += 1
            if value in nums3:
                counter += 1
            if counter > 1:
                result.append(value)
        return result

print(Solution().twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))