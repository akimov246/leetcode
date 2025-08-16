class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        result = 0
        for command in commands:
            match command:
                case 'UP':
                    result -= n
                case 'DOWN':
                    result += n
                case 'LEFT':
                    result -= 1
                case 'RIGHT':
                    result += 1
        return result


print(Solution().finalPositionOfSnake(n = 2, commands = ["RIGHT","DOWN"]))