class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        c = {child: 1 for child in range(children)}
        money -= children
        while money:
            for child in range(children):
                if c[child] != 8:
                    if money >= 7:
                        money -= 7
                        c[child] += 7
                    else:
                        c[child] += money
                        money = 0
            else:
                c[children - 1] += money
                money = 0
        c = list(c.values())
        while 4 in c:
            idx = c.index(4)
            c[idx] -= 1
            if idx + 1 < len(c):
                c[idx + 1] += 1
            elif idx - 1 > -1:
                c[idx - 1] += 1

        return c.count(8)

print(Solution().distMoney(money = 24, children = 2))