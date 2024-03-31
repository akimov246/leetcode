class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        target = len(arr) * 0.25
        count = dict()
        for num in arr:
            count[num] = count.get(num, 0) + 1
            if count[num] > target:
                return num

print(Solution().findSpecialInteger(arr = [1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))