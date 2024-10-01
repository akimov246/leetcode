class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        sum_ = sum(arr)
        if sum_ % k:
            return False
        elif all(n > 0 for n in arr) and sum_ < k * len(arr) // 2:
            return False

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if (arr[i] + arr[j]) % k == 0:
                        return True
            else:
                return False

        return True


print(Solution().canArrange(arr = [8,6,3,3], k = 9))