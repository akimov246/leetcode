class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        max_ = 0
        for s in strs:
            try:
                max_ = max(max_, int(s))
            except:
                max_ = max(max_, len(s))
        return max_

print(Solution().maximumValue(strs = ["alic3","bob","3","4","00000"]))