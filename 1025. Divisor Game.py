class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1 or n == 3:
            return False
        if n == 2:
            return True

        divs = set()
        for i in range(1, n):
            if n % i == 0:
                divs.add(i)

        print(divs)



print(Solution().divisorGame(6))