class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter = {}
        for a in arr:
            counter[a] = counter.get(a, 0) + 1
        return len(counter.values()) == len(set(counter.values()))

print(Solution().uniqueOccurrences(arr = [1,2,2,1,1,3]))