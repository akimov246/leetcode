class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        if sentence[0][0] == sentence[-1][-1]:
            for i in range(1, len(sentence)):
                if sentence[i][0] != sentence[i - 1][-1]:
                    return False
            return True
        else:
            return False

print(Solution().isCircularSentence(sentence = "leetcode exercises sound delightful"))