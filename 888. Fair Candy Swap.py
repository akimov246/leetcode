class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        for a in set(aliceSizes):
            for b in set(bobSizes):
                if alice_sum - a + b == bob_sum - b + a:
                    return [a, b]
                aliceSizes.append(a)
                bobSizes.append(b)



print(Solution().fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))