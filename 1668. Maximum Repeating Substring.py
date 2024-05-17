class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        while True:
            if sequence.find(word * k) == -1:
                return k - 1
            k += 1

print(Solution().maxRepeating(sequence = "ababc", word = "ab"))