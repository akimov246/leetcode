class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        counter = {}
        for n in nums:
            if n % 2 == 0:
                counter[n] = counter.get(n, 0) + 1

        return sorted(counter.items(), key=lambda item: (item[1], -item[0]), reverse=True)[0][0] if counter else -1

print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))