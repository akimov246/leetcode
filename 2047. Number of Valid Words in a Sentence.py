import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile('\d+-?\d+')

print(Solution().countValidWords(sentence = "cat and  dog"))