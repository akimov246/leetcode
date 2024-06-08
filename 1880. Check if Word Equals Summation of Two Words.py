from string import ascii_lowercase
from itertools import zip_longest

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letter_value = dict((letter, str(value)) for letter, value in zip(ascii_lowercase, range(len(ascii_lowercase))))
        letter_value.update({'':''})
        f_value = ''
        s_value = ''
        t_value = ''
        for f, s, t in zip_longest(firstWord, secondWord, targetWord, fillvalue=''):
            f_value += letter_value[f]
            s_value += letter_value[s]
            t_value += letter_value[t]
        return int(f_value) + int(s_value) == int(t_value)

print(Solution().isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cd"))