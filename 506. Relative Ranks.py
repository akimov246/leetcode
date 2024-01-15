class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        gold = 'Gold Medal'
        silver = 'Silver Medal'
        bronze = 'Bronze Medal'
        sorted_score = sorted(score, reverse=True)
        d = dict()
        for place in range(len(sorted_score)):
            if place == 0:
                d[sorted_score[place]] = gold
            elif place == 1:
                d[sorted_score[place]] = silver
            elif place == 2:
                d[sorted_score[place]] = bronze
            else:
                d[sorted_score[place]] = str(place + 1)
        return [d[s] for s in score]

print(Solution().findRelativeRanks([10,3,8,9,4]))