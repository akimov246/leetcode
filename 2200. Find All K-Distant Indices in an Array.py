class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        key_indices = []
        k_distant_indices = []
        for i in range(len(nums)):
            if nums[i] == key:
                key_indices.append(i)
        for i in range(len(nums)):
            for j in key_indices:
                if abs(i - j) <= k:
                    k_distant_indices.append(i)
                    break
        return k_distant_indices

print(Solution().findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))