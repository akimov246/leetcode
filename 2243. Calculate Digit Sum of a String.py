class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = (s[i:i + k] for i in range(0, len(s), k))
            tmp_s = ''
            for group in groups:
                tmp_s += str(sum(int(n) for n in group))
            s = tmp_s

        return s

print(Solution().digitSum(s = "11111222223", k = 3))