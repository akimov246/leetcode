class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operation in operations:
            match operation:
                case '--X' | 'X--':
                    x -= 1
                case '++X' | 'X++':
                    x += 1
        return x

print(Solution().finalValueAfterOperations(operations = ["--X","X++","X++"]))