class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counter = {}
        for char in arr:
            counter[char] = counter.get(char, 0) + 1
        c = 0
        for char, number in counter.items():
            if number == 1:
                c += 1
            if c == k:
                return char
        return ''

print(Solution().kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))