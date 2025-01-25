from collections import defaultdict


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_nums = sorted(nums)
        num_to_group = {}
        group_to_list = defaultdict(list)

        group_idx = 0
        num_to_group[sorted_nums[0]] = group_idx
        group_to_list[group_idx].append(sorted_nums[0])
        for i in range(1, len(sorted_nums)):
            if abs(sorted_nums[i] - sorted_nums[i - 1]) > limit:
                group_idx += 1
            num_to_group[sorted_nums[i]] = group_idx
            group_to_list[group_idx].append(sorted_nums[i])

        group_to_list_iters = {group_idx: iter(values) for group_idx, values in group_to_list.items()}
        result = []
        for n in nums:
            group_idx = num_to_group[n]
            result.append(next(group_to_list_iters[group_idx]))

        return result


print(Solution().lexicographicallySmallestArray(nums=[1, 11, 6, 2, 4, 9, 14], limit=2))
