class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        bits = "".join(str(bit) for bit in bits[:len(bits) - 1])
        i = 0
        while i < len(bits):
            if bits[i] == '0':
                i += 1
            else:
                if bits[i:i+2] not in ['11', '10']:
                    return False
                i += 2
        return True

print(Solution().isOneBitCharacter([0,0]))