class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        res = 0
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            res += 1
        return res

print(Solution().countQuadruplets(nums = [1,1,1,3,5]))