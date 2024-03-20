class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        arr = tuple(arr)
        total = sum(arr)
        for i in range(1, len(arr)):
            for j in range(2, len(arr)):
                if i < j:
                    a = arr[:i]
                    b = arr[i:j]
                    c = arr[j:]
                    count = sorted((a, b, c), key=len)
                    s1 = sum(count[0])
                    s2 = sum(count[1])
                    if s1 == s2 == (total - s1 -s2):
                        return True


        return False

print(Solution().canThreePartsEqualSum(arr = [12,-4,16,-5,9,-3,3,8,0]))