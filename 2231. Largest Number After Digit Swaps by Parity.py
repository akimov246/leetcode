class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        odds = []
        evens = []
        parity = {}
        for i in range(len(num)):
            if int(num[i]) % 2:
                parity[i] = 1
                odds.append(num[i])
            else:
                parity[i] = 0
                evens.append(num[i])
        odds.sort()
        evens.sort()
        #print(odds, evens, parity)
        value = ''
        for i in range(len(num)):
            if parity[i]:
                value += odds.pop()
            else:
                value += evens.pop()

        return int(value)

print(Solution().largestInteger(1234))