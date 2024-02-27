from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        for char in set(paragraph):
            if char in "!?',;.":
                paragraph = paragraph.replace(char, ' ')
        words = paragraph.split()
        words_frequency = defaultdict(int)
        for i in range(len(words)):
            if words[i] not in banned:
                words_frequency[words[i]] += 1

        ans = sorted(words_frequency.items(), key=lambda item: item[1])[-1]
        return ans[0]

print(Solution().mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))