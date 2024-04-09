class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        res = []
        while s:
            set_ = set(s)
            while set_:
                min_ = min(set_)
                res.append(min_)
                set_.remove(min_)
                s.remove(min_)
            set_ = set(s)
            while set_:
                max_ = max(set_)
                res.append(max_)
                set_.remove(max_)
                s.remove(max_)
        return ''.join(res)


print(Solution().sortString(s = "aaaabbbbcccc"))