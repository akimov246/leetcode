class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for ball in range(lowLimit, highLimit + 1):
            number = sum(int(n) for n in str(ball))
            boxes[number] = boxes.get(number, 0) + 1
        return max(boxes.values())

print(Solution().countBalls(lowLimit = 1, highLimit = 10))