class Solution:
    def isHappy(self, n: int) -> bool:
        was = set()
        tmp = 0
        while n != 1:
            for num in str(n):
                tmp += int(num) * int(num)
            if tmp in was:
                return False
            was.add(tmp)
            n = tmp
            tmp = 0
        return True

print(Solution().isHappy(19))