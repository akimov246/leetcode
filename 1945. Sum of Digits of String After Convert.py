from string import ascii_lowercase

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = {letter:str(n) for letter, n in zip(ascii_lowercase, range(1, len(ascii_lowercase) + 1))}
        convert = ''
        for char in s:
            convert += alphabet[char]
        for _ in range(k):
            convert = str(sum(int(val) for val in convert))
        return int(convert)

print(Solution().getLucky(s = "iiii", k = 1))