class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_idx = 0
        end_idx = len(s)
        polindroms = set()
        max_len_polindrom = 0
        while start_idx != end_idx:
            if max_len_polindrom < len(s[start_idx:end_idx]) and s[start_idx:end_idx] == s[start_idx:end_idx][::-1]:
                polindroms.add(s[start_idx:end_idx])
                max_len_polindrom = max(max_len_polindrom, len(s[start_idx:end_idx]))
            end_idx -= 1
            if start_idx == end_idx:
                start_idx += 1
                end_idx = len(s)
        return max(polindroms, key=len)



print(Solution().longestPalindrome(s = "cbbd"))