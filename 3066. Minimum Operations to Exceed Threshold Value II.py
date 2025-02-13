class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        operations = 0
        lt = []
        min_gt = float('inf')

        for n in nums:
            if n < k:
                lt.append(n)
            else:
                min_gt = min(min_gt, n)

        lt.sort(reverse=True)

        while lt:
            operations += 1
            x = lt.pop()
            if not lt:
                y = min_gt
            else:
                y = lt.pop()
            value = x * 2 + y
            if value < k:
                if not lt or len(lt) == 1:
                    lt.append(value)
                    continue
                if lt[0] <= value:
                    lt.insert(0, value)
                    continue
                if lt[-1] >= value:
                    lt.append(value)
                    continue
                left = 0
                right = len(lt) - 1
                middle = (left + right) // 2
                while True:
                    if lt[middle] >= value and lt[middle + 1] <= value:
                        lt.insert(middle + 1, value)
                        break
                    if lt[middle] > value:
                        left = middle + 1
                    elif lt[middle] < value:
                        right = middle - 1
                    middle = (left + right) // 2
            else:
                min_gt = min(min_gt, value)

        return operations


print(Solution().minOperations(nums = [22,53,55,52,8,44,19,97,8], k = 92))