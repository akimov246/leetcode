class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        new_code = []
        if k > 0:
            for i in range(len(code)):
                new_value = 0
                for j in range(i + 1, i + 1 + k):
                    new_value += code[j % len(code)]
                new_code.append(new_value)
        elif k < 0:
            for i in range(len(code)):
                new_value = 0
                j = i - 1
                for _ in range(abs(k)):
                    new_value += code[j % len(code)]
                    j -= 1
                new_code.append(new_value)
        else:
            return [0] * len(code)

        return new_code



print(Solution().decrypt(code = [10,5,7,7,3,2,10,3,6,9,1,6], k = -4))