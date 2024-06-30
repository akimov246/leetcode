class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        counter = {}
        for d in digits:
            counter[d] = counter.get(d, 0) + 1
        result = []
        for d in range(100, 1000, 2):
            str_d = str(d)
            if all(str_d.count(e) <= counter.get(int(e), 0) for e in set(str_d)):
                result.append(d)

        return result

print(Solution().findEvenNumbers(digits = [2,2,8,8,2]))