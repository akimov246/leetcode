class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        mmm = 0
        brokenLetters = set(brokenLetters)
        for word in text.split():
            if not set(word) & brokenLetters:
                mmm +=1
        return mmm

print(Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad"))