from string import ascii_lowercase

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {str(n):str(letter) for n, letter in zip(range(1, 27), ascii_lowercase)}
        for i in range(10, len(alphabet) + 1):
            alphabet[str(i) + '#'] = alphabet.pop(str(i))
        dec = ''
        i = len(s) - 1
        while i > -1:
            if s[i] == '#':
                dec += alphabet[s[i-2:i + 1]]
                i -= 3
            else:
                dec += alphabet[s[i]]
                i -= 1
        return dec[::-1]

print(Solution().freqAlphabets(s = "10#11#12"))