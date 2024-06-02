class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        s = s.split()
        for word in s:
            words[word[-1]] = word[:-1]
        words = dict(sorted(words.items(), key=lambda item: item[0]))
        return ' '.join(words.values())

print(Solution().sortSentence(s = "is2 sentence4 This1 a3"))