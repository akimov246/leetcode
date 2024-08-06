class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = {}
        for char in word:
            counter[char] = counter.get(char, 0) + 1

        amounts = sorted(counter.values(), reverse=True)
        del counter

        pushes = 0

        for i, amount in enumerate(amounts):
            p = i // 8 + 1
            pushes += amount * p

        return pushes

print(Solution().minimumPushes(word = "aabbccddeeffgghhiiiiii"))