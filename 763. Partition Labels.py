class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        result = []

        def helper(string):
            for i in range(1, len(string) + 1):
                for char in set(string[:i]):
                    if char in string[i:]:
                        break
                else:
                    result.append(i)
                    return helper(string[i:])

        helper(s)
        return result

print(Solution().partitionLabels(s = "ababcbacadefegdehijhklij"))