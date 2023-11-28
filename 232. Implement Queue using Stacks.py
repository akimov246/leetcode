class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int | None:
        return self.queue[0] if not self.empty() else None

    def empty(self) -> bool:
        return not self.queue

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(7)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()