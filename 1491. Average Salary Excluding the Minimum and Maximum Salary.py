class Solution:
    def average(self, salary: list[int]) -> float:
        min_ = min(salary)
        max_ = max(salary)
        sum_ = sum(salary) - min_ - max_
        return sum_ / (len(salary) - 2)

print(Solution().average(salary = [4000,3000,1000,2000]))