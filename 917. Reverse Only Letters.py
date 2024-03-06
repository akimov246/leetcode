from string import ascii_lowercase, ascii_uppercase

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        eng_letters = ascii_lowercase + ascii_uppercase
        s = list(s)
        ans = ["" if char in eng_letters else char for char in s]
        s = [char for char in s if char in eng_letters]
        for i in range(len(ans)):
            if not ans[i]:
                ans[i] = s.pop()
        return "".join(ans)



print(Solution().reverseOnlyLetters(s = "a-bC-dEf-ghIj"))