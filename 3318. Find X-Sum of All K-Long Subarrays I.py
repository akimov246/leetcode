class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        answer = []

        for i in range(n - k + 1):
            subarray = nums[i: i + k]
            elem__freq = {}
            for elem in subarray:
                elem__freq[elem] = elem__freq.get(elem, 0) + 1
            elem__freq = sorted(elem__freq.items(), key=lambda item: (-item[1], -item[0]))
            answer.append(sum(elem * freq for elem, freq in elem__freq[:x]))

        return answer

print(Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))