import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        heap = [(-((p + 1) / (t + 1) - (p / t)), (p, t)) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, (p, t) = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-((p + 1) / (t + 1) - (p / t)), (p, t)))

        return float(f'{(sum(p / t for _, (p, t) in heap) / len(classes)):.5f}')

print(Solution().maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))