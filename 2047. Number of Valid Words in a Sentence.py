import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile('([a-z]+[-]?[a-z]+[!.,]?)|([a-z]*[!.,]?)')
        counter = 0
        for word in sentence.split():
            if pattern.fullmatch(word):
                counter += 1
        return counter

print(Solution().countValidWords(". ! 7hk  al6 l! aon49esj35la k3 7u2tkh  7i9y5  !jyylhppd et v- h!ogsouv 5"))