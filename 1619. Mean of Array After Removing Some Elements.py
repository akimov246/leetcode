class Solution:
    def trimMean(self, arr: list[int]) -> float:
        number_elements_to_remove = int(len(arr) * 0.05)
        arr.sort()
        arr = arr[number_elements_to_remove:-number_elements_to_remove]

        return sum(arr) / len(arr)


print(Solution().trimMean(arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))