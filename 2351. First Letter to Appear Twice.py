class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = {}
        for char in s:
            c = counter.get(char, 0)
            if c == 1:
                return char
            counter[char] = c + 1

print(Solution().repeatedCharacter(s = "abccbaacz"))