class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k:
            bag = [-1] * numNegOnes
            bag.extend([0] * numZeros)
            bag.extend([1] * numOnes)
            return sum(bag[-k:])
        else:
            return 0

print(Solution().kItemsWithMaximumSum(numOnes = 2, numZeros = 4, numNegOnes = 4, k = 0))