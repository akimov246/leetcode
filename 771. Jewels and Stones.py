class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for j in jewels:
            ans += stones.count(j)
        return ans

print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))