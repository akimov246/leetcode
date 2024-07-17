class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_ = 0
        for sentence in sentences:
            max_ = max(max_, len(sentence.split()))
        return max_

print(Solution().mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))