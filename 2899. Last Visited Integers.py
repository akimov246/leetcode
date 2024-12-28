class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        seen = []
        ans = []
        k_counter = 0
        for n in nums:
            if n > 0:
                seen.insert(0, n)
                k_counter = 0
            elif n == -1:
                k_counter += 1
                if k_counter <= len(seen):
                    ans.append(seen[k_counter - 1])
                else:
                    ans.append(-1)

        return ans


print(Solution().lastVisitedIntegers(nums = [1,2,-1,-1,-1]))