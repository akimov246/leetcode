class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        result = 0
        max_score = 0
        divisors.sort()
        for d in divisors:
            current_score = 0
            for n in nums:
                if n % d == 0:
                    current_score += 1
            if current_score > max_score:
                max_score = current_score
                result = d
        return result if result else divisors[0]

print(Solution().maxDivScore(nums = [20,14,21,10], divisors = [10,16,20]))