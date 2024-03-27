class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            y = stones.pop(stones.index(max(stones)))
            x = stones.pop(stones.index(max(stones)))
            if x != y:
                stones.append(y - x)
        return stones[0] if stones else 0

print(Solution().lastStoneWeight(stones = [2,7,4,1,8,1]))