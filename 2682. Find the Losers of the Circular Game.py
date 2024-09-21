class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        friends = set(range(n))
        current = 0
        received = set()
        counter = 1
        while True:
            if current % n in received:
                break
            received.add(current)
            current += counter * k
            current %= n
            counter += 1

        return sorted(list(f + 1 for f in friends.difference(received)))

print(Solution().circularGameLosers(n = 5, k = 2))