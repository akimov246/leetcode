class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance = len(arr1)
        for num in arr1:
            for n in arr2:
                if abs(num - n) < d:
                    distance -= 1
                    break
        return distance

print(Solution().findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))