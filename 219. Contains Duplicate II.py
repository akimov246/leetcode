class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            j = seen.get(nums[i], -1)
            if j >= 0:
                if abs(i - j) <= k:
                    return True
            seen[nums[i]] = i

        return False

print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

