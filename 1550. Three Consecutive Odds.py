class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 and len(arr[i:i+3]) == 3 and all(n % 2 for n in arr[i + 1: i + 3]):
                return True
        return False


print(Solution().threeConsecutiveOdds(arr = [2,6,4,1]))