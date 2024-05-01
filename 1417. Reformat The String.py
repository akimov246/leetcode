from string import ascii_lowercase, digits

class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits_ = []
        for char in s:
            if char in ascii_lowercase:
                letters.append(char)
            elif char in digits:
                digits_.append(char)
        if abs(len(letters) - len(digits_)) > 1:
            return ''
        long = max(letters, digits_, key=len)
        short = letters if long == digits_ else digits_
        result = []
        for l in long:
            result.append(l)
            if short:
                result.append(short.pop())
        return ''.join(result)


print(Solution().reformat(s = "a0b1c2"))