class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        prefix = strs[0]
        prev_prefix = None
        while True:
            if prefix == prev_prefix:
                return prefix
            prev_prefix = prefix
            for word in strs:
                if not word.startswith(prefix):
                    prefix = prefix[:len(prefix) - 1]
                    break




print(Solution().longestCommonPrefix(["flower","flow","flight"]))