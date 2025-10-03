class Solution:
    def isBalanced(self, num: str) -> bool:
        balance = 0
        for i in range(len(num)):
            if i % 2:
                balance += int(num[i])
            else:
                balance -= int(num[i])

        return not bool(balance)


print(Solution().isBalanced(num = "24123"))