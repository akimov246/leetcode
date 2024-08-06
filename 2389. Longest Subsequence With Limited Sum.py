class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        answer = []

        nums.sort()
        sum_ = sum(nums)
        for query in queries:
            tmp_sum = sum_
            array = nums.copy()
            while tmp_sum > query:
                tmp_sum -= array.pop()
            answer.append(len(array))

        return answer


print(Solution().answerQueries(nums = [736411,184882,914641,37925,214915], queries = [331244,273144,118983,118252,305688,718089,665450]))