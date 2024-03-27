# Моё решение (медленное)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                if i != 0:
                    i -= 1
            else:
                i += 1
        return s

# Решение с leetcode
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]
        for a in s:
            if(len(ans)>0 and ans[-1]==a):
                ans.pop()
            else:
                ans.append(a)
        return("".join(ans))

print(Solution().removeDuplicates(s = "aaaaaaaa"))