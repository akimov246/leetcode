class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        answer = []
        specials = [0]
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                specials.append(i)
                specials.append(i)
        specials.append(len(nums))
        print(specials)
        specials = set(range(specials[i], specials[i + 1]) for i in range(0, len(specials), 2))
        print(specials)

        for (from_, to_) in queries:
            f = None
            t = None
            for i, s in enumerate(specials):
                if from_ in s:
                    f = i
                if to_ in s:
                    t = i
                if f is not None or t is not None:
                    if f == t:
                        answer.append(True)
                    else:
                        answer.append(False)
                    break

        return answer


print(Solution().isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))