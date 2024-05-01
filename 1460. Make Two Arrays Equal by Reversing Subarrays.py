class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        t_counter = {}
        a_counter = {}
        for t, a in zip(target, arr):
            t_counter[t] = t_counter.get(t, 0) + 1
            a_counter[a] = a_counter.get(a, 0) + 1

        return frozenset(t_counter.items()) == frozenset(a_counter.items())

print(Solution().canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))