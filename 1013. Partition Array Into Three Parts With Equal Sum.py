class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        for i in range(1, len(arr)):
            a = sum(arr[:i])
            j = i + 1
            if a and (total - a) % a:
                continue
            b = arr[i]
            while j < len(arr):
                if a == b:
                    if sum(arr[j:]) == a:
                        return True
                b += arr[j]
                j += 1

        return False

print(Solution().canThreePartsEqualSum(arr = [3,3,6,5,-2,2,5,1,-9,4]))