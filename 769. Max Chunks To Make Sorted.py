class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        if arr == list(range(n)):
            return n
        chunks = 0
        for i in range(1, n + 1):
            if sorted(arr[:i]) == list(range(i)):
                chunks += 1

        return chunks


print(Solution().maxChunksToSorted(arr = [0,2,1,4,3]))