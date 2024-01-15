class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        counter = 0
        for i in range(0, len(s), k):
            x = s[i:i + k]
            #print(x)
            if counter % 2 == 0:
                ans += x[::-1]
            else:
                ans += x
            counter += 1
        return ans

print(Solution().reverseStr('abcdefg', 2))