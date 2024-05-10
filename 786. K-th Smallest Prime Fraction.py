class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        answer = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                answer.append([arr[i], arr[j]])
        answer.sort(key=lambda nums: nums[0] / nums[1])
        return answer[k - 1]

print(Solution().kthSmallestPrimeFraction(arr = [1,3,11,13,37,53,59], k = 6))