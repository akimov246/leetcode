class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        f = "Fizz"
        b = "Buzz"
        ans = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                ans.append(f + b)
            elif not i % 3:
                ans.append(f)
            elif not i % 5:
                ans.append(b)
            else:
                ans.append(str(i))
        return ans


print(Solution().fizzBuzz(3))