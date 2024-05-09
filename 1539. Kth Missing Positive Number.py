class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        arr = set(arr)
        range_ = set(range(1, max(arr) + k + 1))
        diff = sorted(list(range_.difference(arr)))
        return diff[k - 1]

print(Solution().findKthPositive(arr = [1,2], k = 8))