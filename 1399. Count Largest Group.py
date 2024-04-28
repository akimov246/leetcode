from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(set)
        #max_len = 0
        for number in range(1, n + 1):
            sum_ = sum((int(x) for x in str(number)))
            groups[sum_].add(number)
            #max_len = max(max_len, len(groups[sum_]))
        max_len = len(max(groups.values(), key=len))
        ans = 0
        for g in groups.values():
            if len(g) == max_len:
                ans += 1
        return ans

print(Solution().countLargestGroup(13))