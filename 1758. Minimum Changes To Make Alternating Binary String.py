class Solution:
    def minOperations(self, s: str) -> int:
        # model1 = ('1' if i % 2 else '0' for i in range(len(s)))
        # model2 = ('0' if i % 2 else '1' for i in range(len(s)))

        def model():
            while True:
                yield ('0', '1')
                yield ('1', '0')

        diff1 = 0
        diff2 = 0

        for x, m in zip(s, model()):
            if x != m[0]:
                diff1 += 1
            if x != m[1]:
                diff2 += 1
        return min(diff1, diff2)

print(Solution().minOperations(s = "10010100"))