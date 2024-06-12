from string import ascii_lowercase

class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        pointer = 'a'
        i = 0
        while i < len(word):
            if word[i] != pointer:
                pntr_idx = ascii_lowercase.index(pointer)
                clockwise = ascii_lowercase[pntr_idx:] + ascii_lowercase[:pntr_idx]
                counterclockwise = clockwise[0] + clockwise[1:][::-1]
                for shift, (cw, ccw) in enumerate(zip(clockwise, counterclockwise)):
                    if word[i] in [cw, ccw]:
                        seconds += shift
                        break
                #seconds += min(clockwise.index(word[i]), counterclockwise.index(word[i]))
                pointer = word[i]
            else:
                seconds += 1
                i += 1

        return seconds


print(Solution().minTimeToType('bza'))