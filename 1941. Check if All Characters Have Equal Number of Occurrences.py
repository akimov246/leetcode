class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        #return all(tuple(counter.values())[0] == value for value in counter.values())
        return len(set(counter.values())) == 1

print(Solution().areOccurrencesEqual(s = "abacbc"))