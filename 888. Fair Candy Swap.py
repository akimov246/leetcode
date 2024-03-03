class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        diff = (alice_sum - bob_sum) // 2
        A = set(aliceSizes)
        B = set(bobSizes)
        for a in A:
            if a - diff in B:
                return [a, a - diff]

print(Solution().fairCandySwap(aliceSizes = [1,1], bobSizes = [2,2]))