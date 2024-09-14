from math import sqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        for _ in range(k):
            idx = gifts.index(max(gifts))
            gifts[idx] = int(sqrt(gifts[idx]))
        return sum(gifts)

print(Solution().pickGifts(gifts = [25,64,9,4,100], k = 4))