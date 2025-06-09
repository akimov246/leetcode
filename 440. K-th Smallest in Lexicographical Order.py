# Memory limit
import os
import psutil

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result = sorted(range(1, n + 1), key=lambda item: str(item))
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        print(memory_info.rss / 1024 ** 2)
        return result[k - 1]


print(Solution().findKthNumber(10065000, 8786251))