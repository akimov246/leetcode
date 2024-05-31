class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])

print(Solution().truncateSentence(s = "Hello how are you Contestant", k = 4))