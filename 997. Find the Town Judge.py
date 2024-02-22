from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        people = defaultdict(set)
        for pare in trust:
            people[pare[0]].add(pare[1])
        judge = set(range(1, n + 1)).difference(set(people.keys()))
        print(people.values())
        if len(judge) == 1:
            for p in people.values():
                if list(judge)[0] not in p:
                    return -1
        else:
            return -1
        return list(judge)[0]



print(Solution().findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print(3 in [{3, 5}])
