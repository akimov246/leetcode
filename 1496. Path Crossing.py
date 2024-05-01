class Solution:
    def isPathCrossing(self, path: str) -> bool:
        position = [0, 0]
        visited = set()
        visited.add(tuple(position))
        for direction in path:
            match direction:
                case 'N':
                    position[1] += 1
                case 'E':
                    position[0] += 1
                case 'S':
                    position[1] -= 1
                case 'W':
                    position[0] -= 1
            if tuple(position) in visited:
                return True
            visited.add(tuple(position))
        return False

print(Solution().isPathCrossing(path = "NESWW"))