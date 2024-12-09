class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        specials = {0: [True]}
        indexes = []

        def make_specials(idx, first=True):
            for i in range(idx + 1, len(nums)):
                if nums[i] % 2 != nums[i - 1] % 2:
                    specials[idx].append(True)
                else:
                    specials[idx].append(False)
                    if first:
                        indexes.append(i)

        make_specials(0)
        print(specials)
        print(indexes)
        for i in indexes:
            specials[i] = [True]
            make_specials(i, False)
        print(specials)

print(Solution().isArraySpecial(nums = [2,8,10,9], queries = [[1,3]]))