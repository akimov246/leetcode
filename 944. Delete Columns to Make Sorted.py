class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        ans = 0
        for col in zip(*strs):
            if col != tuple(sorted(col)):
                ans += 1
        return ans

print(Solution().minDeletionSize(strs = ["cba","daf","ghi"]))