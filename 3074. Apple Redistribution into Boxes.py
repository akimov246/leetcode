class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        result = 0
        for c in capacity:
            total_apples -= c
            result += 1
            if total_apples <=0:
                return result

print(Solution().minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2]))