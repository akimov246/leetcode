class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        names_height = sorted((zip(names, heights)), key=lambda pair: pair[-1], reverse=True)
        return [pair[0] for pair in names_height]

print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))