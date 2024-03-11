class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        range_ = [n for n in range(len(s) + 1)]
        perm = []
        for char in s:
            match char:
                case 'I':
                    perm.append(range_.pop(0))
                case 'D':
                    perm.append(range_.pop())
                case _:
                    raise ValueError
        perm.append(range_[0])
        return perm


print(Solution().diStringMatch(s = "IDID"))