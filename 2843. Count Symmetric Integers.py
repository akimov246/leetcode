class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for x in range(low, high + 1):
            if len(str(x)) % 2 == 0:
                left = str(x)[:len(str(x)) // 2]
                right = str(x)[len(str(x)) // 2:]
                if sum(int(d) for d in left) == sum(int(d) for d in right):
                    result += 1

        return result

print(Solution().countSymmetricIntegers(low = 1, high = 100))