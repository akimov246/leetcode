class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = list(range(1, len(pattern) + 2))

        def helper(nums: list, n, p_idx=0, value=''):
            value += str(n)
            nums.remove(n)
            if len(value) == len(pattern) + 1:
                return value

            char = pattern[p_idx]
            if char == 'I':
                for num in nums:
                    if num > n:
                        result = helper(nums.copy(), num, p_idx + 1, value)
                        if result:
                            return result
            elif char == 'D':
                for num in nums:
                    if num < n:
                        result = helper(nums.copy(), num, p_idx + 1, value)
                        if result:
                            return result

        for n in nums:
            result = helper(nums.copy(), n)
            if result:
                return result


#print(Solution().smallestNumber(pattern = "DDDIII"))
#print(Solution().smallestNumber(pattern = "IIIDIDDD"))
for n in range(256):
    pattern1 = bin(n)[2:].replace('1', 'D').replace('0', 'I')
    pattern2 = bin(n)[2:].replace('1', 'I').replace('0', 'D')
    #print(pattern1)
    #print(pattern2)
    print(Solution().smallestNumber(pattern1))
    print(Solution().smallestNumber(pattern2))