class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr.pop() - arr[-1]
        for i in range(1, len(arr)):
            if arr[i] - diff != arr[i - 1]:
                return False
        return True

print(Solution().canMakeArithmeticProgression(arr = [3,5,1]))