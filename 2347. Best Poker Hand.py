class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if all(suit == suits[0] for suit in suits[1:]):
            return 'Flush'
        counter = {}
        for r in ranks:
            counter[r] = counter.get(r, 0) + 1
        if sorted(counter.values())[-1] > 2:
            return "Three of a Kind"
        if sorted(counter.values())[-1] > 1:
            return 'Pair'
        return 'High Card'

print(Solution().bestHand(ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]))