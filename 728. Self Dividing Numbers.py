class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for num in range(left, right + 1):
            if '0' not in str(num):
                if all(num % int(n) == 0 for n in set(str(num))):
                    print(num)
                    ans.append(num)

        return ans

print(Solution().selfDividingNumbers(left=1, right=123456789))