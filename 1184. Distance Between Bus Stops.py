class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        n = len(distance)
        def clockwise(current, destination, dist: int = 0):
            if current == destination:
                return dist
            dist += distance[current % n]
            return clockwise((current + 1) % n, destination, dist)

        def counterclockwise(current, destination, dist: int = 0):
            if current == destination:
                return dist
            dist += distance[(current - 1) % n]
            return counterclockwise((current - 1) % n, destination, dist)

        return min(clockwise(start, destination), counterclockwise(start, destination))


print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))