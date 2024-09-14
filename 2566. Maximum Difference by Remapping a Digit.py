class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        max_ = num
        for n in num:
            if n != '9':
                max_ = max_.replace(n, '9')
                break
        min_ = num.replace(num[0], '0')
        return int(max_) - int(min_)


print(Solution().minMaxDifference(11891))